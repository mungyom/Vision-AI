"""설치 확인용 스크립트: python check_setup.py 로 실행하세요."""
import sys

print("Python 버전:", sys.version.split()[0])

ok = True
for name, module in [("NumPy", "numpy"), ("OpenCV", "cv2"),
                     ("Matplotlib", "matplotlib"), ("scikit-image", "skimage")]:
    try:
        m = __import__(module)
        print(f"  [OK] {name} {m.__version__}")
    except ImportError:
        print(f"  [없음] {name}  →  pip install -r requirements.txt 를 실행하세요")
        ok = False

if not ok:
    sys.exit(1)

import numpy as np
import cv2
import matplotlib
matplotlib.use("Agg")          # 창을 띄우지 않고 파일로 저장
import matplotlib.pyplot as plt
from skimage import data

img = data.camera()
edges = cv2.Canny(img, 100, 200)    # OpenCV가 실제로 동작하는지 테스트
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
axes[0].imshow(img, cmap="gray"); axes[0].set_title("Original"); axes[0].axis("off")
axes[1].imshow(edges, cmap="gray"); axes[1].set_title("Edges (OpenCV)"); axes[1].axis("off")
fig.savefig("setup_check.png", bbox_inches="tight")

print("\n[완료] 설치 완료! 같은 폴더에 setup_check.png 그림이 만들어졌습니다. 열어서 확인해 보세요.")
