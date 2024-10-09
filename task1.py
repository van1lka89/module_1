from itertools import count

calls=0
def count_calls():
    global calls
    calls=calls+1
def string_info(str_1):
    count_calls()
    a=[]
    a.append(len(str_1))
    a.append(str(str_1).upper())
    a.append(str_1.lower())
    return a
def is_contains(str_2,list_1):
    count_calls()
    list_2=[x.upper()for x in list_1]
    if str_2.upper() in list_2:
        return True
    else:
        return False
print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)

