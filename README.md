# mecharmpi270
Work project on using the MechArm Pi 270 to automate clinical processes

## Need
The Abaxis VetScan HM5 hematology analyzer requires clinics to initiate a tube cleaning process by pressing a button on its capacitive touchscreen. With our workplace operating two clinics in different cities, this necessitates staff travel to the remote location solely to activate the function. This is costly in both monetary terms (e.g., travel expenses) and staff time, diverting resources from patient care.

## Solution
Use a MechArm Pi 270 from Elephant Robotics, modified with a stylus that simulates a human finger touch on the VetScan HM5's capacitive touchscreen by grounding it to the Raspberry Pi in the arm's base. The arm is controlled remotely via a game controller (e.g., joystick or gamepad), allowing staff to operate it from the main clinic without travel. The program runs on the Raspberry Pi, receiving instructions over a secure network, positioning the arm to press the button, and providing real-time camera feedback for alignment. This automation reduces costs, saves time, and enhances efficiency.

The system is designed for minimal use (once a week for <5 minutes by one doctor), prioritizing simplicity, security, and cross-platform accessibility (laptop and iPhone via a responsive web UI).

### Hardware Modifications
- **Stylus Setup**: A metal stylus with a soft rubber tip is wrapped in copper tape (conductive adhesive) at the tip to create a ~1/4 inch contact area, contacting the metal body for conductivity.
- **Grounding**: A copper wire (cut from a jumper wire) connects the stylus to a GND pin on the Raspberry Pi (e.g., pin 6). The wire is routed along the arm with zip ties for a clean look.
- **Mounting**: The stylus is secured to the MechArm's end-effector (ATOM module) with tape or a 3D-printed holder.
- **Testing**: Manual tests confirm 10/10 successful taps with light contact, calibrated using the arm's camera.

If passive grounding is unreliable, a micro servo can be added for active press/release, controlled via GPIO.

### Tech Stack
The project uses Python for ease of development, with optional C++ for performance-critical tasks (e.g., low-latency GPIO if needed). The stack is lightweight, running on the Raspberry Pi 4, and supports real-time control, security, and cross-platform UI.

| Layer              | Technology                              | Purpose                                                                 |
|--------------------|-----------------------------------------|-------------------------------------------------------------------------|
| Robot SDK          | pymycobot (Python)                     | Control MechArm to position stylus for VetScan HM5 touchscreen press    |
| Hardware I/O       | Raspberry Pi GPIO (Python, C++ opt.), Copper Tape, Copper Wire | Ground stylus with tape tip and wire; C++ for low-latency GPIO if needed |
| Controller Input   | Gamepad API (JavaScript)               | Gamepad input for arm control via browser (laptop/iPhone)               |
| Vision System      | OpenCV (Python), MJPEG (Picamera2)     | Camera feed to monitor stylus alignment                                 |
| Communication      | Websockets (`python-socketio`)         | Real-time messaging for control and video between Pi and clients        |
| Interface Layer    | Streamlit (Python), JavaScript         | Single responsive web GUI for camera view and gamepad on laptop/iPhone  |
| Security           | TLS/SSL (`wss://`), API keys           | Secure remote access and authentication for clinic use                  |
| Network            | ngrok                                  | Secure tunneling for cross-city access to Pi                           |
| Safety             | Software E-stop (pymycobot API)        | Emergency stop in GUI to prevent arm mishaps                            |
| Packaging          | PyInstaller                            | Deploy backend (Pi) and client app                                     |

- **Why Python-Focused?** Python handles 90%+ of the code for rapid development. C++ is optional (via WiringPi and `ctypes`) and deferred until needed (e.g., for GPIO latency).
- **UI Details**: Streamlit provides a browser-based, mobile-responsive interface, embedding MJPEG camera stream and JavaScript Gamepad API