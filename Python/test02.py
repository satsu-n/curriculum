while True:
    try:
        print()
        print('1: ValueError例外を発生')
        print('2: IndexError例外を発生')
        print('3: 例外を発生させない')
        print('4: 終了')
        number = int(input('選択してください。: '))
        # 問①：if文を用いて、以下の画像のように処理されるように記述しましょう。
        ##ここに書く
        print('↓')
        if number == 1:
            value = int('hoge')
        elif number == 2:
            Index = [10,20,30]
            print(Index[3])
        elif number == 3:
            print('例外を発生させませんでした')
        elif number == 4:
            print('終了します')
            break

    except ValueError as e:
        print('ValueError')
        print(e.args)

    except IndexError as e:
        print('IndexError')
        print(e.args)

    # 問②：else節を用いて、以下の画像のように処理されるように記述しましょう。
    ##ここに書く
    else:
        print('↓')
        print('もう一度選択しましょう')

print('↓')
print('無限ループを終了します')