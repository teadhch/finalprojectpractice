from torchreid.utils import FeatureExtractor
from pathlib import Path
import torch.nn.functional as F

image_dir = Path("data/results/detected")
extractor = FeatureExtractor(
    model_name="osnet_x1_0",
    device="cpu"
)

image_paths = []
for ext in ["*.jpg"]:
    image_paths.extend(image_dir.glob(ext))

image_paths = sorted(image_paths)
print(len(image_paths))
image_paths = [str(path) for path in sorted(image_paths)]

if not image_paths:
    print("사람 crop 이미지가 없습니다.")
else:
    features = extractor(image_paths)

for i in range(len(features)):
    for j in range(i + 1, len(features)):
        similarity = F.cosine_similarity(
            features[i].unsqueeze(0),
            features[j].unsqueeze(0)
        ).item()

        print(image_paths[i], image_paths[j], similarity)