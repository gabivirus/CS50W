people = [
    {'name': 'harry', 'house': 'gryffindor'},
    {'name': 'cho', 'house': 'ravenclow'},
    {'name': 'draco', 'house': 'slytherin'}
]

def f (person):
    return person["name"]

#people.sort(key=lambda person: person["name"])
#people.sort(key="name")

print(f)