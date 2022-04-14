"""
    [ 함수 ]

     - 반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다
     - 역할별 구문을 작성한다

     def 함수명(매개변수):
        수행할 문장들
"""


# 1. 인자도 없고 리턴값도 없는 함수
def func():
    print("inside func")


result = func()
print("result =", result)  # 리턴값이 없으면 None


def func():
    print("inside func")
    return 'hello'


result = func()
print("result =", result)  # 리턴값을 받와서 출력


# 2 리턴값이 여러개인 경우
def func(arg):
    return arg + 5, arg - 5


add, minus = func(10)
print("add =", add)
print("minus =", minus)


# (3) 위치 인자 ( positional argument )
def func(greeting, name):
    print(greeting, '!!!!!!', name, '님')


func("안녕하세여", "홍길동")
func("마이클", "하이")

# (4) 키워드 인자 (keyword qrgumnet)
func(name="마이클2", greeting="하이2")


# 매개변수 지정 (기본값 지정)
def func(greeting, name="아무개"):
    print(greeting, '!!!!!!', name, '님')


func("안녕", "홍길동")
func("올라")


# 참고
def func(a, b, c=100):
    return a * 2 + b * 3 + c * 4


print(func(c=1, b=2, a=3))  # 16
print(func(1, 2, 3))  # 20
print(func(1, 2))  # 408

'''
#----------------------------------------------------------------
# (5) 위치 인자 모으기 (*)

첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?

'''


def func(a, b, c=0, *args):  # 받는 변수 위치 인자 뭐시기...
    sum = a + b + c
    for i in args:
        sum += i
    return sum


print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))  # args에 7,8,9가 튜플로 들어간다


# 6 키워드 인자 모으기

def func(a, b, c=0, *args, **kwargs):  # 받는 변수 위치 인자 뭐시기...
    sum = a + b + c
    for i in args:
        sum += i  # 튜플 값 불러와서 더하기
    for j in kwargs:
        sum += kwargs[j]  # dictionary 로 키워드로 들어간 값을 불러와서 더하기
    return sum


print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))
print(func(4, 5, 6, 7, kor=80, eng=70))
print(func(4, 5, 6, 7, kor=80, eng=70, java=60))


# [ 4. 함수 ]

# 1. 다음 코드의 실행 결과를 쓰시오.
def test(t):
    t = 20
    print("In Function:", t)  # In Function: 20


x = 10
print("Before:", x)  # Before: 10
test(x)
print("After:", x)  # After : 20 #  정답 After : 10 x의 10의 값을


# 2. 다음 코드의 실행 결과를 쓰시오.
def sotring_function(list_value):
    return list_value.sort()  # sort함수는 return 값이 없어서


print(sotring_function([5, 4, 3, 2, 1]))  # 1 2 3 4 5


# 3. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
def is_yes(your_answer):
    if your_answer.upper() == "YES" or your_answer.upper() == "Y":
        result = your_answer.lower()


print(is_yes("Yes"))


# 1?


# ➀ Error ➁ 'Yes' ➂ None ➃ 'yes' ➄ 'YES'


# 4. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
def add_and_mul(a, b, c):
    return b + a * c + b


print(add_and_mul(3, 4, 5) == 63)


# ➀ 63 ➁ 2.39 ➂ True ➃ False ➄ 5.23
# 4

# 5. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
def args_test_3(one, two, *args, three):
    print(one + two + sum(args))
    print(args)


args_test_3(3, 4, 5, 6, 7)
# 1


# ➀ 25 (5, 6, 7) ➁ 20 (6, 7)➂ TypeError➃ 25 (6, 7) ➄ 20 (5, 6, 7)
