
# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

"""
a = 112                  # 숫자형
b = ['1','2','3']       # 리스트
c = '987'                # 문자열
d = tuple(b)             # 튜플
e = dict(k=5, j=6)       # 딕셔너리 print(entry, ':', e[entry])

for entry in e: # a는 반복이 안되지만 b부터 e까지는 반복된다.
    print(entry, ':', e[entry])

for k, v in e.items(): # a는 반복이 안되지만 b부터 e까지는 반복된다.
    print(k,':',v)

#----------------------------------------------------
a = ['z', 'y', 'x']

while a:
    data = a.pop()
    print(data)
else:
    print("끝")

"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
for x in range(2, 10):
    print("{}단".format(x))
    for y in range(1,10):
        #print(x, '*', y, '=', x*y)
        print('{0} * {1} = {2}'.format(x, y, x*y))
    else:
        print('--'*10)

#1
fruit = 'apple'
if fruit == 'Apple':
    fruit = 'Apple'
elif fruit == 'fruit':
    fruit = 'fruit'
else:
    fruit = fruit
print(fruit) # fruit #정답은 apple 마지막 else에서 문자 fruit 아니라 변수 fruit = 'apple' 을 저장하는 것
#2
number = ["1", 2, 3, float(4), str(5)]
if number[4] == 5: # number[4] 는 문자열 5  == 5 는 숫자형 false
    print(type(number[0]))
elif number[3] == 4: # 숫자형4는 실수형 4.0 이니까 그래서 true?
    print(number[2:-1]) # 인덱스2부터 맨 뒤에서 부터 -1전까지  3, 4.0
    # 3, 4.0

#3
num = 0
i = 1
while i < 8: # 1 2 3 4 5 6 7
    if i % 3 == 0: # i를 3으로 나머지 연산했을때 남은 값이 0이라면
        break # 멈춰라
    i += 1 # 1 +=1 , 2 +=1
    num += i # 2, 3
print(num) # 답은 5

#4
result = 0
for i in range(5, -5, -2): # [5, 3, 1, -1, -3]
    if i < -3:
        result += 1
    else:
        result -= 1
print(result) # -5

#5
num = ""
for i in range(10): # 0~9
    if i <= 5 and (i % 2)==0: # 2 4
        continue
    elif i is 7 or i is 10: # 7,10
        continue
    else:
        num = str(i) + num
print(num) # 9 8 6 5 3 1

#6
coupon = 0
money = 20000
coffee = 3500
while money > coffee: # 20000 > 3500
    if coupon < 4: # 0 1 2 3
        money = money - coffee # 16500 13000 9500 6000 8800 5300 1800
        coupon += 1 #               1   2    3    4    0     1    2
    else:
        money += 2800 # 8800 쿠폰 0
        coupon = 0
print(money) #1800
print(coupon) #2
#7
list_data_a = [1, 2]
list_data_b = [3, 4]
for i in list_data_a:
    for j in list_data_b:
        result = i + j

print(result)

#➀ 20 ➁ 6 ➂ [13, 14, 23, 24] ➃ [4, 5, 5, 6] ➄ Error