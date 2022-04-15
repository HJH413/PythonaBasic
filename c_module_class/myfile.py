#myfile.py
#from mypackage.mymodule import *
#import mymodule as mm 패키지 불러올때 별칭을 사용하기도함 별칭을 사용시 원래 명칭은 못 불러옴
# print('오늘의 날씨는 ', get_weather(), '입니다')
# print('오늘의 요일은 ', get_date(), '입니다')

# import mypackage.mymodule
#
# print('오늘의 날씨는 ', mypackage.mymodule.get_weather(), '입니다')
# print('오늘의 요일은 ', mypackage.mymodule.get_date(), '입니다')

#from mypackage.mymodule import *
from mypackage import mymodule

print('오늘의 날씨는 ', mymodule.get_weather(), '입니다')
print('오늘의 요일은 ', mymodule.get_date(), '입니다')


# 1번의 3
# 2번의 3
# import fah_converter as fah
# 4번의 2
# from calculator import *