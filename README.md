# Maya Tool Release

Autodesk Maya / 게임 파이프라인용 Python 툴 모음의 **배포(release) 저장소**입니다.
리깅 · 모델링 · 애니메이션 · 페이셜 작업을 자동화하는 툴들을 셸프 버튼으로 손쉽게 설치해 쓸 수 있습니다.

- **제작**: Ji Hun Park (Junny)
- **대상 DCC**: Autodesk Maya (Python 3 / `maya.cmds`, 일부 PySide)
- **OS**: Windows
- **라이선스**: [MIT](./LICENSE)

> 이 저장소는 **사용자 배포용**입니다. 개발 소스가 아니라, 바로 설치해서 쓸 수 있도록 패키징된 결과물만 담겨 있습니다.

---

## 1. 다운로드 · 설치

### 방법 A — `install.bat` 파일 하나로 자동 설치 (가장 간단, 권장)

빈 폴더를 하나 만들고 그 안에 **`install.bat` 파일 하나만** 넣은 뒤 더블클릭하세요.

- **처음 실행**: 저장소를 그 폴더 아래 `Maya_Tool_Release` 하위 폴더로 **자동 `git clone`** 한 뒤,
  Maya 경로 등록(`setup_app_dir.py`)까지 한 번에 끝냅니다. → **2장(첫 설정)을 따로 할 필요가 없습니다.**
- **이후 실행**: 이미 받은 저장소를 **최신 상태로 업데이트**합니다(= 4장 업데이트와 동일).
- 이미 `git clone` 으로 받은 저장소 폴더 안에서 실행하면 **그 자리에서** 업데이트합니다.

> `install.bat` 은 이 저장소 루트에도 들어 있으니, 받은 폴더에서 그대로 실행해도 됩니다.
> **요건**: [Git](https://git-scm.com/) 과 [Python 3](https://www.python.org/)(런처 `py`)이 설치되어 있어야
> 합니다. 없으면 `install.bat` 이 어떤 것을 설치해야 하는지 안내 메시지를 띄우고 멈춥니다.

### 방법 B — Git 으로 직접 클론

```bash
git clone https://github.com/elom1213/Maya_Tool_Release.git
```

클론해 두면 아래 **업데이트** 한 번으로 항상 최신 버전을 받을 수 있습니다.

### 방법 C — ZIP 다운로드

GitHub 페이지 우측 상단 **`Code` ▸ `Download ZIP`** 로 받아 원하는 위치에 압축을 풉니다.
(이 경우 업데이트는 다시 ZIP 을 받아 덮어써야 합니다.)

---

## 2. 첫 설정 (Maya 에 경로 등록)

> **방법 A(`install.bat`)로 설치했다면 이 단계는 이미 자동으로 끝나 있습니다.** 곧바로 3장으로 가세요.

(방법 B/C 로 받은 경우) 처음 받은 직후 **`update.bat`** 을 한 번 실행하세요. 내부적으로 `setup_app_dir.py`
가 실행되어 Maya `scripts/userSetup.py` 에 이 저장소의 `tools/` 경로가 등록됩니다.

- 이렇게 하면 Maya 시작 시 툴 경로가 자동으로 `sys.path` 에 잡혀, 셸프 버튼이 안정적으로 동작합니다.
- 설정 후 **Maya 를 재시작**하면 적용됩니다. (스크립트 에디터에 `JUN Tools Loaded` 가 출력됩니다.)
- 폴더 위치를 옮긴 경우 `update.bat` 을 다시 실행해 경로를 갱신하세요.

## 3. 툴 설치 (Maya 셸프 버튼 만들기)

1. 사용할 툴 폴더를 엽니다. 예: `tools/A00110_animTool/`
2. 그 안의 **`__dragDrop_*.py`** 파일(예: `__dragDrop_A00110.py`, 일부 툴은 `__dragDrop.py`)을
   **Maya 뷰포트 안으로 드래그&드롭** 합니다.
3. 현재 활성화된 셸프에 **버튼이 자동 생성**됩니다. 이후엔 그 버튼만 누르면 툴이 실행됩니다.

> 받은 폴더의 **위치를 옮기면** 위 1장의 `update.bat` 을 다시 실행해 경로를 갱신하고,
> 셸프 버튼도 다시 만들어 주세요(파일을 다시 드래그&드롭).

---

## 4. 업데이트

클론으로 받았다면, 저장소 루트의 **`update.bat`**(또는 **`install.bat`**) 을 더블클릭하세요. 두 단계를 수행합니다.

1. `update.py` — `git fetch` → `git reset --hard origin/master` → `git clean -fd` 로
   **원격 최신 상태로 강제 동기화**합니다.
2. `setup_app_dir.py` — Maya `scripts/userSetup.py` 에 `tools/` 경로를 (재)등록합니다.

- 즉, 이 폴더 안에서 직접 수정한 파일은 업데이트 시 사라집니다. 개인 수정본은 별도 위치에 보관하세요.
- 업데이트 후에는 셸프 버튼을 다시 만들 필요 없이 그대로 사용하면 됩니다(폴더 위치가 그대로일 때).

---

## 5. 수록 툴

각 툴 폴더 안에 안내 문서가 있는 경우 `docs/` 하위에 함께 들어 있습니다(예: `tools/A00110_animTool/docs/`).

| 툴 | 도메인 | 설명 |
|----|--------|------|
| `A00030_quickTool` | 공용 | 자주 쓰는 작업을 모은 퀵 툴 |
| `A00040_file_exporter` | 파이프라인 | 파일 익스포트 도우미 |
| `A00050_uvTool` | 모델링 | UV 작업 보조 |
| `A00110_animTool` | 애니메이션 | SmartLayer 기반 애니메이션/베이크 툴 |
| `A00170_driverTool` | 리깅 | 드라이버(Set Driven Key) 작업 |
| `A00180_abSymMesh` | 모델링 | 메시 대칭(symmetry) 처리 |
| `A00190_FKIK_General_Tool` | 리깅 | FK ↔ IK 전환 |
| `A00200_CSV_tool` | 페이셜 | ARKit 페이셜 CSV 임포트 |

> 각 툴의 자세한 사용법은 해당 툴 폴더의 `docs/*.md` 문서를 참고하세요.

---

## 6. 요구 환경

- Autodesk Maya (Python 3 기반 버전)
- Windows
- 업데이트 기능 사용 시 [Git](https://git-scm.com/) 설치 필요

---

## 7. 문제 해결

- **드래그&드롭 해도 버튼이 안 생겨요**: Maya **뷰포트(3D 화면)** 안에 떨어뜨렸는지 확인하세요.
  스크립트 에디터나 다른 패널이 아니라 뷰포트여야 합니다.
- **버튼을 눌렀더니 import 오류가 나요**: 폴더를 옮긴 경우입니다. `update.bat` 을 다시 실행해 경로를
  갱신한 뒤, 해당 툴의 `__dragDrop_*.py` 를 다시 드래그&드롭해 버튼을 재생성하세요.
- **`update.bat` 이 동작하지 않아요**: Git 이 설치되어 있는지, 그리고 이 폴더가 `git clone` 으로 받은
  폴더인지 확인하세요(ZIP 으로 받은 폴더는 업데이트가 불가합니다).
