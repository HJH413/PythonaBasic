"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""
# name = input('이름을 입력하세요 : ')
# print('당신의 이름은', name, '입니다.')
# format()이용
# msg = '이름을 입력하세요:'
# print('당신의 이름은 {name} 입니다.'.format(name=name))
# % 이용
# ('당신의 이름은 %s 입니다.' %(name))

# -------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력 -> eval() 이용
# age = input('나이를 입력하세요. : ')
# print('당신의 나이는', eval(age)+1, '입니다.')
# print('당신의 나이는 {age} 입니다.'.format(age=eval(age)+1))
# print('당신의 나이는 %d 입니다.' %(eval(age)+1))

# height = input('키를 입력하세요. : ')
# print('당신의 키는', eval(height), 'cm 입니다.')
# -----------------------------------------
# print() 함수
print('1+2')
print(eval('1+2'))

# ,를 쓰면 구분자의 형식으로 한칸씩 공백을 줌
print("친구" + '안녕')
print("친구", '안녕')
print("친구"  '안녕')

# for i in range(1, 5, 2):
#     print(i)
#
# for i in range(5):
#     print(i, end=',' if i < 4 else '')
# ----------------------------------
# 단을 입력받아 구구단을 구하기
inputNum = input("구구단 숫자를 입력하세요. : ")
print("-------", int(inputNum), '단', "-------")
for i in range(1, 10):
    print(int(inputNum), '*', i, '=', int(inputNum) * i)

# 정수 5개를 입력받아 평균 구하기
# inputInt1 = input("숫자를 입력하세요.")
# inputInt2 = input("숫자를 입력하세요.")
# print((int(inputInt1)+int(inputInt2))/2)
sum = 0

for x in range(5):
    inputInt = input("숫자를 입력하세요.")
    sum += int(inputInt)
print(sum / 5)

# 2. 사용자에게서 받은 문자들을 역순으로 출력한다.

inputText = input("글자를 입력하세요.")
print(inputText[::-1])

# 3. 사용자에게서 받은 정수들의 평균과 표준편차를 계산하여 출력한다.
# 평균과 표준편차를 프로그램을 작성하세요.
lst = input('정수리스트입력: ').strip().split()
lst = [int(i) for i in lst]
avg = sum(lst)/len(lst)
devi = [(i-avg)**2 for i in lst]
print('평균=%.1f' % avg)
print('표준편차 %.2f' % (sum(devi)/len(devi))**0.5)

#4. 전화 키패드에는 각 숫자키마다 3개의 문자가 적혀있다. 사용자가 입력한 문자열을 전화기의 숫자키로 변환하는 프로그램을 작성해보자.
str = input('문자열을 입력하시오:').upper()               #입력값 받아오기
for i in range(len(str)):
    if str[i] in ('A' , 'B' , 'C'):
        print(2,end='')
    elif str[i] in ('D' , 'E' , 'F'):
        print(3,end='')
    elif str[i] in ('G' , 'H' , 'I'):
        print(4,end='')
    elif str[i] in('J' , 'K' , 'L'):
        print(5,end='')
    elif str[i] in('M' , 'N' , 'O'):
        print(6,end='')
    elif str[i] in('P' , 'Q' , 'R' , 'S'):
        print(7,end='')
    elif str[i] in('T' , 'U' , 'V'):
        print(8,end='')
    else:
        print(9,end='')

# -------------------------------------------------------
inputstr = input("문자열을 입력하시오")
phone = {'2' : ['A','B','C'], '3' : ['D','E','F'], '4' : ['G','H','I'],
         '5' : ['J','K','L'],'6':['M','N','O'],'7':['P','Q','R','S'],
         '8' : ['T','U','V'],'9':['W','X','Y','Z']}
#print(phone.items())
for i in range(len(inputstr)):
    for key, value in phone.items():
        if inputstr[i] in value:
            print(key,end='')

# -------------------------------------------------------

# 1
from string import ascii_uppercase
alphabet_list = list(ascii_uppercase)   # 대문자 알파벳 리스트
num_pad = {}
num = 2
# 키:알파벳, 값:숫자 딕셔너리 생성
for a in alphabet_list:
    num_pad[a] = num
    if a in ['C', 'F', 'I', 'L', 'O', 'S', 'V']:    # 다음 숫자로 가는 기준
        num += 1
input_text = input("문자열을 입력하시오: ").upper()

# 문자를 키로 검색
for t in input_text:
    print(num_pad.get(t), end='')
# -------------------------------------------------------
# 2
# 키:숫자, 값:문자리스트 리스트 생성
alphabet_list = [[], [],
                 ['A', 'B', 'C'],
                 ['D', 'E', 'F'],
                 ['G', 'H', 'I'],
                 ['J', 'K', 'L'],
                 ['M', 'N', 'O'],
                 ['P', 'Q', 'R', 'S'],
                 ['T', 'U', 'V'],
                 ['W', 'X', 'Y', 'Z']
                 ]

input_text = input("문자열을 입력하시오: ").upper()
# 글자별 리스트 포함 확인
for t in input_text:
    for i, a in enumerate(alphabet_list):
        if t in a:
            print(i, end='')
            break;
# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3
