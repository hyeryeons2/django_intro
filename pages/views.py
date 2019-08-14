from django.shortcuts import render
from datetime import datetime
import random

# Create your views here.
# ★☆★☆중요☆★☆★
# view 함수 실행하면서 사용자는 url을 로그인 페이지를 볼 수 있음(mapping한다)
# 즉 url과 view 함수가 연동됨
# 예) login url -> views.py의 login 함수 실행 -> 페이지 보여줌
# 작업들이 실제로 일어나는 함수들 정의하는 곳

# 사용자에게 어떤 페이지를 보여줄 지 view 함수를 선언해준다.
# 요청이 들어오면 index.html을 찾아서 보여준다(어디서? pages>templates>에서 찾음)
def index(request):         # 첫 인자는 반드시 request -> 사용자가 보내는 요청에 대한 정보
    return render(request, 'index.html')  # render의 첫 인자도 반드시 request(위에서 받은 request), 페이지 이름


def introduce(request):
    return render(request, 'introduce.html')


# template variable example
# Variable routin'으로 'name' 을 받아서 context에 'name' 도 함께 넣는다.
# dinner.html에서 'name' 님의 저녁식사는 'pick' 입니다로 출력하기   
def dinner(request, name):
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)  # dinner라고 동일한 이름으로 함수를 지정하는 경우, name space없음
    context = {
        'pick': pick,
        'name': name,
    }
    # Django template로 context를 보낸다(전달)
    return render(request, 'dinner.html', context)


def image(request):
    image_url = 'https://picsum.photos/700'
    context = {
        'image_url': image_url,
    }
    return render(request, 'image.html', context)

# greeting/name/으로 됨
def greeting(request, name):  # url에서 받은 다양한 변수 받는 것 request 뒤에 name
    context = {
        'name': name,
    }
    return render(request, 'greeting.html', context)


def times(request, num1, num2):
    result = num1 * num2
    context = {
        'result': result,
        'num1': num1,
        'num2': num2,
    }
    return render(request, 'times.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'template_language.html', context)


def info(request):
    return render(request, 'info.html')


def student(request, name):
    age = 28
    context = {
        'name': name,
        'age': age,
    }

    return render(request, 'student.html', context)