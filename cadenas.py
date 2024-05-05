fact = "The moon has no atmosphere."
print(fact)

two_facts = fact + " No sound can be heard on the moon."
print(two_facts)

triple = """We only see about 60% of the Moon's surface, this is known as the "near side"."""
print(triple)


multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

multiline = """Facts about the Moon:
 There is no atmosphere. 
 There is no sound."""
print(multiline)

#here are some examples of string methods in Python:

print("temperatures and facts about the moon".title())
heading = "temperatures and facts about the moon"

heading_upper = heading.title()
print(heading_upper)

temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)

temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n')
print(temperatures_list)

print("Moon" in "This text will describe facts and challenges with space travel")
print("Moon" in "This text will describe facts about the Moon")

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))

print("The Moon And The Earth".lower())

print("The Moon And The Earth".upper())

temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

print("-60".startswith('-'))

if "30 C".endswith("C"):
    print("This temperature is in Celsius")

print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))
