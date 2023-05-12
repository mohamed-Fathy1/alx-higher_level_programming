#!/usr/bin/python3

def main():
    import sys
    argc = len(sys.argv)

    sum = 0
    for i in range(1, argc):
        sum += int(sys.argv[i])
    print("{:d}".format(sum))


if __name__ == '__main__':
    main()
