
# -----------------------------------------
#  문자열 포맷
#       0- 문자열 포맷팅
#               print('내가 좋아하는 숫자는 ', 100 )
#       1- format() 이용
#               print('내가 좋아하는 숫자는 {0:d} 이다'.format(100) )
#       2- % 사용
#               print('내가 좋아하는 숫자는 %d 이다' % 100 )
#       성능(속도)는 %이 더 빠르다고는 하지만 코드가 깔끔하게 하는 것이 더 중요하다고 하고는
#       어느 것으로 선택하라고는 안 나옴


# format()이용
msg = '{0}님 오늘도 행복하세요. - {1}로부터'
print(msg.format("홍길동",'대한민국'))
msg = '{1}님 오늘도 행복하세요. - {0}로부터'
print(msg.format("홍길동",'대한민국'))

msg = '{name}님 오늘도 행복하세요. - {group}로부터'
print(msg.format(name="홍길동",group='대한민국'))


# [참고] http://pyformat.info

# % 이용 - printf() 역할
name = '홍길동'
age = 22
height = 170.456
print('%s님 %d세 입니다. 그리고 키는 %fcm 입니다.' % (name, age, height))



#--------------------------------------------------
# 실수인 경우
# 출력결과 : 내가 좋아하는 숫자는 ____________입니다.
su=99.999999
print("내가 좋아하는 숫자는 %f입니다." %(su))
msg = "내가 좋아하는 숫자는 {su}입니다."
print(msg.format(su=su))


print('내가 좋아하는 숫자는 ', su, '입니다.')
print('내가 좋아하는 숫자는 {0:.2f} 입니다.'.format(su)) # 소숫점 자리 맞추기  반올림 해서 소숫점 자리 맞추니까 데이터 변환 조심하기
print('내가 좋아하는 숫자는 %.2f 입니다.' % su)
