# HomeGuard – Your Personal Room Security System 🛡️📸

HomeGuard is a smart security system that continuously monitors your room using a camera. If it detects someone entering the room, it captures a photo and instantly sends it to your email! 📧📲

## Features 🔒

- **Real-time monitoring** – Continuously observes your room using a webcam.
- **Intruder detection** – Uses AI-powered YOLOv8 object detection to identify humans.
- **Instant alerts** – Captures an image and emails it when a person is detected.
- **Secure communication** – Sends email notifications via SSL encryption.
- **Runs on CPU/GPU** – Works efficiently on your computer, using CUDA if available.

## Installation & Setup ⚙️

### Prerequisites

Make sure you have Python installed. Then, install the required dependencies:

```sh
pip install torch numpy opencv-python ultralytics supervision smtplib ssl
```

### Configuration

Before running, update the script with your email credentials:

```python
email_sender = 'your_email@gmail.com'
passwd = 'your_password'
email_receiver = 'recipient_email@gmail.com'
```

> **Note:** Consider using an **App Password** instead of your actual email password for security.

## How to Run ⚡

Simply execute the script:

```sh
python homeguard.py
```

Press `q` to exit the program.

## How It Works 🤖

1. The camera captures real-time footage.
2. YOLOv8 detects if a person is present.
3. If a person is found, a photo is taken.
4. The captured image is sent to your email instantly.

## Example Screenshot 📸

*(Example image of detection output can be added here)*

## Future Improvements ⚙

- Add motion detection to reduce false positives.
- Implement cloud storage for detected images.
- Enable multi-camera support.

## License 📜

HomeGuard is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**. This means:

- You are free to use, modify, and share this project.
- Any modifications or derivative works must also be open-sourced under AGPL-3.0.
- If you distribute or deploy this software as a service, you must provide access to the full source code.

See the full license text [here](https://www.gnu.org/licenses/agpl-3.0.html).

## Third-Party Licenses 📄

This project uses third-party libraries, each with its respective license:

- **YOLOv8 (Ultralytics)** – Licensed under AGPL-3.0 ([Source](https://github.com/ultralytics/ultralytics))
- **Supervision** – Licensed under Apache 2.0 ([Source](https://github.com/roboflow/supervision))
- **OpenCV** – Licensed under Apache 2.0 ([Source](https://github.com/opencv/opencv))
- **NumPy** – Licensed under BSD-3-Clause ([Source](https://github.com/numpy/numpy))
- **Torch (PyTorch)** – Licensed under BSD-style ([Source](https://github.com/pytorch/pytorch))

By using HomeGuard, you agree to comply with the terms of these third-party licenses.

## Disclaimer ⚠️

This project is for **personal use only** and should not be used for unlawful surveillance.

---

Enjoy HomeGuard and keep your space secure! 🏡🛡️
