"""
    파이션  - 무료이지만 강력하다
        ` 만들고자 하는 대부분의 프로그램 가능
        ` 물론, 하드웨어 제어같은 복잡하고 반복 연산이 많은 프로그램은 부적절
        ` 그러나, 다른언어 프로그램을 파이썬에 포함 가능 
        
    [주의] 줄을 맞추지 않으면 실행 안됨

    [실행] Run 메뉴를 클릭하거나 단축키로 shift + ctrl + F10

    [도움말] ctrl + q

"""

""" 
    여러줄 
    주석 
"""
'''
    여러줄 
    주석 
'''
# 한줄 주석

# 문자열표시
print("헬"
      "로우")
print('he'
      'llo')
# 문자열 입력시 """ """ 을 사용 하면 그 안에서 작성한 내용의 공백도 프린트해줌
print("""안


        녕""")
print('''올
라''')
# 실행 : shift + ctrl + F10

'''
변수란
    파이션의 모든 자료형은 객체로 취급한다 (참조형)
    a = 7
            7 객체을 가리키는 변수 a이다. ( 저장한다는 표현 안함 )
            변수 a는 7이라는 정수형 객체를 가리키는 레퍼런스이다.
            여기서 7은 기존 프로그램언어에 말하는 상수가 아닌 하나의 객체이다.
    
    [변수명 규칙]
    - 영문자 + 숫자 + _ 조합
    - 첫글자에 숫자는 안됨
    - 대소문자 구별
    - 길이 제한 없음
    - 예약어 사용 안됨       
    
    [python 의 자료형]
    1. 기본형
        - 숫자형
        - 문자형
        - 논리형 'False', 'None', 'True' 주의 다른언어랑 다르게 첫 글자가 대문자임
        - 날짜형
        
    2. 집합형
        - List
        - set
        - dictionary (자바의 map이랑 비슷함)
        - tuple *** 중요
        
'''

import keyword
print(keyword.kwlist)

a = 777
b = 777
print(id(7))
print(id(a))
print(id(b))
c=8
d=7

if(c==d):
      print("True")
else:
      print("False")
