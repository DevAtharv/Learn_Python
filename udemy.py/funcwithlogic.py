def even_check(number):
    reasult= number % 2==0
    return reasult

even_check(20)

even_check(21)

# RETURN true if any number is even inside a list
def check_even_list (num_list):
    
    for number in num_list:
        if number % 2 == 0:
            return True
    else:
        pass
    
print(check_even_list([1,3,5]))

print(check_even_list([2,4,6]))