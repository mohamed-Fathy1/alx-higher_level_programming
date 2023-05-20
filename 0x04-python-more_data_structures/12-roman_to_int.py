#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    result = 0

    for i, val in enumerate(roman_string):
        if i < len(roman_string) - 1:
            if ((val == 'I' and roman_string[i + 1] in ('X', 'V'))
                    or (val == 'X' and roman_string[i + 1] in ('L', 'C'))
                    or (val == 'C' and roman_string[i + 1] in ('D', 'M'))):
                result -= dic[val]
                continue

        result += dic[val]

    return (result)
