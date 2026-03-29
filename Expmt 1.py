#Boolean
is_africaines_black = True
is_arabes_white = False
is_australiens_green = False
print(f"Africaines are black: {is_africaines_black}")
print(f"Arabes are white: {is_arabes_white}")
print(f"Australiens are green: {is_australiens_green}")

#string
name="sourou_kire"
age="towenty one"
email="souroukire@gmail.com"
print(f"hi {name}")
print(f"your age is:{age}")
print(f"your email ID:{email}")


#float
otp=33.02
distance=5.3
payment=210.75
print(f"your otp is:{otp}")
print(f"your distance is:{distance}km")
print(f"your payment is:${payment}")

#integer
age=22
white=75
hight=2
print(f"i am {age}years old")
print(f"my white is:{white}kg")
print(f"my hight is:{hight}m")
#FUNCTION
def add(x, y):
    z = x + y
    print("Addition:", z)

def subtract(x, y):
    z = x - y
    print("Subtraction:", z)

def multiply(x, y):
    z = x * y
    print("Multiplication:", z)

def divide(x, y):
    if y != 0:
        z = x / y
        print("Division:", z)
    else:
        print("Cannot divide by zero")

x = 3
y = 4

add(x, y)
subtract(x, y)
multiply(x, y)
divide(x, y)

OUTPUT:

Africaines are black: True
Arabes are white: False
Australiens are green: False

hi sourou_kire
your age is:towenty one
your email ID:souroukire@gmail.com

your otp is:33.02
your distance is:5.3km
your payment is:$210.75

i am 22years old
my white is:75kg
my hight is:2m

Addition: 7
Subtraction: -1
Multiplication: 12
Division: 0.75
