from PIL import Image
from transformers import CLIPModel, CLIPProcessor
import torch

model = CLIPModel.from_pretrained("patrickjohncyh/fashion-clip")
processor = CLIPProcessor.from_pretrained("patrickjohncyh/fashion-clip")

image = Image.open(
    r"D:\2025_langchain_aivision\finalproject\data\results\detected\lo_e1281_c1_frame_00005s_person_1.jpg"
).convert("RGB")

texts = [
    # "gray shorts, white shirt",
    # "red hat, blue skirt, green shirt",
    # "white shirt, black shorts",
    # "white shirt, gray shorts, green hat, white shoes",
    # "white shirt",
    "black shirt"

]

inputs = processor(
    text=texts,
    images=image,
    return_tensors="pt",
    padding=True
)

with torch.no_grad():
    outputs = model(**inputs)

scores = outputs.logits_per_image.softmax(dim=1)[0]

for text, score in zip(texts, scores):
    print(text, float(score))