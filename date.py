from datetime import date

print(date.today())
print(date.today().year)
print("Today is", date.today().strftime("%a %b %d %Y"))
print("Today's date is:" + str(date.today()))

