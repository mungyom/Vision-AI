# Vision-AI: 공장 이미지·영상 AI 분석 학습 과정 (초보 → 기초)

제품 품질 사진, 설비 CCTV 영상을 AI로 분석하기 위한 기초 학습 자료입니다.

## 어디서부터 보면 되나요?

| 순서 | 파일 | 내용 |
|---|---|---|
| 1 | [00_environment.md](00_environment.md) | 실습 환경 고르기 (Colab / VS Code / Claude Code) + 실행 방법 |
| 2 | [01_roadmap.md](01_roadmap.md) | 8주 학습 계획 |
| 3 | [02_local_setup_windows.md](02_local_setup_windows.md) | 내 PC(Windows)에 Python 설치 + VS Code 실행 방법 |
| 4 | [lesson01_theory.md](lesson01_theory.md) | 1강 이론: 이미지는 숫자다 |
| 5 | [notebooks/lesson01_image_basics.ipynb](notebooks/lesson01_image_basics.ipynb) | 1강 실습 (Colab에서 실행) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mungyom/Vision-AI/blob/claude/project-thread-csjf9x/notebooks/lesson01_image_basics.ipynb) |
| 6 | [lesson02_theory.md](lesson02_theory.md) | 2강 이론: 전처리 (크기·ROI·블러·이진화·정규화) |
| 7 | [notebooks/lesson02_preprocessing.ipynb](notebooks/lesson02_preprocessing.ipynb) | 2강 실습 + 1강 문법 보충 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mungyom/Vision-AI/blob/claude/project-thread-csjf9x/notebooks/lesson02_preprocessing.ipynb) |
| 8 | [lesson03_theory.md](lesson03_theory.md) | 3강 이론: 규칙 기반 검사 (엣지·컨투어·치수 측정) |
| 9 | [notebooks/lesson03_rule_based_inspection.ipynb](notebooks/lesson03_rule_based_inspection.ipynb) | 3강 실습: 도면 규격 검사기 + 개수 세기 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mungyom/Vision-AI/blob/claude/project-thread-csjf9x/notebooks/lesson03_rule_based_inspection.ipynb) |

## 실행 확인 파일

- `requirements.txt`: 내 PC에 설치할 라이브러리 목록
- `check_setup.py`: 설치가 잘 됐는지 확인 (`python check_setup.py`)

## 원칙

- 학습 단계에서는 **공개 샘플 데이터만** 사용합니다. 회사 이미지는 보안 확인 후 사용합니다.
- 모르는 것은 바로 Claude에게 물어봅니다.
