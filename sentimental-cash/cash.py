import math

coins_used = 0
while True:
    try:
        owned = float(input("Change owned: "))
        if owned > 0:
            break
    except:
        owned = float(input("Change owned: "))
cents = round(owned * 100)

while cents >= 25:
    coins_used += 1
    cents -= 25

while cents >= 10:
    coins_used += 1
    cents -= 10

while cents >= 5:
    coins_used += 1
    cents -= 5

while cents >= 1:
    coins_used += 1
    cents -= 1
print(coins_used)