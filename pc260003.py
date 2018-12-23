def calcute_profit(I):
  I = I / 10000
  if I <= 10:
    a = I * 0.01
    return a * 10000
  elif I <= 20 and I > 10:
    b = 0.25 + I * 0.075
    return b * 10000
  elif I <= 40 and I > 20:
    c = 0.75 + I * 0.05
    return c * 10000
  elif I <= 60 and I > 40:
    d = 0.95 + I * 0.03
    return d * 10000
  elif I <= 60 and I > 100:
    e = 2 + I * 0.015
    return e * 10000
  else:
    f = 2.95 + I * 0.01
    return f * 10000

I = int(input('净利润:'))
profit = calcute_profit(I)
print('利润为%d元时，应发奖金总数为%d元' % (I, profit))