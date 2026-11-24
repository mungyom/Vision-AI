# 02. 내 PC(Windows)에 Python 설치하고 VS Code에서 실행하기

## 왜 필요한가요?

회사 사진은 회사 밖(Colab 같은 클라우드)으로 내보낼 수 없습니다. 그래서 **실제 회사 품질 사진을 분석할 때는 회사 PC에서 직접 실행**해야 합니다.
학습(1~6주차)은 Colab + 공개 데이터로 하고, 내 PC 환경은 지금 미리 준비해 두면 됩니다.

> GPU(그래픽카드)가 없어도 괜찮습니다. 이미지 처리(OpenCV), 이미 학습된 모델 사용하기, 작은 모델 추가 학습은 CPU로도 충분히 돌아갑니다. 속도가 조금 느릴 뿐입니다.

> 회사 PC라면 프로그램 설치에 IT 부서 승인이 필요할 수 있습니다. 먼저 확인하세요.

---

## 1단계. Python 설치 (약 5분)

1. https://www.python.org/downloads/ 접속
2. **Python 3.12** 버전의 Windows installer (64-bit) 를 받습니다.
   - 가장 최신 버전보다 3.12를 권장합니다. AI 라이브러리들이 최신 버전을 늦게 지원하는 경우가 있기 때문입니다.
   - 3.12 목록은 https://www.python.org/downloads/windows/ 에서 찾을 수 있습니다.
3. 설치 프로그램 첫 화면 맨 아래 **"Add python.exe to PATH"** 를 반드시 체크 ✅
   (이걸 빼먹으면 명령어가 안 먹힙니다. 가장 흔한 실수입니다.)
4. **Install Now** 클릭

### 설치 확인

키보드 `윈도우 키` → `cmd` 입력 → 명령 프롬프트 실행 → 아래 입력:

```
python --version
```

`Python 3.12.x` 처럼 나오면 성공입니다.
`'python'은(는) 내부 또는 외부 명령...` 이 나오면 PATH 체크를 빼먹은 것입니다. 설치 파일을 다시 실행해서 **Modify** → PATH 추가를 하거나, 제거 후 다시 설치하세요.

---

## 2단계. 실습 폴더 만들기 + 가상환경 만들기 (약 5분)

**가상환경**이란? 이 프로젝트 전용 "라이브러리 보관함"입니다. 다른 프로그램과 섞이지 않게 해 줍니다.

1. VS Code 실행 → `File(파일) → Open Folder(폴더 열기)` → 실습 폴더 선택
   (예: `C:\Users\본인계정\Project\vision-ai`)
2. VS Code 메뉴 `Terminal(터미널) → New Terminal(새 터미널)` → 아래쪽에 검은 창이 열립니다.
3. 터미널에 한 줄씩 입력:

```
python -m venv .venv
.venv\Scripts\activate
```

줄 맨 앞에 `(.venv)` 가 보이면 성공입니다.

> 빨간 글씨로 "스크립트를 실행할 수 없으므로…" 오류가 나면 (PowerShell 보안 설정 때문):
> ```
> Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
> ```
> 를 한 번 입력하고 `Y` 를 누른 뒤, 다시 `.venv\Scripts\activate` 를 입력하세요.

---

## 3단계. 라이브러리 설치 (약 3~5분)

GitHub에서 받은 자료 폴더 안에 `requirements.txt` 가 있습니다. 터미널에서:

```
pip install -r requirements.txt
```

(자료를 아직 안 받았다면 아래 한 줄로도 됩니다.)

```
pip install numpy opencv-python matplotlib scikit-image jupyter ipykernel
```

---

## 4단계. 잘 설치됐는지 확인

```
python check_setup.py
```

마지막에 `[완료] 설치 완료!` 가 나오고 `setup_check.png` 파일이 생기면 성공입니다.

---

## 5단계. VS Code 확장 설치 + 노트북 실행

1. VS Code 왼쪽 세로 메뉴의 **네모 4개 아이콘(Extensions)** 클릭
2. `Python` 검색 → Microsoft 것 설치
3. `Jupyter` 검색 → Microsoft 것 설치
4. `notebooks/lesson01_image_basics.ipynb` 파일 열기
5. 오른쪽 위 **Select Kernel(커널 선택)** → `Python Environments` → **`.venv`** 선택
6. 셀 왼쪽 ▶ 버튼 또는 `Shift + Enter` 로 실행 (Colab과 똑같습니다)

---

## 나중에 (4주차 무렵): 딥러닝 라이브러리 설치 (GPU 없는 PC용)

```
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

GPU 없는 PC용(CPU 전용) 버전이라 용량이 작고 설치가 간단합니다. 지금은 안 해도 됩니다.

---

## 막히면

오류 메시지 전체를 복사해서 Claude에게 붙여 넣고 "이 오류 해결해줘"라고 하세요. 스크린샷도 괜찮습니다.
