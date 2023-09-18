import torch
import numpy as np
import cv2
from time import time
from ultralytics import YOLO
import supervision as sv

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


email_sender = 'cygannostale@gmail.com'
passwd = 'dfjw vbgd tgqf gjuh'
email_receiver = 'szymon242820@gmail.com'


def send_email(count, time_now, filename):
    image_open = open(filename, 'rb').read()

    msg = MIMEMultipart()
    msg['Subject'] = f"Homeguard monit {time_now}"
    msg['From'] = email_sender
    msg['To'] = email_receiver
    text = MIMEText(f'Ktoś wlazł do pokoju! {count}')
    msg.attach(text)
    image = MIMEImage(image_open, 'jpg', name='osoba')
    msg.attach(image)

    context_data = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context_data) as mail:
        mail.login(email_sender, passwd)
        mail.sendmail(email_sender, email_receiver, msg.as_string())


class ObjectDetection:
    def __init__(self, capture_index=0):
        self.capture_index = capture_index
        self.email_sent = False
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print('Using Device: ', self.device)
        self.model = self.load_model()
        self.CLASS_NAMES_DICT = self.model.model.names
        self.box_annotator = sv.BoxAnnotator(color=sv.ColorPalette.default(),
                                             thickness=3, text_thickness=3, text_scale=1)

    def load_model(self):
        model = YOLO('yolov8n.pt')
        model.fuse()
        return model

    def predict(self, frame):
        results = self.model(frame)
        return results

    def plot_bboxes(self, results, frame):
        xyxys = []
        confidences = []
        class_ids = []
        for result in results[0]:
            class_id = result.boxes.cls.cpu().numpy().astype(int)
            if class_id == 0:
                xyxys.append(result.boxes.xyxy.cpu().numpy())
                confidences.append(result.boxes.conf.cpu().numpy())
                class_ids.append(result.boxes.cls.cpu().numpy().astype(int))
        detections = sv.Detections.from_ultralytics(results[0])
        frame = self.box_annotator.annotate(scene=frame, detections=detections)
        return frame, class_ids

    def __call__(self):
        cap = cv2.VideoCapture(self.capture_index)
        assert cap.isOpened()
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        frame_count = 0

        while True:
            start_time = time()
            ret, frame = cap.read()
            assert ret
            results = self.predict(frame)
            frame, class_ids = self.plot_bboxes(results, frame)

            if len(class_ids) > 0:
                if not self.email_sent:
                    time_now = time()
                    filename = f'output_{time_now}.jpg'
                    cv2.imwrite(filename, frame)
                    send_email(len(class_ids), time_now, filename)
                    self.email_sent = True
            else:
                self.email_sent = False

            end_time = time()
            fps = 1/np.round(end_time - start_time, 2)
            cv2.putText(frame, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255, 0), 2)
            cv2.imshow('YOLOv8 Detections', frame)
            frame_count += 1

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


detector = ObjectDetection()
detector()
