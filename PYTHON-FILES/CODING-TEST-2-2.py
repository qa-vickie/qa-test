def lucky_sum (numbers):

    my_sum = 0

    for i in numbers:
        n = int(i)
        if n != 13:
	    my_sum = my_sum + n
        else:  
            break 
    return (my_sum)

str_numbers = raw_input('Enter the list of values, separated by comma: ')
list_of_numbers = str_numbers.split(',')
print lucky_sum(list_of_numbers)



