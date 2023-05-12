#!/usr/bin/python3

def main():
    from calculator_1 import add, sub, mul, div
    import sys

    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    oper = sys.argv[2]
    b = int(sys.argv[3])

    if oper == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif oper == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif oper == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif oper == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if __name__ == '__main__':
    main()
