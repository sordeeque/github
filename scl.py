print('welcome ')

school = {
'pry1':[{
    'name',
    'age',
    'std_cls',
    'dob',}],
'pry2':[{
    'name',
    'age',
    'std_cls',
    'dob',}],
'pry3':[{
    'name',
    'age',
    'std_cls',
    'dob',}]
}
name = input('what is your name: \n')
age = input('what is your age: \n')
std_cls = input('what class are you(pry1/pry2/pry3): \n')
dob = input('what is your class: \n')

if std_cls == 'pry1':
    school['pry1'] = {name, age, std_cls, dob}
    print(school)
elif std_cls == 'pry2':
    school['pry2'] = name, age, std_cls, dob
    print(school)
elif std_cls == 'pry3':
    school['pry3'] = name, age, std_cls, dob
    print(school)
    

else:
    print('your class have not been creat')
