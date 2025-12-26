# five_servo_sequence.py
from machine import Pin, PWM
from time import sleep

class Servo:
    def __init__(self, pin, freq=50, min_us=500, max_us=2500):
        self.pin_num = pin
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(freq)
        self.freq = freq
        self.min_us = int(min_us)
        self.max_us = int(max_us)
        self.period_us = int(1_000_000 // freq)

    def angle_to_duty(self, angle):
        angle = max(0, min(180, int(angle)))
        pulse_us = self.min_us + (angle / 180.0) * (self.max_us - self.min_us)
        duty_fraction = pulse_us / self.period_us
        duty_u16 = int(duty_fraction * 65535)
        return int(pulse_us), duty_u16

    def write(self, angle, debug=False):
        pulse_us, duty = self.angle_to_duty(angle)
        self.pwm.duty_u16(duty)
        if debug:
            print("Pin", self.pin_num, "angle", angle, "pulse", pulse_us, "duty", duty)

    def deinit(self):
        try:
            self.pwm.deinit()
        except:
            pass

# Configure servos (GP0..GP4)
pins = [0, 1, 2, 3, 4]

# Per-servo calibration (min_us, max_us)
calibrations = [
    (500, 2500),
    (500, 2500),
    (500, 2500),
    (500, 2500),
    (500, 2500),
]

servos = [Servo(pin=p, min_us=c[0], max_us=c[1]) for p, c in zip(pins, calibrations)]

def smooth_move(current, target, step_delay=0.01):
    """
    current, target: lists of 5 angles
    Smoothly moves servos from current -> target.
    """
    steps = max(abs(target[i] - current[i]) for i in range(5))
    if steps == 0:
        return target

    for step in range(1, steps + 1):
        intermediate = []
        for i in range(5):
            cur = current[i]
            tgt = target[i]
            if tgt > cur:
                val = min(tgt, cur + step)
            elif tgt < cur:
                val = max(tgt, cur - step)
            else:
                val = cur
            intermediate.append(val)

        for s, ang in zip(servos, intermediate):
            s.write(ang)
        sleep(step_delay)

    return target

def set_positions_immediate(angles):
    for s, a in zip(servos, angles):
        s.write(a)

# Sequential movement pattern
SEQUENCE = [
    ([180, 180, 180, 180, 180], 10),
    ([0,   180, 180, 180, 180], 10),
    ([0,   0,   180, 180, 180], 10),
    ([0,   0,   0,   180, 180], 10),
    ([0,   0,   0,   0,   180], 10),
    ([0,   0,   0,   0,   0  ], 10),
    ([180, 180, 0,   0,   0  ], 10),
]

# Main program
if __name__ == "__main__":
    try:
        current = [0, 0, 0, 0, 0]
        print("Init: moving all to 0°")
        set_positions_immediate(current)
        sleep(1)

        print("Starting sequence. Each step holds for 10 seconds.")
        for idx, (angles, duration) in enumerate(SEQUENCE, start=1):
            print("Step", idx, "->", angles)
            current = smooth_move(current, angles, step_delay=0.005)
            sleep(duration)

        print("Sequence finished. Returning to 0°")
        current = smooth_move(current, [0, 0, 0, 0, 0], step_delay=0.005)
        sleep(1)

    finally:
        for s in servos:
            s.deinit()
        print("Servos deinitialized.")
