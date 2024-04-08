def string_valid(parentheses_string: str) -> bool:
    parenthese_values = {
        '(': ')', '{':'}', '[':']'
    }

    len_of_string = len(parentheses_string)
    if len_of_string % 2 != 0:
        return  False
    
    for i in range(0, len_of_string, 2):
        string_valid = parentheses_string[i:i+2]
        if parenthese_values.get(string_valid[0]) != string_valid[-1]:
            return False
        
    return True

if __name__ == "__main__":
    parentheses = ["()", "()[]{}", "(]"]
    for parenthese in parentheses:
        result = string_valid(parenthese)
        print(f"{parenthese} is valid {result}")