def safe_print_list(my_list=[], x=0):
    i = 0
    for item in range(x):
        try:
            i += 1
            print("{}".format(my_list[item]), end="")
        except IndexError:
            break
    print("")
    return (i)
