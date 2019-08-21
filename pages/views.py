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
    return render(request, 'pages/index.html')  # render의 첫 인자도 반드시 request(위에서 받은 request), 페이지 이름


def introduce(request):
    return render(request, 'pages/introduce.html')


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
    return render(request, 'pages/dinner.html', context)


def image(request):
    image_url = 'https://picsum.photos/700'
    context = {
        'image_url': image_url,
    }
    return render(request, 'pages/image.html', context)

# greeting/name/으로 됨
def greeting(request, name):  # url에서 받은 다양한 변수 받는 것 request 뒤에 name
    context = {
        'name': name,
    }
    return render(request, 'pages/greeting.html', context)


def times(request, num1, num2):
    result = num1 * num2
    context = {
        'result': result,
        'num1': num1,
        'num2': num2,
    }
    return render(request, 'pages/times.html', context)


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
    return render(request, 'pages/template_language.html', context)


def info(request):
    return render(request, 'pages/info.html')


def student(request, name):
    age = 28
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'pages/student.html', context)


def b_day(request):
    # tday = datetime.now()
    # if tday.month == 10 and today.day == 15:
    #     result = '예'
    # else:
    #     result = '노' 

    # context = {
    #     'result': result,
    # }
    # return render(request, 'b_day.html', context)
    return render(request, 'pages/b_day.html')


def lotto(request):
    real_lotto = [21, 25, 30, 32, 40, 42]
    lotto = sorted(random.sample(range(1, 45), 6))
    context = {
        'real_lotto': real_lotto,
        'lotto': lotto,
    }
    return render(request, 'pages/lotto.html', context)


def search(request):
    return render(request, 'pages/search.html')


def result(request):
    # request.GET.get을 쓰는 이유? 예를 들어 회원가입의 경우, 이름, 성별, 나이 등 여러가지 정보가
    # 입력되는데 이름, 성별, 나이 등 각각의 항목을 각각 처리하고자 사용하는 방식
    # <QueryDict: {'query': ['안녕!']}>
    query = request.GET.get('query')  # get을 할 때에는 페이지 두개 쓸 때 필요한거
    category = request.GET.get('category')
    context = {
        'query': query,
        'category': category,
    }
    return render(request, 'pages/result.html', context)


def lotto_pick(request):  # html 파일에서 input 값(form)에서 받겠다.
    return render(request, 'pages/lotto_pick.html')


def lotto_result(request):
    pick_lotto = request.GET.get('pick_lotto')  # lotto_pick에서 받은 번호를 가져온다
    pick_lotto = list(map(int, pick_lotto.split()))  # 받은 번호를 스플릿해서 list로 만든다

    result_lotto = [21, 25, 30, 32, 40, 42]  
    context = {
        'pick_lotto': pick_lotto,
        'result_lotto': result_lotto,
    }
    return render(request, 'pages/lotto_result.html', context)


def static_example(request):
    return render(request, 'pages/static_example.html')


def num_push(request):
    return render(request, 'pages/num_push.html')


def pull(request):
    num = request.GET.get('num')
    context = {
        'num': num,
    }
    return render(request, 'pages/pull.html', context)
