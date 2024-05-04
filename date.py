from datetime import date

print(date.today())
print(date.today().year)
print("Today is", date.today().strftime("%a %b %d %Y"))
print("Today's date is:" + str(date.today()))

parsec = 11
light_year = 3.262 * parsec
print(str(parsec) + " parsecs is equal to " + str(light_year) + " light years")
