def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum=sum+n
    return sum #回傳for迴圈的計算結果
value=calculate(10)
print(value)
