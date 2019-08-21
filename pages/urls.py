# dango.urls에서 path 함수 가져오겠다
from django.urls import path
# 현재 경로(.)에서부터 views를 가져와라
from . import views


urlpatterns = [
    # 기존에 pages에 있던 url 옮겨오기!
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
]