що = input("Що робимо? (+, -, /, *): ")

а = float(input("Введіть перше число: "))
б = float(input("Введіть друге число: "))

if що == "/" and б == 0:
    print("Дебіл, на нуль ділити не можна")
else:
    if що == "+":
        результат = а + б
    elif що == "-":
        результат = а - б
    elif що == "*":
        результат = а * б
    elif що == "/":
        результат = а / б
    else:
        print("Неправильний вибір")

    if що in ("+", "-", "/", "*"):
        print("Результат: " + str(результат))
