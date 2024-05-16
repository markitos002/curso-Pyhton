planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])
planets[3] = "Red Planet" # modifies the value of a list item
print("Mars is also known as", planets[3])

number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

planets.append("Pluto")
number_of_planets = len(planets) #len() is a built-in function that returns the number of items in a list
print("There are actually", number_of_planets, "planets in the solar system.")

planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

for planet in planets:
    print(planet, end=" ")

print("The first planet is", planets[0])

print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

jupiter_index = planets.index("Jupiter") # returns the index of the first occurrence of a value
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

mercury_index = planets.index("Mercury")
print("Mercury is the", mercury_index + 1, "planet from the sun")

gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
print("The gravity on Venus is", gravity_on_planets[1], "m/s^2")    # Venus is the second planet from the sun

bus_weight = 124054 # in Newtons, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "N")
print("On Venus, a double-decker bus weighs", bus_weight * gravity_on_planets[1], "N")
print("On Mars, a double-decker bus weighs", bus_weight * gravity_on_planets[3], "N")   
print("On Jupiter, a double-decker bus weighs", bus_weight * gravity_on_planets[4], "N")

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "N")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "N")

planets_before_earth = planets[0:2]
print(planets_before_earth)

planets_after_earth = planets[3:8]
print(planets_after_earth) 


planets_after_earth = planets[3:] # a segmentation creates a new list, it does not modify the original list
print(planets_after_earth) 

print(planets_after_earth + planets_before_earth + planets)

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons # the contatenation of two lists creates a new list
print(amalthea_group + galilean_moons)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
regular_satellite_moons.sort(reverse=True)  # the use of sort modifies the original list
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

user_planet = input("Please enter the name of the planet (with a capital letter to start)")
planet_index = planets.index(user_planet)

print("Here are the planets closer than " + user_planet)
print(planets[0:planet_index])

print("Here are the planets closer than " + user_planet)
print(planets[0:planet_index])