## Git 사용법

- 분산 버전 관리 프로그램

### 로컬 저장소

![git 저장소](https://www.notion.so/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Ff2678325-6f7b-4a25-b188-86c42030d6d5%2F7142d992-3d01-481c-9d4e-e818c6e185d8%2FUntitled.png%3FspaceId%3Df2678325-6f7b-4a25-b188-86c42030d6d5?table=block&id=2cb611ac-3a00-806f-9790-d13a0ade2843&cache=v2)

- `Working Directory`  : 사용자의 일반적인 작업 공간
- `Staging Area`  : 커밋을 위한 작업물이 추가되는 공간
- `Repository`  : Staging area에 있는 작업물의 변경사항을 저장하는 곳

### Git 명령어

- git init
    - 현재 작업 중인 디렉토리를 Git으로 관리하겠다는 명령어
    - `.git` 이라는 숨김 폴더 생성

- git status
    - Working Directory와 Staging Area에 있는 파일의 상태를 알려주는 명령어
        1. Untracked : Git이 관리하지 않는 파일
        2. Tracked : Git이 관리하는 파일
            - Unmodified : 최신 상태
            - Modified : 수정되어 Working Directory에 위치
            - staged : Staging Area에 위치

- git add
    - Working Directory에 위치한 파일을 Staging Area로 올리는 명령어

- git commit
    - Staging Area에 올라온 파일의 변경사항을 커밋하여 저장하는 명령어
    - 커밋 시 변경사항들을 잘 나타낼 수 있도록 `-m "메시지"` 메시지를 작성
    
- git log
    - 커밋의 내역을 조회 할 수 있는 명령어
    - `--oneline`  축약해서 보기

### Github 명령어

- git remote
    1.  등록
        - `add origin [원격저장소 주소]`
    2. 조회
        - `-v`
    3. 삭제
        - `re [이름]` ex) origin
- git push
    - 로컬 저장소의 커밋을 원격저장소로 업로드하는 명령어
    - `git push <저장소> <브랜치>` ex) git push origin main

