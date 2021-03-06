# (0) 문자열을 "" 이나 '' 으로 표현



# -----------------------------------------
# (1) 개행을 포함한 문자열
msg = """
    안녕하세요.
    저는 성이 파이이고,
    이름은 썬입니다.
    잘 부탁합니다.
"""
print(msg)

msg = '''
    행복합시다
    즐깁시다
    오늘도
'''
print(msg)

# -----------------------------------------
#  (2) 문자열 연산
#       문자열 합치기 : 문자열 + 문자열
#       문자열 반복 : 문자열 * 숫자

a = '독도는 '
b = "한국이다. "
c = a+b
d = "ox"
print("-"*50)
print(c)
print(d*25)
print((c)*3)
print("="*50)
""" [ 출력결과 ] 
        --------------------------------------------------
        독도는 한국이다. 
        oxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxox
        독도는 한국이다. 독도는 한국이다. 독도는 한국이다. 
        ==================================================
"""

print("-"*50+'\n'+(a+b)+'\n'+'ox'*25+'\n'+(a+b)*3+'\n'+'='*50)

# -----------------------------------------
#  (3) 문자열의 인덱싱과 슬라이싱
#       - 인덱스는 0부터 시작한다
#       - s[i] : s 문자열에서 i번째 문자 추출
#       - s[i:j] : s 문자열에서 i번째에서 j-1까지의 문자 추출
#       - s[i:j:k] : s 문자열에서 i번째에서 j-1까지에서 k개씩 건너뛰어 문자 추출
#
#       - s[-i] : s 문자열에서 뒤에서부터 i번째 문자 추출
#                 ( 뒤에서 인덱스는 1부터 센다 )

s=[1,2,3]
s[1:3] # [2 1
print("#"*50)
print(s[1:2]) # 인덱스1 -> 2번째 : 3번째인데 ->인덱스 2번째
print("#"*50)
msg ='오늘도 행복도 하다'
# print(msg[0])
# print(msg[0:3]) # 도
# print(msg[0:5:2]) # 도
# print(msg[-1]) # 다
""" [ 출력결과 ]
        오
        오늘
        늘도 행복
        오도행
        다
"""
print(msg[0])#오
print(msg[0:2]) # 오늘 0번째문자 오랑 msg 문자열의 앞에서 2번째 까지 출력 [1:0] <- 하면 공백나옴 왜냐하면 1은 늘 이지만 뒤에 오는 0은 문자열에서 0번째라서 공백임
print(msg[1:6]) # 늘도 행복 0오 1늘 : 1오2늘3도4 5행6복 -> 1:늘도 행6:복
print(msg[0:5:2]) # 오도행  0오: 1오2늘3도4 5행: 2글자씩 건너뛰어라 1오 3도 5행
print(msg[-1]) # 다 뒤에서 한글자

""" [ 참고 ] 
       ` msg[0] == msg[-0] 같은 값을 추출
       ` msg[:] 전체 추출
       ` msg[i:-j] i번째부터 뒤에서 j-1 까지 추출
"""
# print(msg[0])#오
# print(msg[-0])#오
# print(msg[:])#오늘도 행복도 하다
# print(msg[2:-2])# 2번째부터 뒤에서 2글자 까지의 사이의 글자를 출력
print(msg[2:-2]) #0오1늘2도3 4행5복6도7 8하9다  2번째인 5 뒤에서 9다 8하를 뺀" "공백 7까지 즉 도 행복도

""" [ 확인 ]
    1- 문자열 끝까지라면 두번째 숫자 생략 가능
    2- 처음부터 시작하는 것이라면 첫번째 숫자 생략 가능
"""
print("@"*50)
msg ='오늘도 행복도 하다'
# 1) 인덱스 5번째 글짜 출력
print(msg[5]) #0오1늘2도3 4행5복
# 2) 앞에서 부터 5개 출력
print(msg[:5]) #0오1늘3도4 5행
# 3) 앞에서 부터 5개 출력하고 2개씩 건너 뛰기
print(msg[:5:2]) #오도행
# 4) 문자열 전체를 2개씩 건너 뛰기
print(msg[::2])

# 회문 # 기러기 토마토 문자가 대칭 인것
a = '1001' \
    ''
a2 = a[::-1]
if a == a2:
    print('회문임')
else:
    print('회문아님')

print("@"*50)
""" [ 연습-1 ]
    날짜와 시간을 표현하는 문자열에서 '2020-02-22 : 12:05:12'
    '2020년 2월 22일' 출력
    '12시 5분' 출력
"""
f = '2020-02-22 : 12:05:12'

print(f[0:4]+'년'+f[5:7]+'월'+f[8:10]+'일')
print(f[-8:-6]+'시'+f[-5:-3]+'분')
# -----------------------------------------
#  (4-1) 문자열 관련 함수
#       s.count('글') : s 문자열에서 '글'이라는 문자 개수 세기
#       s.index('글') : s 문자열에서 문자 '글' 위치 알려주기
#       s.find('글') : s 문자열에서 문자 '글' 위치 알려주기 없는 글자를 찾을때는 find -1을 리턴해줌
#       s.rfind('글') : s 문자열에서 문자 '글' 오른쪽에서 왼쪽으로 찾아서 위치 알려주기
#       len(s) : s 문자열 길이
print("@"*50)
msg ='오늘도 행복도 하다'

""" [ 출력결과 ]
    1) '행복'이라는 글자 위치 찾기
    2) '가자'라는 글자 위치 찾기
    3) '행복'이라는 글자를 오른쪽에서 왼쪽으로 찾기
    4) 문자열 전체 길이 구하기
    5) '도'라는 단어의 갯수 구하기
"""
print(msg.index('행복')) # 값이 없으면 에러 index와 find는 비슷하지만 다름
print(msg.find('가자')) #값이 없으면 -1로표시
if(-1==msg.find('가자')):
    print("True")
else:
    print("False")
print(msg.rfind('행복')) # 첫글자를 기준으로 오른쪽에서 몇번째 글자인지 find와 마찬가지로 값이 없으면 -1로
print(len(msg)) #문자열의 전체길이
print(msg.count('도')) # 문자열에서 '도'가 몇 개가 있는지 알려줌

# -----------------------------------------
#  (4-2) 문자열 관련 함수
#   s.upper() : 소문자를 대문자로
#   s.lower() : 대문자를 소문자로
#   s.lstrip() : 왼쪽 공백 지우기
#   s.rstrip() : 오른쪽 공백 지우기
#   s.strip() : 양쪽 공백 지우기
print("@"*50)
msg = '  This is My Life  '
print(msg.upper()) # 대문자
print(msg.lower()) # 소문자
print(msg.lstrip()) #왼쪽공백제거
print(msg.rstrip()) #오른쪽공백제거
print(msg.strip())

# [고민]
print(msg.replace(" ","")) #공백을 없애기



print("@"*50)
# -----------------------------------------
#  (4-3) 문자열 관련 함수
#   s.replace("a","b")  :  s 문자열에서 단어 a를 단어 b로 바꾸기
#   s.split() : s 문자열을 공백으로 나누기
#   s.split('z') : s 문자열을 z 기호로 나누기
#   d.join(s) : d 단어를 s 문자열에 삽입
msg = "우리는 독도를 지킨다"

print(msg.replace("독도","대한민국")) # 원본을 훼손하지 않는다.
print(msg.split()) #문자열을 공백으로 나누기
print(msg.split('z')) # ?????????????
print(",".join(msg))#문자의 사이마다 z를 넣기

# 단어별로 : ':' 문자를 삽입 
print(":".join(msg.split())) # 공백을 기준으로 : 을 삽입






