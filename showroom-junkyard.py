showroom = set()

showroom.add('Honda Accord')
showroom.add('Toyota Camry')
showroom.add('Nissan Altima')
showroom.add('Ford Bronco')

# print(len(showroom))

showroom.add('Ford Bronco')

# print(showroom)

showroom.update({'Ford Mustang', 'Dodge Charger'})

# print(showroom)

showroom.discard('Dodge Charger')

junkyard = {'Honda Civic', 'Subaru Outback', 'Nissan Altima', 'Toyota Camry'}

# print(showroom.intersection(junkyard))

showroom.union(junkyard)

showroom.discard('Ford Mustang')

print(showroom)