
counties = ['Araphoe','Denver','Jefferson']
if counties[1] == 'Denver':
    print(counties[1])
if counties[2] != 'Jefferson':
   print(counties[2])

if 'El Paso' in counties:
    print('El Paso is in the list of counties.')
else:
    print('El Paso is not in the list of counties')

if 'Araphoe' in counties or 'El Paso' in counties:
    print('Araphoe or El Paso are in the list of counties.')
else:
    print('Araphoe and El Paso is not in the list of counties')

if 'Araphoe' in counties and 'El Paso' not in counties:
    print('Only Araphoe is in the list of counties')
else:
    print('Araphoe is in the list of counties and El Paso is not in the list of counties')

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
for num in range(5):
    print (num)

for i in range(len(counties)):
    print(counties[i])

counties_dic = {'Araophoe':422829,'Denver':463353,'Jefferson':432438}
for county in counties_dic:
    print(county)






