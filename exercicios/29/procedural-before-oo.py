
def person(name, phone, email):
    return {
        'name': name,
        'phone': '99999-9999',
        'email': '',
    }

def student(name, phone, email, number, avarage_mark):
    lperson = person(name, phone, email)
    lperson['number'] = number
    lperson['avarage_mark'] = avarage_mark
    return lperson

def person_purchase_pass(person):
    print(f'{person.name} buyed a pass')

def student_is_aligible(person):
    return person['avarage_mark'] > 70


g_student = student('Bruno', '9999', 'bruno@', 'AB999999', 80)
print(g_student)