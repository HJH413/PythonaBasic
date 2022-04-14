"""
    @ 컴프리핸션 (comprehension)
    ` 하나 이상의 이터레이터로부터 파이썬 자료구조를 만드는 컴팩트한 방법
    ` 비교적 간단한 구문으로 반복문과 조건 테스트를 결합

    * 리스트 컨프리핸션
        [ 표현식 for 항목 in 순회가능객체 ]
        [ 표현식 for 항목 in 순회가능객체 if 조건 ]

    * 딕셔러리 컨프리핸션
        { 키_표현식: 값_표현식 for 표현식 in 순회가능객체 }

    * 셋 컨프리핸션
        { 표현식 for 표현식 in 순회가능객체 }

"""


# 컨프리핸션 사용하지 않은 리스트 생성
alist = []
alist.append(1)
alist.append(2)
alist.append(3)
alist.append(4)
alist.append(5)
alist.append(6)
print(alist)

alist = []
for n in range(1,7):
    alist.append(n)
print(alist)

alist = list(range(1,7))
print(alist)

print("---"*10)
#------------------------------------------------
# 리스트 컨프리핸션
blist = [n for n in range(1, 7)]
print(blist)

#연산이 가능하다
blist = [n*2 for n in range(1, 7)]
print(blist)

#조건문도 가능하다
blist = [n*2 for n in range(1, 7) if n%2 ==0]
print(blist)

clist = []
for r in range(1, 4):
    for c in range(1, 3):
        clist.append((r,c))
print(clist)

# dlist = [r for r in range(1, 4) for c in range(1, 3) dlist.append((r,c))]
dlist = [(r, c) for r in range(1, 4) for c in range(1, 3)]
print(dlist)

#-------------------------------------------
# 딕셔러니 컨프리핸션
data = ( 2, 3, 4)
adic = { n: n**2 for n in data}
print(adic)

word = 'LOVE LOL'
wcnt = { letter: word.count(letter) for letter in set(word)} # 단어의 갯수를 구할 때 # set은 인덱스를 저장하지 않음
print(wcnt)

#------------------------------------------------
# 셋 컨프리핸션
data = (1,2,3,1,1,2)
alist = [n for n in data]
print(alist)

bset = {n for n in data}
print(bset)


# -------------------------------------------------
# [참고] 제너레이터 컨프리핸션
# ( ) 를 사용하면 튜플이라 생각하지만 튜플은 컨프리핸션이 없다.













우리의결의= """취하고싶으면달려라
             맡은업무는반드시마치자
             노력없는성과는없다
             구글신과함께공부하자"""

result = [ j[i*2] for i, j in enumerate(우리의결의.splitlines())]
print(result)

#1
mylist = ['apple' ,'banana', 'grape']
result = list(enumerate(mylist))
print(result)
#[(0, 'apple'), (1, 'banana'), (2, 'grape')]


#2
#           0   1   2   3    4     5  6  7   8
cat_song = "my cat has blue eyes, my cat is cute"
print({i:j for j,i in enumerate(cat_song.split())}) # 잘 모르겠담
# j 0, i word # 3? 왜 my cat 은 5하고 6인가? 답은4번
#{'my': 5, 'cat': 6, 'has': 2, 'blue': 3, 'eyes,': 4, 'is': 7, 'cute': 8}

#3
colors = ['orange', 'pink', 'brown', 'black', 'white']
result = '&'.join(colors) # 배열을 연결시켜준다는 의미?
print(result)
#orange&pink&brown&black&white

#4
user_dict = {}
user_list = ["students","superuser", "professor", "employee"]
for value_1, value_2 in enumerate(user_list):
    user_dict[value_2] = value_1
print(user_dict)
# [(students, 0),(superuser, 1),(professor, 2),(employee, 3)]
# {'students': 0, 'superuser': 1, 'professor': 2, 'employee': 3}  정답 딕셔너리니까 이렇게 생성해야함

#6
animal = ['Fox', 'Dog', 'Cat', 'Monkey', 'Horse', 'Panda', 'Owl']
print([ani for ani in animal if 'o' not in ani])
# cat,panda,Owl

#7
name = "Hanbit University"
student = ["Hong", "Gil", "Dong"]
split_name = name.split() #['Hanbit', 'University']
join_student = ''.join(student) # Hong Gil Dong
print(join_student[-4:] + split_name[1])
#Hong Gil University -4: 는 뒤에서 -4번째글자부터 마지막까지 값을 가져와라
#Dong University

#8
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2' ,'b3']

#for a, b in (alist, blist): #배열이 묶여있지 않아서 zip을 추가하여 묶어줘야함
for a, b in zip(alist, blist):
    print(a, b)

#9
a = [1, 2, 3]
b = [4, 5, ]
c = [7, 8, 9]
print([[sum(k), len(k)] for k in zip(a, b, c)])
# 정답 [[12, 3], [15, 3]]  이유 b list에는 2번째 인덱스가 없어서

#10
week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
list_data = [week, rainbow]
print(list_data[1][2]) # 1번째인덱스 안에있는 2번째 인덱스를 선택하라
#yellow

#11
kor_score = [30, 79, 20, 100, 80]
math_score = [43, 59, 0, 30, 90]
eng_score = [49, 72, 48, 67, 15]
midterm_score = [kor_score, math_score, eng_score]
print ("score:",midterm_score[2][1])
#72

#12
# alist = ["a", "b", "c"]
# blist = ["1", "2", "3"]
# abcd= []
# for a, b in enumerate(zip(alist, blist)): # a 1
#     try:
#         abcd.append(b[a])
#     except IndexError:
#         abcd.append("error")
#
# print(abcd)
#13
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
nums = [i for i in range(20)]
answer = [alpha+str(num) for alpha in alphabet for num in nums if num%2==0]
print(len(answer))
#4?
# -------------------------------------------------
# 프로젝트할 때 팀구호
#우리의결의= """취하고싶으면달려라
#맡은업무는반드시마치자
#노력없는성과는없다
#구글신과함께공부하자
#"""
#result = [ j[i*2] for i, j in enumerate(우리의결의.split('\n')]
#print(result)