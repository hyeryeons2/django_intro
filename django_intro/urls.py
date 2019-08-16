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
from django.urls import path
from pages import views  # pages라는 app에서 views를 가져온다

# www.ssafy.com/admin/ 쳤을 때 들어오면 성공함(admin이 생성되어 있기 때문에)
# www.ssafy.com/login/ 쳤을 때, login 페이지가 없기 때문에 페이지가 뜨지 않음
# 따라서 urlpatterns에서 path('admin/', admin.site.urls)를 추가하면 login 쳤을 때 login 페이지로 이동
urlpatterns = [
    # 사용자가 접속하는 경로
    path('num/pull/', views.pull),
    path('num/push/', views.num_push),

    path('static_example', views.static_example),

    path('lotto_result/', views.lotto_result),
    path('lotto_pick/', views.lotto_pick),
    
    path('result/', views.result),
    path('search/', views.search),

    path('lotto/', views.lotto),
    path('isit_b_day/', views.b_day),
    path('student/<str:name>', views.student),
    path('info/', views.info),
    path('template_language/', views.template_language),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('greeting/<str:name>/', views.greeting),  # <> 안의 변수를 다양한 사람으로 지정해 인사받는 페이지
    path('dinner/<str:name>/', views.dinner),  # 저녁메뉴 하나 추천받는 페이지
    path('index/', views.index),  # 경로 적는 순서도 중요함(위->아래)
    path('introduce/', views.introduce),
    path('image/', views.image),
    path('admin/', admin.site.urls),
]
