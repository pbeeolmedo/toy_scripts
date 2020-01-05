def asc_order(input_list = None):
    '''
    Order a list of 3 integers in ascending order.
    '''
    if (input_list is None) or len(input_list) != 3:
        return None

    a,b,c= input_list
    ordered_list = [0]*len(input_list)

    a_index = (a>=b) + (a>=c)
    b_index = (b>a) + (b>=c)
    c_index = (c>a) + (c>b)


    ordered_list[a_index] = a
    ordered_list[b_index] = b
    ordered_list[c_index] = c

    return ordered_list


sample_list = [50,'2',0]
print(asc_order(sample_list))