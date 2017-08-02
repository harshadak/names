# Part I
def print_names():
    students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
        #print data
    for value in students:
        print value['first_name'], value['last_name']
            
print_names()


# Part II
def students_instructors():
    users = {
        'Students': [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ],
        'Instructors': [
            {'first_name' : 'Michael', 'last_name' : 'Choi'},
            {'first_name' : 'Martin', 'last_name' : 'Puryear'}
        ]
    }

    for key, data in users.items():
        print key
        i = 1
        #print data
        for value in data:
            name_length = len(value["first_name"] + value["last_name"])
            print i, " -", value["first_name"], value["last_name"], "-", name_length
            i += 1
students_instructors()