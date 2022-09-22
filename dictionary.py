'''dictionary = {
    key:value
    key:[value,value,[value]]

    }

print()
dictionary[]
NB: all doors most be opened b4 accessed
NB: all function must have ()
NB: a dic can be accesed with key
NB: a list can be accessed with index
index[]
(dictionary['key'].append('value'))

#ways to use your1
dic
student = {'name':'john', 'age': 25, 'courses':['math','english']}

# to access a dic
print(student['name'])
print(student['courses'][1])
print(student.get('phone','not found'))
#to add to a dic
student['name'].append('sodiq','james')
#to update a key in a dic
dictionary['key'] = 'value'
or
dictionary.update('key':'value')
print(len(student))
print(student.keys)
print(student.value)
print(student.item)'''







school = {}

num_std = input("how many std did u want to register: ")

n = 0

while n < int(num_std):
    name = input('enter std name: ')
    age = input('enter std age: ')
    phone = input('enter std num: ')
    school[name] = {'name':name, 'age':age, 'phone':phone}
    n += 1
for items in school[name]['age']:
    n += 1
    print(items)










