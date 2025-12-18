# Git 사용법

- 분산 버전 관리 프로그램

## 로컬 저장소

![git 저장소](https://www.notion.so/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Ff2678325-6f7b-4a25-b188-86c42030d6d5%2F7142d992-3d01-481c-9d4e-e818c6e185d8%2FUntitled.png%3FspaceId%3Df2678325-6f7b-4a25-b188-86c42030d6d5?table=block&id=2cb611ac-3a00-806f-9790-d13a0ade2843&cache=v2)

- `Working Directory`  : 사용자의 일반적인 작업 공간
- `Staging Area`  : 커밋을 위한 작업물이 추가되는 공간
- `Repository`  : Staging area에 있는 작업물의 변경사항을 저장하는 곳

## Git 명령어

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

## Github
+ .gitignore
  + 특정 파일 폴더를 Git이 버전 관리를 하지못하도록 지정하는 방법
  + [.gitignore 파일 생성](https://www.toptal.com/developers/gitignore/)

+ branch 
  - main에서 벗어나 독립적으로 작업할 수 있는 공간
  - 장점
    - 원본(main)에 대한 안정성
    - 동시에 작업이 가능하여 체계적인 개발 가능
    - 빠른 속도와 적은 용량
+ merge
  + 나뉘어진 브랜치들을 다시 병합
  - Merge 종류
      1. Fast-Forward
      2. 3-Way Merge
      3. Merge Conflict
    
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
- git clone URL
    - 원격 저장소 자체를 복제
    - git init 되어 있지 않은 곳으로 복제
- git pull origin main
    - 원격 저장소의 변경 사항을 로컬에 동기화 
  
- git branch / -r
    - 브랜치 목록 확인(git/github)
  
- git branch <브랜치 이름> <커밋 ID>
- git switch -r <브랜치 이름> <커밋 ID>
    - 커밋 위치에 브랜치 생성

- git branch -d/D <브랜치 이름>
    - d는 병합된 브랜치(삭제 되어도 상관없은)만 삭제 가능
    - D는 강제 삭제

- git switch <다른 브랜치 이름> <커밋 ID>
    - 특정 브랜치로 이동

- git merge <합칠 브랜치 이름>
    - 메인이 될 브랜치로 이동 후 합칠 브랜치를 입력

### Workflow

+ 원격 저장소 소유권이 있는 경우
    1. local 저장소로 clone
    2. 새로운 branch 생성하여 작업
    3. 원격 저장소로 push → Pull Request
    4. 코드 리뷰 후 병합 진행(문제 있을시 반려)
    5. local 저장소 branch main으로 복귀
    6. 원격 저장소로 부터 pull
    7. 생성했던 branch 삭제  

+  원격 저장소 소유권이 없는 경우
    1. 원격 저장소(진)에서 나의 원격 저장소로 fork
    2. local 저장소로 clone
    3. 새로운 branch 생성하여 작업
    4. 나의 원격 저장소로 push → 원격 저장소(진) 에게 Pull Request
    
    이후 과정 동일