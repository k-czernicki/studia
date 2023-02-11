# ex 1
# write Logger class taking and storing name in init
# with methods: info, warning, error, and critical
# each taking messafge argument and printing
# '{name of logger} {method name}: {message}'

# ex 2
# refactor Logger class to use only one '_log' method
# for prinitng messages

logger = Logger('simple_logger')
logger.info('hello')
logger.critical('world')
print()

# ex 3
# write functio taking iterable(list, tuple)
#     returning elements on odd indexes

print(print_odd_indexes([6,3,5,26,7,3]))
print(print_odd_indexes((6,3,5,26,7,3)))
print()

# ex 4
# write function checking if word is palindrome
#   palindrome is a word that read same from both
#   sides like 'level' and 'sos'

is_palindrome('level')
is_palindrome('lelevel')
print()

# ex 5
# write function calculting bmi value and give
# option to round calculated result
# tip: use default argument
# more or less: bmi = weight_in_kg / height_in_m ** 2

print('bmi', bmi(81, 1.76))
print('bmi', bmi(81, 1.76, True))
print('bmi', bmi(81, 1.76, round_result=True))
print()
