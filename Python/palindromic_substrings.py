class Solution:
    def countSubstrings(self, s: str) -> int:
        sub_string_count = len(s)
        def _possible_substrings(first_string: str, remaining_string: str) -> None:
            nonlocal sub_string_count
            if not remaining_string:
                return None
            substring = first_string + remaining_string
            if substring == substring[::-1]:
                sub_string_count +=1
            return _possible_substrings(first_string, remaining_string[:-1])
        
        for index, value in enumerate(s):
            _possible_substrings(value, s[index+1:])

        return sub_string_count



if __name__ == "__main__":
    solution_instance = Solution()
    test_01 = solution_instance.countSubstrings("abc")
    test_02 = solution_instance.countSubstrings("aaa")
    print(f"test 01 {test_01} test 02 {test_02}")