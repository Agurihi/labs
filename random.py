import random
vid = int(input("Початок діапазону:"))
do = int(input("Кінець діапазону:"))
gim = int(input("кількість цифр:"))
for i in range(gim):
    random_x = random.randint(vid,do)
    print(random_x)
