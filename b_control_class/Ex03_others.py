msg = '행복해'            # 문자열
li = ['a','b','c']       # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = {'k': 5, 'j': 6, 'l':7 }    # 딕셔너리

# (1) unpacking : 요소분해
c1, c2, c3 = di.items() # li, tpl, di
print(c1)
print(c2)
print(c3)

alist = [(1, 2), (3, 4), (5, 6)]

# a1, a2, a3 = alist
# print("{}+{}={}".format(a1[0],a1[1],a1[0]+a1[1]))

# 출력 양식 : 1 + 2 = 3
# for i in range(len(alist)):
#     print(alist[i][0], "+", alist[i][1], "=", alist[i][0]+alist[i][1])

for i, j in alist:
    print("{}+{}={}".format(i, j, i+j))

# (2) enumerate() 함수 : 각 요소에 인덱스를 붙여주는 함수
user_list = ['개발자','코더','프로그래머','분석가']

for value in user_list:
    print(value)

for value in enumerate(user_list):
    print(value)

for idx, value in enumerate(user_list): # enumerate로 인덱스를 붙히고서 요소로 분해하는 과정
    print(idx, ":", value)

# (3) zip() #리스트를 묶는 것
days = ['월', '화', '수']
doit = ['잠자기', '놀기', '밥먹기', '공부']

print(zip(days, doit))
print(list(zip(days, doit)))
print(dict(zip(days, doit)))

for d, h in zip(days, doit):
    print(d, '요일에 할일 : ', h)
