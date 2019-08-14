from django.shortcuts import render
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
def dinner(request):
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)  # dinner라고 동일한 이름으로 함수를 지정하는 경우, name space없음
    context = {
        'pick': pick,
    }
    # Django template로 context를 보낸다(전달)
    return render(request, 'dinner.html', context)
