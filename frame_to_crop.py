from pathlib import Path
from ultralytics import YOLO

BASE_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = BASE_DIR / "images"
OUTPUT_DIR = BASE_DIR / "output"

model = YOLO("yolov8m.pt")

folder_path = Path(IMAGE_PATH)

image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}