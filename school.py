print('welcome')

school = {'s_cls':{
'pry1':{
    'name':[],
    'age':[],
    'std_cls':[]
    },
'pry2':{
    'name':[],
    'age':[],
    'std_cls':[]
    },
'pry3':{
    'name':[],
    'age':[],
    'std_cls':[]
    }
}}

num_std = int(input('how many student did you want to register: \n'))

n = 0

while n < num_std:
    name = input('student name: \n')
    age = input('student age: \n')
    std_cls = input('student class(pry1/pry2/pry3): \n')

    n += 1

    if std_cls == 'pry1':
        school['pry1'] = {'name':name, 'age':age, 'std_cls':std_cls}
        print(school)
    elif std_cls == 'pry2':
        school['pry2'] = {'name':name, 'age':age, 'std_cls':std_cls}
        print(school)
    elif std_cls == 'pry3':
        school['pry3'] = {'name':name, 'age':age, 'std_cls':std_cls}
        print(school)
    else:
        print('your class have not been created')

