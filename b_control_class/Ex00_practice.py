# 리스트를 인자로 받아 짝수만 갖는 리스트 반환하는 함수 ( 함수명 : even_filter )
# [ 실행 ]
# print(even_filter([1, 2, 4, 5, 8, 9, 10]))

def even_filter(list_value):
    return [i for i in list_value if i % 2 == 0]


print(even_filter([1, 2, 4, 5, 8, 9, 10]))


# 주어진 수가 소수인지 아닌지 판단하는 함수 ( 함수명 : is_prime_number )
def is_prime_number(k):
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 2:
        return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True


print(is_prime_number(60))
print(is_prime_number(61))


# 주어진 문자열에서 모음의 개수를 출력하는 함수 ( 함수명 : count_vowel )
def count_vowel(word):
    cnt = 0
    vowel = 'aeiou'
    for i in vowel:
        cnt += word.count(i)

    print(cnt)


print(count_vowel("pythonian"))
