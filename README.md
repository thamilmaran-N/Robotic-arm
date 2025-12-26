# Robotic Arm

## Project Overview
This project demonstrates a **bionic arm finger movement mechanism** using **five servo motors** controlled by PWM signals. Each servo represents a finger and rotates smoothly from **0° to 180°** in a **sequential order**, simulating natural finger movement. The system is implemented using **MicroPython** on a Raspberry Pi Pico / Pico W and works completely offline.

---

## Project Objectives
- Control five servo motors using PWM  
- Achieve full 0°–180° rotation for each servo  
- Perform smooth and sequential finger movement  
- Simulate basic bionic/prosthetic hand motion  
- Ensure stable and calibrated servo operation  

---

## Hardware Requirements
- Raspberry Pi Pico / Pico W  
- 5 × Servo Motors (SG90 / MG90S or equivalent)  
- External 5V power supply (recommended for servos)  
- Connecting wires  

---

## Pin Configuration
| Servo | Pico GPIO Pin |
|------|---------------|
| Servo 1 | GP0 |
| Servo 2 | GP1 |
| Servo 3 | GP2 |
| Servo 4 | GP3 |
| Servo 5 | GP4 |

Servo motors should be powered using an external 5V supply with a common ground to the Pico.

---

## Software Requirements
- MicroPython firmware for Raspberry Pi Pico / Pico W  
- Thonny IDE  

### Libraries Used (Built-in)
- `machine` – For GPIO and PWM control  
- `time` – For delay and timing control  

No external libraries are required.

---

## Working Principle
- Each servo motor is controlled using a **50 Hz PWM signal**.  
- The duty cycle is mapped to pulse widths between **500 µs and 2500 µs**, corresponding to **0°–180° rotation**.  
- The program moves the servos smoothly using incremental angle steps.  
- Servos rotate in a predefined **sequential pattern**, holding each position for a fixed duration.  
- After completing the sequence, all servos return to the initial 0° position.

---

## Movement Sequence
1. All servos move to 180°  
2. Servo 1 moves to 0°  
3. Servo 2 moves to 0°  
4. Servo 3 moves to 0°  
5. Servo 4 moves to 0°  
6. Servo 5 moves to 0°  
7. Selected servos return to 180°  
8. All servos finally return to 0°  

Each step is held for **10 seconds** with smooth transitions.

---

## Output
- Smooth and stable servo rotation  
- Sequential finger-like movement  
- Accurate 0°–180° positioning  
- Reliable PWM-based control
<img width="896" height="1280" alt="image" src="https://github.com/user-attachments/assets/6e5cad5f-676a-44c8-b40e-30f02ca17550" />

<img width="706" height="1296" alt="image" src="https://github.com/user-attachments/assets/dc0d7f7d-c341-497d-add7-97f2e2693197" />

---

## Applications
- Bionic / prosthetic arm prototypes  
- Biomedical engineering projects  
- Robotics finger actuation  
- Rehabilitation and assistive devices  
- Educational demonstrations  

---

## Conclusion
This project successfully demonstrates a **simple, low-cost bionic arm control system** using PWM-controlled servo motors. The sequential and smooth movement provides a strong foundation for advanced prosthetic control systems.

---

## 🔮 Future Enhancements
- Integration of EMG sensors for muscle-based control  
- Wireless control using Bluetooth or Wi-Fi  
- Individual finger force control  
- Gesture-based control algorithms  
- Integration with IoT dashboards for monitoring  

---
