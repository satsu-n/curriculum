all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
wait_place = ["札幌","大阪"]
get_place = ["横浜"]

for place in all_place:
    if place in get_place:
        print(place + "のチケットが当選しました！")
    elif place in wait_place:
        print(place + "のチケットは結果待ち")
    else:
        print(place + "のチケットは落選しました")


get_place += wait_place
s = "{0}と{1}と{2}のチケットが当選しました！"
print(s.format(get_place[0],get_place[1],get_place[2]))