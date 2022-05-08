count=0
for string in 'content':
    count+=1
    if string == 't':
        break  #強制跳出整個迴圈
        #continue #跳過本次，繼續下個迴圈
        #pass #什麼事都不做
    print (string)

print('\n迴圈結束')
print('迴圈執行了 %d 次' %count)

#https://medium.com/@chiayinchen/1-%E5%88%86%E9%90%98%E6%90%9E%E6%87%82-python-%E8%BF%B4%E5%9C%88%E6%8E%A7%E5%88%B6-break-continue-pass-be290cd1f9d8