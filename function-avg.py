#無限/不定 參數資料 (以Tuple資料型態處裡)
def avg(*ns):
    sum=0 #先另一個參數sum=0
    for n in ns: #把ns中的資料一個一個提出來
        sum=sum+n #在迴圈內，將提出來的資料一個一個加起來
    print(sum/len(ns)) #len為資料的長度，可用來作為數量
avg(3,4)
avg(10,11,15,103)


#參數的預設資料
# def power (base,exp=0):
#     print(base**exp)
# power(101) #若沒有給exp資料，系統會自動帶入

#多行一起註解 ctrl+/ (不能用數字鍵的/)