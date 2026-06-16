from ultralytics import YOLO
from pathlib import Path
import cv2
model = YOLO("yolov8n.pt")
image_dir = Path("data/results/frames")

image_paths = []
for ext in ["*.jpg"]:
    image_paths.extend(image_dir.glob(ext))
image_paths = sorted(image_paths)

results = model.predict(source=image_paths, classes=0, conf=0.1, save=False)
for image_path, r in zip(image_paths, results) :
    frame = cv2.imread(str(image_path))

    if frame is None:
        continue

    for person_idx, box in enumerate(r.boxes, 1):
        print(box.xyxy[0])
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)