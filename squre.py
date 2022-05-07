n=input('input a number: ') #輸入一個數字(文字)
n=int(n) #輸入的數字轉成整數型態
for i in range(n): #列出從0到n的整數
    if i*i==n: #布林值判斷
        print(i)
        break #用break強制結束迴圈，不執行else
else:
    print('NA')
