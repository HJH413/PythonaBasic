"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록{}을 대신 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생
        print(b)  =>  if 안에 있는 문장
    print(b)  => if 밖에 있는 문장

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
i = 0;
i2=0.0
i3=""
i4=str()
i5=list()
i6=tuple()
i7=set()
i8=dict()
i9={}
i10=None

a = -1 # -1을 가리키는 객체 a를 만들라!

if a:
    print("True1") #True
else:
    print("False1")

if not a:
    print("True2")
else:
    print("False2") # False


a = 10;
b = -1;

if a and b:
    print("True3") #
else:
    print("False3")
if a or b:
    print("True4") #
else:
    print("False4")

print(a and b) # True -1 결론이 나고자 하는 값으로 결과를 리턴해 해줌  그래서 -1  and는 두 개의 값이 True  그래서 and 의 뒤에 있는 b를 확인하고서 값을 출력함  만약에 a가 false라면 바로 a를 출력함
print(a or b) # True 10

#-----------------------------------------------
a=0
if a:
    print('A')
print('B')
print('C')

#-----------------------------------------------
a=10
b=-1

if a:
    c=2
elif b:
    c=4
else:
    c=6
print(c)#2





