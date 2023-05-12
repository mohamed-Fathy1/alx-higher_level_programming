#!/usr/bin/python3

def main():
    import sys

    n = len(sys.argv)

    if n == 1:
        print("0 arguments.")
        sys.exit(1)

    print("{:d} argument:".format(n - 1))
    for i in range(1, n):
        print("{:d}: {}".format(i, sys.argv[i]))


if __name__ == '__main__':
    main()
