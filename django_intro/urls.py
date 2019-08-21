"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 작업할 파일 2

# 사용자가 들어오는 경로 지정(사용자가 접속하는 경로)
from django.contrib import admin
from django.urls import path, include  # include 함수 포함시키겠다
# from pages import views  # pages라는 app에서 views를 가져온다

# www.ssafy.com/admin/ 쳤을 때 들어오면 성공함(admin이 생성되어 있기 때문에)
# www.ssafy.com/login/ 쳤을 때, login 페이지가 없기 때문에 페이지가 뜨지 않음
# 따라서 urlpatterns에서 path('admin/', admin.site.urls)를 추가하면 login 쳤을 때 login 페이지로 이동
urlpatterns = [
    # path(사용자가 접속하는 경로)
    # 최초 어플리케이션 파일 만들었을 때, 한번만 선언해주면된다
    path('utilities/', include('utilities.urls')),
    path('pages/', include('pages.urls')),  # pages로 온다면 include 함수를 통해 pages에 있는 urls 파일로 보내줘!
    path('admin/', admin.site.urls),
]
