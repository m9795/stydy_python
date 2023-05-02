#入出力
#print("Hello World")
#x = input("数字を入力してください。\n")
#print("入力した数字は{}です。\n" .format(x))

#Cのdo~while→while True:~~if: break

while True :
  print("メニューを選択してください。")
  x = input("1:レンジ\n2:オーブン\n")
  x = int(x)

  if x == 1:
    y = "\n選択中のメニュー:レンジ"
  elif x == 2:
    y = "\n選択中のメニュー:オーブン"
  else:
    y = "\nERROR!\n"
  print(y)
  if x == 1 or x == 2:
    break

print("時間を選択してください。")

if x == 1:
  z = input("1:10秒\n2:1分\n3:5分\n")
  z = int(z)
elif x == 2:
  z = input("1:10分\n2:30分\n3:1時間\n")
  z = (z)

#print("メニュー：{}　時間：{}". format(x,z))
#メニューと時間を配列にする？
