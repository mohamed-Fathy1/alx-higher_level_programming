def safe_print_division(a, b):
    result = 0
    try:
        result = (a / b)
    except ZeroDivisionError:
        return (None)
    finally:
        print("Inside result: {}".format(result))
