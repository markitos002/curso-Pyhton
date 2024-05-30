def rocket_parts():
    print("payload, propellant, structure")
output = rocket_parts()
output

#funciones integradas

any([False, False, False]) 
#any()   # True si alguno de los elementos es True

str(15)   # convierte a string

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
    
distance_from_earth("Moons")  # 238,855
salida = distance_from_earth("Moons")
print(salida)

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

salida2 = round(days_to_complete(238855, 1000) ) # 9.952083333333334 
print(salida2)
