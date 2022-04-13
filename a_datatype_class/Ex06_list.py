"""
    [ 리스트 ]
      1- 임의의 객체를 순차적으로 저장하는 집합 자료형
      2- 각 값에 대해 인덱스 부여
      3- 변경가능 (**)
      4- 대괄호 [ ] 사용

      [참고]
      배열은 연속적으로 공간을 저장하는 것이니깐 파이션에는 없다
      파이션에서는 리스트를 사용한다
      배열은 생성시 크기를 지정하지만 리스트트 크기 제한이 없다
"""

# --------------------------------------------------------------------
# (1) 리스트 인덱스

arr = []                # 비워져 있는 리스트 생성
arr = list()
arr = [1,2,3,4,5]

""" [출력결과]
    [1, 2, 3, 4, 5, 10]
    [1, 2, 3, 4, 5, 10, 'hello']
    1
    10
    HELLO
    h
"""
arr.append(10)
print(arr)
arr.append('hello')
print(arr)
print(arr[0])
print(arr[5])
print(arr[6].upper())
print(arr[6][0])

# 이중 리스트 만들고 인덱싱하기
arr.append([])
print(arr)
# 마지막에 넣은 빈 리스트에 'korea' 추가
arr[7].append('korea')
print(arr)
# 'korea' 중에서 'a' 만 추출
print(arr[7][0][-1])




""" [ 연습 ] 아래에서
    a = ['인천','부산',['전라','경상',['판교','부천']]]
    (1) '경상' 요소 추출
    (2) '부천' 요소 추출
    (3) '판'이라는 글자만 추출
"""
a = ['인천','부산',['전라','경상',['판교','부천']]]
print(a[2][1])

print(a[2][2][1])

print(a[2][2][0][0])






""" [ 연습 ] 아래에서
    a = ['인천','부산',['전라','경상'],['대전','광주','대구'], '서울','제주']
    (1) '부산'부터 '대구'까지 추출
    (2) '대전'부터 '제주'까지 추출
    (3) '인천'부터 '서울'까지 추출
    (4) '광주'부터 '대구'까지 추출
"""
a = ['인천','부산',['전라','경상'],['대전','광주','대구'], '서울','제주']

print(a[1],a[2],a[3])
print(a[3],a[4],a[5])
print(a[0],a[1],a[2],a[3],a[4])
print(a[3][1],a[3][2])

print(a[1:4])
print(a[3:])
print(a[:5])
print(a[3][1:])


# --------------------------------------------------------------------
# (2) 리스트 연산자

a = ['독','도','는']
b = ['대한민국','섬']

print(a+b)
print(a*3)


# --------------------------------------------------------------------
# (3) 리스트 관련 함수들
#           append()    : 요소 추가
#           sort()      : 리스트 정렬
#           reverse()   : 역순으로 뒤집기
#           index()     : 위치 반환
#           insert()    : 리스트에 요소 삽입
#           remove()    : 요소 제거
#           pop()       : 맨 마지막 요소를 꺼내기
#           count()     : 요소 개수 세기
#           extend()    : 리스트에 리스트를 더하기\
#           clear()     : 모든 요소를 제거

"""
    (1) 리스트 a에 0 요소 추가
    (2) 리스트 a에 9를 추가하여 출력 (a요소에는 추가하는 것은 아님)
    (3) 0번째 요소로 1을 추가
    (4) 3번째 요소로 1을 추가
    (5) 리스트 맨 마지막 요소를 꺼낸다
    (6) 요소 1을 삭제 ( 1이 여러개인 경우 맨 앞에 하나만 삭제됨 )
    (7) 리스트 모든 요소를 삭제
"""
a = [7, 2, 3, 5, 6]

#1
a.append(0)
print(a)

#2
print(a,[9])

#3
a.insert(0,1)
print(a)

#4
a.insert(2,1)
print(a)

#5
print(a.pop())

#6
a.remove(1)
print(a)

#7
a.clear()
print(a)




# [참고] 리스트에 리스트 구조에서 clear() 하는 경우
a1 = [1]
b1 = [7,6, 5,4,3, a1]
print(a1) # [1]
print(b1) # 7,6,5,4,3,1
b1.clear()  # 종속관계로 되어 있기에 b1의 내용만 삭제되고 a1은 유지왼다 1
print(b1) # []
print(a1) # 1
print()



"""
    (8) 리스트 a의 모든 요소를 역순으로 뒤집기
    (9) 리스트 a 정렬하기
    (10) 리스트 a에 리스트 b를 더하기
    (11) 리스트 a에서 0번째부터 1번째 요소까지 삭제
"""
a = [3,5,4,8,0]
b = [1,2]
#8
a.reverse()  #원본 변경
print(a)
#9
a.sort() #원본 변경
print(a)
#10
print(a+b)
#a.extend(b)
print(a)
#11
del a[:2] #원본 변경
print(a)

# --------------------------------------------------------------
#  (4) 리스트 요소 변경
#       - 2번째 요소를 'z'로 변경
#       - 0번째부터 1번째 요소를 'k'와 'o'로 변경
a = [3,5,4,8,0]
a[2] = 'z'
print(a)
a[0:2] = 'k','o'
a[0:2] = ['k','o']
a[0:2] = 'ko'
print(a)
print("--"*50)
#1. 다음 코드의 실행 결과를 쓰시오
a = [0, 1, 2, 3, 4]
print(a[:3], a[:-3]) # 0,1,2         인덱스 0번 부터 2번까지 , 인덱스 0번부터 뒤에서 3번째 전까지
# [0, 1, 2] [0, 1]
#2. 다음 코드의 실행 결과를 쓰시오
print(a[::-1]) # 4? 틀림 닶음 4 3 2 1 0 reverse 의 역할을 하는듯
# [4, 3, 2, 1, 0]
#3. 다음 코드의 실행 결과를 쓰시오
first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]

order = [first, second, third]

john = [order[0][:-2], second[1::3], third[0]]        # 해석 order에서 0번째 인덱스부터 뒤에서 두번째 전까지 저장, 두번째 1번째 인덱스와 1번째 인덱스에서 건너뛴 4번째 인덱스 출력, 전체다 출력
# "egg", "salad", "bread",      chicken,     apple      # [['egg', 'salad', 'bread'] , ['lamb', 'chicken'],
del john[2]          # john list의 2번째 인덱스 제거
 # "egg", "salad", "bread",      chicken,
john.extend([order[2][0:1]])                      # jonn list에  요소 추가 third의 0번째인덱스부터 1번째 인덱스 전까지
  # "egg", "salad", "bread",      chicken,     "apple"
print(john)
# [['egg', 'salad', 'bread'], ['lamb', 'chicken'], ['apple']]
#4
list_a = [3, 2, 1, 4]
list_b = list_a.sort()
print(list_a, list_b)
#내가 생각한 답 3 2 1 4 1 2 3 4 실제 닶 1 2 3 4 none
#5
fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry', 'melon']
print(fruits[-3:], fruits[1::3])
# 'apple', 'banana', 'cherry', 'grape',        'banana'   'orange'
#  ['orange', 'strawberry', 'melon'] ['banana', 'orange']

num = [1, 2, 3, 4]
print(num * 2)
# 1 2 3 4 1 2 3 4



a = [1, 2, 3, 5]
b = ['a', 'b', 'c','d','e']
a.append('g')       #  1 2 3 5 g
b.append(6)     # a b c d e 6
print('g' in b, len(b))   # a b c d e 6 g, 7
# False 6   문자 g 가 리스트 b안에 있는지 물어보는 것 없으므로 False, 리스트의 길이는 6


list_a = ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', 'in', 'South Korea']
list_b=[ ]
for i in range(len(list_a)):    # 9
    if i % 2 != 1:
        list_b.append(list_a[i])
print(list_b)
# ['Hankook', 'is', 'academic', 'located', 'South Korea']


# 9 ???? 2번?        답은 3번 우리가 입력하는 것을 형변환 안하면 무조건 스트링
# admission_year = input("입학 연도를 입력하세요: ")
# print(type(admission_year))

#10
country = ["Korea", "Japan", "China"]
capital = ["Seoul", "Tokyo", "Beijing"]
index = [1, 2, 3]
country.append(capital)  #      ["Korea", "Japan", "China" ,["Seoul", "Tokyo", "Beijing"]]
country[3][1] = index[1:]
print(country)
# ["Korea", "Japan", "China" ,["Seoul", "2", "3"]]
# ['Korea', 'Japan', 'China', ['Seoul', [2, 3], 'Beijing']]    # contry의 인덱스 3번째안에 있는 1번째 인덱스를  변수 인덱스 의 1번째 인덱스부터 시작하는 1 2로 교체

#11
# True #False # 내가 이렇게 답을 적은 이유는 is는 주소 값을 비교한다고 했으니까 리스트 안에 들어있는 값은 똑같아도 a 와 c는 각각 선언 했기에 값의 주소가 다르다
a = [5, 4, 3, 2, 1]
b = a
c = [5, 4, 3, 2, 1]
print(a is b)
print(a is c)

#15
list_1 = [[1, 2], [3], [4, 5, 6]]
a,b,c = list_1
list_2 = a + b + c
print(list_2)
#[[1, 2], [3], [4, 5, 6]]   