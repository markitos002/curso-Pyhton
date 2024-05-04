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