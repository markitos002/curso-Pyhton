people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Ginny", "house": "Gryffindor"},
    {"name": "Luna", "house": "Ravenclaw"}
]
print(people)
print()

people.sort(key=lambda person: person["name"])

for person in people:
    print("{name} is in {house} house".format(**person))

print()

movies = [
    {"title": "Green Book", "year": 2018},
    {"title": "The Shape of Water", "year": 2017},
    {"title": "Moonlight", "year": 2016},
    {"title": "Spotlight", "year": 2015},
    {"title": "Birdman", "year": 2014},
    {"title": "12 Years a Slave", "year": 2013}
]
print(movies)
print()
movies.sort(key=lambda movie: movie["year"])

for movie in movies:
    print("{title} was released in {year}".format(**movie))
