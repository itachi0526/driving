country = input('請問你來自哪個國家？ ')
age = input('請輸入年齡： ')
age = int(age)
if country == '台灣':
    if age < 18:
        print('你還太嫩了')
    else:
        print('恭喜你可以開車車了')  