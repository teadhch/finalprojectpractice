from fashion_clip.fashion_clip import FashionCLIP
import numpy as np

fclip = FashionCLIP("fashion-clip")

images = [
    r"D:\2025_langchain_aivision\finalproject\data\results\detected\lo_e1281_c1_frame_00005s_person_1.jpg"
]

texts = [
    # "a person wearing red jacket",
    # "a person wearing black pants",
    # "a person wearing white shirt",
    # "a person wearing gray shorts",
    "a person wearing white shirt and gray shorts, white shoes",
    # "a person wearing white shoes"
]

image_embeddings = fclip.encode_images(images, batch_size=32)
text_embeddings = fclip.encode_text(texts, batch_size=32)

image_embeddings = image_embeddings / np.linalg.norm(
    image_embeddings,
    ord=2,
    axis=-1,
    keepdims=True
)

text_embeddings = text_embeddings / np.linalg.norm(
    text_embeddings,
    ord=2,
    axis=-1,
    keepdims=True
)

similarity = image_embeddings @ text_embeddings.T

print(similarity)