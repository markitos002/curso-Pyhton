import math
from math import ceil, floor


answer = 30 + 12
print(answer)

diff = 100 - 50
print(diff)

product = 10 * 5
print(product)

qoutient = 100 / 4
print(qoutient)

seconds = 1042
display_minutes = 1042// 60
print(display_minutes)

display_seconds = 1042 % 60
print(display_seconds)

result_1 = 1032 + 26 * 2
print(result_1)


first_planet = 149597870  # distance from the sun in km
second_planet = 778547200 # distance from the sun in km

distance_between_planets = second_planet - first_planet
print(distance_between_planets)

distance_mi = distance_between_planets / 1.609344
print(distance_mi)

demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

print(39 - 16)
print(16 - 39)

print(abs(39 - 16))
print(abs(16 - 39))

print(round(1.4))
print(round(1.5))
print(round(2.5))
print(round(2.6))

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)

first_planet_input = int(input('Enter the distance from the sun for the first planet in km'))
second_planet_input = int(input('Enter the distance from the sun for the second planet in km'))

print(first_planet_input + second_planet_input)

distance_km1 = second_planet_input - first_planet_input
print(abs(distance_km1))


