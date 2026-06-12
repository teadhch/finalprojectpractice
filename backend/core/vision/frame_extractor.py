# ──────────────────────────────────────────────────────────
# 1. 라이브러리 임포트 및 한글 폰트 설정 (런타임 재시작 불필요)
# ──────────────────────────────────────────────────────────

import os
import matplotlib.font_manager as fm

import cv2                      # OpenCV: 이미지 처리 핵심 라이브러리
import numpy as np              # NumPy: 숫자 배열(행렬) 계산
import matplotlib.pyplot as plt # Matplotlib: 그래프/이미지 시각화
from matplotlib import rcParams
