#name = "admin"
#age = 20
#print(age, type(age))
#print(name, type(name), id(name))
#a = b = c = 1
#print(a, b, c)
#a, b, c = 5, "Hello", 9.2
#print(a, b, c)
#s1 = "Hellow"
#s2 = "world"
#s3 = s1 + ", " + s2 + "!" # конкатенация строк
#print(s3 *3) # умножение строк
num = 4321
print("Исходное:", num)
#1234
one = num % 10 # последняя цифра = остаток от деления на 10
num = num // 10 # остаток от целочисленного деления
two = num % 10
num = num // 10
three = num % 10
num = num // 10
four = num % 10
print("Обратное:", one * 1000 + two * 100 + three * 10 + four)
num = 4321
res = num % 10 * 1000
num = num // 10 #432
res += num % 10 * 100 # previous res 1000 + 200
num = num // 10
res += num % 10 * 10
num = num // 10
res += num % 10
print("Reversed:", res)

