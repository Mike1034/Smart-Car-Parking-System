import cv2
import numpy as np
import pickle
import pandas as pd
import cvzone
from ultralytics import YOLO

# Load parking area data
file_path = "smartcarparking.pickle" 
with open(file_path, "rb") as f:
    data = pickle.load(f)
    polylines, area_names = data.get('polylines', []), data.get('area_names', [])

# Load class list for YOLO model
with open("coco.txt", "r") as my_file:
    class_list = my_file.read().split("\n")

# Initialize YOLO model
model = YOLO('yolov8s.pt')

# Initialize video capture
cap = cv2.VideoCapture('easy1.mp4')
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
   
    count += 1
    if count % 3 != 0:
        continue

    frame = cv2.resize(frame, (1020, 500))
    frame_copy = frame.copy()

    # Predict with YOLO model
    results = model.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")
    
    # Extract centroids of detected cars
    list1 = []
    for index, row in px.iterrows():
        x1, y1, x2, y2, _, d = row
        c = class_list[int(d)]
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)
        if 'car' in c:
            list1.append((cx, cy))

    # Count cars in parking areas
    counter1 = []
    list2 = []
    for i, polyline in enumerate(polylines):
        list2.append(i)
        cv2.polylines(frame, [polyline], True, (0, 255, 0), 2)
        cvzone.putTextRect(frame, f'{area_names[i]}', tuple(polyline[0]), 1, 1) 
        
        # Check if centroids are within parking areas
        for cx1, cy1 in list1:
            if cv2.pointPolygonTest(polyline, (cx1, cy1), False) >= 0:
                cv2.circle(frame, (cx1, cy1), 5, (255, 0, 0), -1)
                cv2.polylines(frame, [polyline], True, (0, 0, 255), 2)    
                counter1.append((cx1, cy1))
                break

    # Calculate car count and free space
    car_count = len(counter1)
    free_space = len(list2) - car_count 
    cvzone.putTextRect(frame, f'CARCOUNTER:-{car_count}', (50, 60), 2, 2) 
    cvzone.putTextRect(frame, f'FREESPACE:-{free_space}', (50, 160), 2, 2) 
    cv2.imshow('FRAME', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
