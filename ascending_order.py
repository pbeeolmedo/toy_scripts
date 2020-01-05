# order a list of 3 integers in ascending order 

def asc_order(input_list = None):
    if input_list is None:
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


sample_list = [50,20,0]

print(asc_order(sample_list))