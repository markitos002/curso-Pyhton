a = 90
b = 65
#test

if a < b:
    #print the statement to be executed if the condition is true
    print(b)
else:
    print(a)


c = 27
d = 27
if c <= d:
    print("a is less than or equal to b")
elif c == d:
    print("a is equal to b")

a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)
else:
    print(a - b)


object_size = 10
proximity = 9000

if object_size > 5 and proximity < 1000:
    print('Evasive maneuvers required')
else:
    print('Object poses no threat')