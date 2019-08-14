# Django Setting

## 가상환경

- 프로젝트 하나당 가상환경 하나씩 
- why? 프로젝트마다 사용하는 라이브러리와 버전이 다르기 때문에(호환성) 가상환경을 별개로 지정해야 함

```bash
# student@M702 MINGW64 ~/development/django/django_intro 에서 작업(작업폴더경로 확인)

# 파이썬 버전 확인(반드시 3.7x 버전이 맞는지 확인 후 진행)
$ python -V
Python 3.7.4

# 가상환경 생성
$ python -m venv <가상환경 설치경로>
$ python -m venv venv 

# 가상환경 적용
$ source venv/Scripts/activate

# 다시 한 번 버전 확인
(venv)  # <= 가상환경 적용 시 git bash에서 해당 환경 이름이 표시됨
$ python -V
Python 3.7.4

# 설치된 모듈 확인
(venv)
$ pip list
Package    Version
---------- -------
pip        19.0.3
setuptools 40.8.0 

# pip upgrade
(venv)
python -m pip install --upgrade pip

# pip upgrade 확인
(venv)
$ pip list
Package    Version
---------- -------
pip        19.2.2
setuptools 40.8.0


```





----



## VS Code 및 기타 settings

### VS Code 파이썬 환경 선택

- vs Code Extensions 에서 `python`과 `Django` 설치

- `Ctrl + shift + p` -> `python select interpreter` -> 방금 생성한 가상환경 선택(`.\venv\Scripts\python.exe`)
  - `.vscode/settings.json` 파일이 생성되며 터미널에서 자동으로 가상환경이 적용된다면 OK.

### Git ignore setting

- `gitignore.io` 에 접속해 `python, django, windows, visualstudiocode` 선택 후 생성
- `.gitignore` 파일 생성 후(`$ touch .gitignore`) 붙여넣기 

### VS Code Django 환경 setting

```json
{
    // '//'는 주석입니다:)

    // 파이썬 환경 선택 => 자동으로 입력됨
    "python.pythonPath": "venv\\Scripts\\python.exe", 

    // Django 에서 사용되는 파일 타입에 대한 정의
    "files.associations": {
        "**/templates/*.html": "django-html",
        "**/templates/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },

    // Django-html 에서도 일반 html emmet을 적용
    // h1, ! tab 등 일반 html에서 사용하는 것들을 emmet 설정을 통해 django에서 사용 가능
    "emmet.includeLanguages": {"django-html": "html"},

    // Django-html 에서 tab size 2칸으로 고정
    "[django-html]": {
        "editor.tabSize": 2
    }, 
}
```



---



## Start Django Project

```bash
(venv)
$ pip install django
```

- `django`를 설치한 순간부터 `djang-admin` 이라는 `command` 를 사용할 수 있게 됨
- 이 `command` 를 통해 `django project` 에 여러가지 명령을 할 수 있음



`Start Project`

```bash
(venv)
$ django-admin startproject django_intro .  
# 띄어쓰기 주의 (intro 띄고 .)
# django_intro와 manage.py 가 생성됨 

```

- 현재 디렉토리에서 `django_intro`라는 이름으로 프로젝트 시작

- `Django project naming`

  - `-` 캐릭터는 사용될 수 없다

  - `python`과 `django`에서 이미 사용되는 이름은 사용하지 않는다.

    (`django` 라는 이름은 `django` 그 자체와 충돌이 발생하며, `test`라는 이름도 `django` 내부적으로 사용하는 모듈 이름)

    

`Runserver`

```bash
$ python manage.py runserver
# 링크로 이동하면 django 시작됨
```

- `ctrl + c` 로 끌 수 있음
- 기본적으로 `localhost:8000`에서 실행됨



`application` 폴더 만들기

```bash
$ python manage.py startapp pages
# starpapp <app 이름>
```

