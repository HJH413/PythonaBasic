# [추가] 함수도 객체이다
def case1():
    print('case-1')


def case2():
    print('case-2')


def case3():
    print('case-3')


f = {'a1': case1, 'a2': case2, 'a3': case3}  # 함수도 객체다
print(f['a1'])

f['a2']()  # 함수 호출

byensu = 'a3'
print(f[byensu])
f[byensu]()


# ---------------------------------------
# 글로벌 변수와 지역변수
# temp = '글로벌'
# def func():
#     print("1>",temp)
#
# func()
# print("2>",temp)

# temp = '글로벌'
# def func():
#     print("0>", temp)
#     temp = '지역'
#     print("1>", temp)
#
# func()
# print("2>", temp)

def func():  # 지역 변수는 지역 안에서 만 사용 가능하다.
    global temp
    temp = '지역'
    print("1>", temp)


func()
print("2>", temp)

'''
#----------------------------------------------
# 람다함수 - 한번 사용하고 버리는 함수
# 파이션에서는 람다함수를 한 줄로 작성???

    파이썬 3.x부터는 람다를 권장하지 않는다고.
    몇몇 개발자들이 람다함수 사용시 직관적이지 않다는 이유라는데
    
    종종 사용됨
'''


# 일반함수
def f(x, y):
    return x + y


print(f(3, 2))

# lambda;
f = lambda x, y: x + y
print(f(3, 2))

# -----------------------------------------------------------
"""  맵리듀스
    (1) map()
         ` 연속 데이터를 저장하는 시퀀스 자료형에서 요소마다 같은 기능을 적용할 때 사용
         ` 형식 : map(함수명, 리스트형식의 입력값)
         ` 파이썬 3.x에서는 list(map(calc, ex)) 반드시 list를 붙여야 리스트 형식으로 반환된다
           파이썬 2.x에서는 list 없이도 리스트 형식으로 반환
    (2) reduce()
         ` 리스트 같은 시퀀스 자료형에 차례대로 함수를 적용하여 모든 값을 통합하는 함수    
    
    파이썬 2.x에서는 많이 사용하던 함수이지만, 최근 문법의 복잡성으로 권장하지 않는 추세란다.
"""


def calc(x):
    return x * 2


data = [1, 2, 3, 4, 5]
result = list(map(calc, data))
print(result)

result = []
for i in data:
    result.append(calc(i))

print(result)

from functools import reduce


def f(x, y):
    return x + y


data = [1, 2, 3, 4, 5]

print(reduce(f, data))


# 6. 다음 코드의 실행 결과를 쓰시오.
def rain(colors):
    colors.append("purple")
    colors = ["green", "blue"]
    return colors


rainbow = ["red", "orange"]
print(rain(rainbow))  # r o g b p # 답이 g b 인 이유는 함수 내에서 지역 변수로 컬러값을 리턴해서 그럼


# 7. 다음 코드의 실행 결과를 쓰시오.
def function(value):
    print(value ** 3)


print(function(2))  # 8


# 8. 다음 코드의 실행 결과를 쓰시오.
def get_apple(fruit):
    fruit = list(fruit)
    fruit.append("e")
    fruit = ["apple"]
    return fruit


fruit = "appl"

get_apple(fruit)  # 함수 안에서 print가 없으므로 정상적으로 출력을 할러면 print(get_apple(fruit))
print(fruit)  # appl


# 9. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
def return_sentence(sentence, n):
    sentence += str(n)
    n -= 1
    if n < 0:
        return sentence
    else:
        return (return_sentence(sentence, n))


sentence = "I Love You"
print(return_sentence(sentence, 5))


# 3
# ➀ None ➁ I Love You➂ I Love You543210
# ➃ I Love You54321 ➄ I Love You5

# 10. 다음 코드의 실행 결과를 쓰시오.
def test(x, y):
    tmp = x  # tmp <- x
    x = y  # x <- y
    y = tmp  # y <- x
    return y.append(x)  # xy


x = ["y"]
y = ["x"]
test(x, y)  # y x
print(y)  # x


# 11. 다음 코드를 실행하면 결과값으로 120이 나온다. 빈칸에 들어갈 알맞은 코드를 작성하시오.
def factorial_calculator(n):
    if n in (0, 1):
        return 1
    else:
        return n * factorial_calculator(n-1) # 재귀함수


print(factorial_calculator(5))
