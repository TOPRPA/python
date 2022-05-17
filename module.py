#載入內建的sys模組並取得資訊
# import sys
# print(sys.platform)
# print(sys.maxsize)

#建立geometry模組，載入使用
# import geometry
# result=geometry.distance(3,3,10,18)
# print(result)
# result2=geometry.slope(3,3,10,18)
# print(result2)

#調整模組搜尋路徑
import sys
sys.path.append("modules") #在模組路徑中加入modules的相對路徑
print(sys.path) #印出模組搜尋路徑