# 関数, randomモジュール, 変数, if文, 入出力

import random

def judge(x, y):
  if x > y:
    j = "あなたの勝ち"
  elif x < y:
    j = "あなたの負け"
  else:
    j = "引き分け"
  print(j)

card = [1, 2, 3, 4, 5]
x = input("1～5の中からカードを選んでください\n")
x = int(x)
x -= 1

y = random.randint(0, 4)

print("あなたのカード：{}" .format(card[x]))
print("コンピュータのカード：{}" .format(card[y]))

judge(x, y)
