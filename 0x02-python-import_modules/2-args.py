#!/usr/bin/python3

def main():
    import sys

    n = len(sys.argv)

    if n < 2:
        print("0 arguments.")
        exit()
    print("{:d} arguments:".format(n - 1))
    for i in range(1, n):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == '__main__':
    main()
