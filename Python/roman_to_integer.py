def roman_to_integer(string_value: str) -> int:
    roman_constans = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    substractions = ''
    integer_number = 0
    for i in string_value:
        if i in ['V', 'X'] and substractions == 'I':
            integer_number = integer_number - roman_constans.get('I')
            integer_number = integer_number + (roman_constans.get(i) - roman_constans.get('I'))
        elif i in ['L', 'C'] and substractions == 'X':
            integer_number = integer_number - roman_constans.get('X')
            integer_number = integer_number + (roman_constans.get(i) -roman_constans.get('X'))
        elif i in ['D', 'M'] and substractions == 'C':
            integer_number = integer_number - roman_constans.get('C')
            integer_number = integer_number + (roman_constans.get(i) - roman_constans.get('C'))
        else:
            integer_number = integer_number + roman_constans.get(i)
        substractions = i
    return integer_number

if __name__ == "__main__":
    roman_numerals = ['III', 'LVIII', 'MCMXCIV']
    for roman_numeral in roman_numerals:
        result = roman_to_integer(roman_numeral)
        print(f"{roman_numeral} is {result}")