
calls = 0 # Глобалка

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()  # проверка на регистры
    return (length, upper_case, lower_case)

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower() # понижаем регистр
    for item in list_to_search:
        if string_lower == item.lower(): # снова
            return True
    return False

print(string_info('Capybara')) # кортеж
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # для True
print(is_contains('cycle', ['recycling', 'cyclic']))    # для False

print(calls) # 4 вызова

