# ──────────────────────────────────────────────────────────
# 1. 라이브러리 임포트 및 한글 폰트 설정 (런타임 재시작 불필요)
# ──────────────────────────────────────────────────────────

import os
import matplotlib.font_manager as fm

import cv2                      # OpenCV: 이미지 처리 핵심 라이브러리
import numpy as np              # NumPy: 숫자 배열(행렬) 계산
import matplotlib.pyplot as plt # Matplotlib: 그래프/이미지 시각화
from matplotlib import rcParams

cap = cv2.VideoCapture('opencv.mp4')

fps = cap.get(cv2.CAP_PROP_FPS) # 초당 프레임수
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 가로 길이
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 세로 길이
total_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 총 프레임수
print(fps, width, height, total_frame)

sample_frames = []
positions = [ i*int(fps) for i in range(int(total_frame/fps)) if i % 5 == 0]

for pos in positions:
  cap.set(cv2.CAP_PROP_POS_FRAMES, pos) # 특정 프레임으로 이동 함수
  ret, frame = cap.read() # 동영상에서 현재 프레임을 읽어옴 (ret : True / False, frame : 읽어온 프레임)
  if ret :
    # 추출된 프레임 또한 matplotlib로 출력하기 위해서는 RGB로 바꿔야 한다.
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    sample_frames.append(frame_rgb)

    
# 사용한 영상(동영상파일, 캠)에 대한 자원 해제
cap.release()

