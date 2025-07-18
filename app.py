import tkinter as tk
from tkinter import filedialog
import threading
import cv2
import util
from sort.sort import *
from ultralytics import YOLO
from util import get_car, read_license_plate, write_csv
import subprocess


def process_video(video_path):
    results = {}
    mot_tracker = Sort()

    # Load models (assuming models are loaded outside the function)
    coco_model = YOLO('yolov8n.pt')
    license_plate_detector = YOLO('./license_plate_detector.pt')

    # Load video
    cap = cv2.VideoCapture(video_path)
    vehicles = [2, 3, 5, 7]

    # Read frames
    frame_nmr = -1
    ret = True
    while ret:
        frame_nmr += 1
        ret, frame = cap.read()
        if ret:
            results[frame_nmr] = {}

            # Detect vehicles (replace with your implementation)
            detections = coco_model(frame)[0]
            detections_ = []
            for detection in detections.boxes.data.tolist():  # Assuming detections are available
                x1, y1, x2, y2, score, class_id = detection
                if int(class_id) in vehicles:
                    detections_.append([x1, y1, x2, y2, score])

            # Track vehicles
            track_ids = mot_tracker.update(np.asarray(detections_))

            # Detect license plates (replace with your implementation)
            license_plates = license_plate_detector(frame)[0]
            for license_plate in license_plates.boxes.data.tolist():
                x1, y1, x2, y2, score, class_id = license_plate

                # Assign license plate to car
                xcar1, ycar1, xcar2, ycar2, car_id = get_car(license_plate, track_ids)

                if car_id != -1:

                    # Process license plate (replace with your implementation)
                    license_plate_crop = frame[int(y1):int(y2), int(x1): int(x2), :]
                    # ... (license plate processing logic)
                    license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
                    _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV)

                    license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_thresh)

                    if license_plate_text is not None:
                        results[frame_nmr][car_id] = {'car': {'bbox': [xcar1, ycar1, xcar2, ycar2]},
                                                      'license_plate': {'bbox': [x1, y1, x2, y2],
                                                                        'text': license_plate_text,
                                                                        'bbox_score': score,
                                                                        'text_score': license_plate_text_score}}

            # Write results (optional, if needed)
    write_csv(results, './test.csv')

            # Capture output from execute.py
    with open('output.txt', 'w') as f:
        process = subprocess.Popen(['python', 'execute.py'], stdout=f)
        process.wait()  # Wait for the process to finish

            # Read the captured output
    with open('output.txt', 'r') as f:
            output_text = f.read()

    cap.release()
    print(output_text)
    return output_text

import tkinter as tk
from tkinter import filedialog
import threading

def upload_and_run():
    video_path = filedialog.askopenfilename(title="Select Video", filetypes=[("MP4 Files", "*.mp4")])
    if not video_path:
        print("Video not found")
        return

    def run_and_capture_output():           
        output_text = process_video(video_path)
        update_output_display(output_text)

    thread = threading.Thread(target=run_and_capture_output)
    thread.start()

    output_label.config(text="Processing video...")

def update_output_display(output_text):
    output_label.config(state=tk.NORMAL)
    output_label.delete(1.0, tk.END)  # Clear previous text
    output_label.insert(tk.END, output_text)
    output_label.config(state=tk.DISABLED)


window = tk.Tk()
window.title("Unathorized vechile DEtection in brt lane")

# Centering the window on the screen
window_width = 400
window_height = 300
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width/2) - (window_width/2)
y_coordinate = (screen_height/2) - (window_height/2)
window.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Title/Header
title_label = tk.Label(window, text="License Plate Detector", font=("Arial", 16))
title_label.pack(pady=10)

# Upload button
upload_button = tk.Button(window, text="Upload Video", command=upload_and_run)
upload_button.pack(pady=5)

# Output label with scrollbar
output_frame = tk.Frame(window)
output_frame.pack(pady=5)
output_scrollbar = tk.Scrollbar(output_frame)
output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_label = tk.Text(output_frame, font=("Arial", 12), width=50, height=10, wrap=tk.WORD, yscrollcommand=output_scrollbar.set)
output_label.pack()
output_scrollbar.config(command=output_label.yview)

window.mainloop()




