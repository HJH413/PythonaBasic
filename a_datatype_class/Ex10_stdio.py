"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""
# name = input('이름을 입력하세요 : ')
# print('당신의 이름은', name, '입니다.')
#format()이용
# msg = '이름을 입력하세요:'
# print('당신의 이름은 {name} 입니다.'.format(name=name))
# % 이용
#('당신의 이름은 %s 입니다.' %(name))

#-------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력 -> eval() 이용
# age = input('나이를 입력하세요. : ')
# print('당신의 나이는', eval(age)+1, '입니다.')
# print('당신의 나이는 {age} 입니다.'.format(age=eval(age)+1))
# print('당신의 나이는 %d 입니다.' %(eval(age)+1))

# height = input('키를 입력하세요. : ')
# print('당신의 키는', eval(height), 'cm 입니다.')
#-----------------------------------------
# print() 함수
print('1+2')
print(eval('1+2'))

# ,를 쓰면 구분자의 형식으로 한칸씩 공백을 줌
print("친구" + '안녕')
print("친구" , '안녕')
print("친구"  '안녕')

# for i in range(1, 5, 2):
#     print(i)
#
# for i in range(5):
#     print(i, end=',' if i < 4 else '')
#----------------------------------
# 단을 입력받아 구구단을 구하기
inputNum = input("구구단 숫자를 입력하세요. : ")
print("-------", int(inputNum), '단', "-------")
for i in range(1, 10):
    print(int(inputNum),'*',i,'=',int(inputNum)*i)

#정수 5개를 입력받아 평균 구하기
# inputInt1 = input("숫자를 입력하세요.")
# inputInt2 = input("숫자를 입력하세요.")
# print((int(inputInt1)+int(inputInt2))/2)
sum=0

for x in range(5):
   inputInt = input("숫자를 입력하세요.")
   sum += int(inputInt)
print(sum/5)


# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3
