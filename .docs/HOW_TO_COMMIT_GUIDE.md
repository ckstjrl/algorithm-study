# 커밋 가이드

---

### 환경 : VSCODE 기준

<br>

---

## 커밋 컨벤션 설정하기

### 1. 클론한 본인 레포지토리 > .gitmessage.txt 확인
<img width="817" height="381" alt="git_main" src="https://github.com/user-attachments/assets/4213f313-d535-4f27-b107-9462134b762e" />

### 2. CLI 창에서 본인 레포지토리 위치까지 들어가기
- 반드시 `main` 혹은 `master`가 옆에 표시되는 깃 폴더인지 확인 
- `ls -a` 커맨드를 통해 `.gitmessage.txt`가 있는지 확인!!
<img width="576" height="308" alt="git_ls_a" src="https://github.com/user-attachments/assets/ead854b1-5e9b-48a4-9511-cc6265938fcc" />

### 3. 커밋 템플릿을 적용하기
- 커밋 템플릿을 적용하는 부분은 `global`과 `local`로 크게 두 가지로 나뉩니다.
    1. `global` -> 로컬에서 커밋하는 모든 커밋 메세지에 템플릿 적용
        - `git config --global commit.template .gitmessage.txt`
    2. `local` -> 해당 프로젝트에만 커밋 메세지 템플릿을 적용
        - `$ git config commit.template .gitmessage.txt`
    <img width="473" height="331" alt="git_global_template" src="https://github.com/user-attachments/assets/b54473c7-1330-4c0a-b905-8d74837bf49d" />


---

## 설정한 커밋 컨벤션 활용해 커밋하기

### VSCODE 내 Source Control 활용
### 1. 커밋을 위한 준비하기
- `git add` 를 통해 Staging Area에 해당 파일 업로드
<img width="621" height="239" alt="add_via_sc" src="https://github.com/user-attachments/assets/9160726b-3145-44b2-aa76-913f2afe108f" />

### 2. 커밋하기
- 변경한 내용을 커밋한다
<img width="494" height="239" alt="commit_button" src="https://github.com/user-attachments/assets/61565bb7-f4bf-47b1-850d-b944f2b1ef03" />

- 커밋 버튼을 누르면 아래와 같은 화면이 나온다.
- 해당 화면에서 커밋 텍스트를 작성 후 우측 상단의 체크를 누르면 커밋이 된다.

<img width="1871" height="660" alt="commit_text" src="https://github.com/user-attachments/assets/1b1bf5c9-d9f0-4b93-ab67-1aefac328ead" />

### 3.sync change(pull&push)

- 커밋을 원격 저장소에 푸시하기 위해 sync change 버튼을 눌러 pull & push 진행
- 기존의 CLI에서 git pull과 git push를 따로 할 필요 없이 한 번 에 진행하는 버튼

<img width="217" height="225" alt="Image" src="https://github.com/user-attachments/assets/0c49bd64-e0fe-4043-b794-1f9a5473f41d" />

---

### Git bash 등 CLI 환경 활용
### 1. 커밋을 위한 준비하기
- `git add` 를 통해 Staging Area에 해당 파일 업로드
<img width="549" height="163" alt="git_add_cli" src="https://github.com/user-attachments/assets/7065b52f-2f36-4474-a206-d7d6367162ff" />

- `git commit` CLI 창에 입력
<img width="488" height="159" alt="git_commit_cli" src="https://github.com/user-attachments/assets/e7dde437-4847-4c61-9b63-0a5e852e2262" />

### 2. 커밋을 하면 vim editor가 열린다.
- vim 에디터가 열리면 아래와 같은 화면이 나타난다.
<img width="1008" height="582" alt="vim" src="https://github.com/user-attachments/assets/970e63da-cd60-429a-856b-bdb0c0649915" />

- `I`를 눌러 vim의 INSERT 모드로 들어간다.
<img width="434" height="160" alt="vim_INSERT" src="https://github.com/user-attachments/assets/122a8152-fc03-49cf-80aa-6d34cbe675e5" />

### 3. 커밋 내용을 작성하고 `esc`를 눌러 `:wq`를 눌러 작성한 것을 저장한다.
<img width="448" height="583" alt="Image" src="https://github.com/user-attachments/assets/bf5fdda1-f85d-4e3c-93a1-be351ec05300" />

- 만약 무언가를 잘못눌렀다면 `esc` 후 `:qa!`

### 4. 이후에는 기존 방식처럼 PUSH!

---