def safe_print_list(my_list=[], x=0):
    i = 0
    for item in my_list:
        try:
            if i > x:
                raise IndexError
            i += 1
            print("{:d}".format(item), end="")
        except IndexError:
            break
    print("")
    return (i)
