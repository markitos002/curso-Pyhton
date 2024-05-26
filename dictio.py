planet = {
    'name' : "Earth" , 
    'moons': 1
}

print(planet.get('name'))
print(planet['name'])

wibble = planet.get('wibble') # Returns None
# wibble = planet['wibble'] # Throws KeyError

print(wibble)

planet.update({'name': 'Makemake'}) # Updates the value of 'name'
print(planet.get('name'))

planet.update({
    'name': 'Jupiter',
    'moons': 79
})

planet['orbital period'] = 4333

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }

planet.pop('orbital period')

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }

# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }

planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}

print(planet)
print(f'{planet["name"]} has {planet["moons"]} moon(s)')
print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')