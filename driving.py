country = input('請問你來自哪個國家？ ')
age = input('請輸入年齡： ')
age = int(age)
if country == '台灣':
    if age < 18:
        print('你還太嫩了')
    else:
        print('恭喜你可以開車車了')
elif country == '木葉忍者村':
    if age > 30:
        print('恭喜你，你活得比第一代火影那時的國名平均壽命還久')
    else:
        print('我愚蠢的歐豆豆呦')
else:
    print('笑死，你只能是台灣人or木葉忍者村的')                            