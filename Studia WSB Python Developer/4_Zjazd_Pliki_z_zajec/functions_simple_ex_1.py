
# write function 'execute_twice' taking
#     another function and executing it twice
def print_me():
    print('me')

def print_him():
    print('him')

def execute_twice(func):
    func()
    func()

execute_twice(print_me)
execute_twice(print_him)
print()

# write two function returning one number each
# write function 'sum_func_results' taking
#    two functions, returning sum of taken functions results

def get_11():
    return 11

def get_22():
    return 22

def sum_func_results(func_1, func_2):
    # result_1 = func_1()
    # result_2 = func_2()
    # return result_1 + result_2
    return func_1() + func_2()

print(sum_func_results(get_11, get_22))
