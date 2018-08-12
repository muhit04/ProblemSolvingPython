# Write a function that given a list of non negative integers, 
# arranges them such that they form the largest possible number. 
# For example, given [50, 2, 1, 9], the largest formed number is 95021.
# Problem Source: https://bit.ly/1XKQugm

class LargestNumber:
    def __init__(self, numbers_list: list):
        self.no_list = numbers_list

    def single_digit_desc_sort(self):
        self.no_list.sort(reverse=True)
        for index, ls in enumerate(self.no_list):
            if (index + 1) == len(self.no_list):
                return self.no_list

            elif int(str(ls)[0]) < self.no_list[index+1]:
                tmp = self.no_list[index+1]
                self.no_list[index+1] = ls
                self.no_list[index] = tmp

    def get_result(self):
        new_list = self.single_digit_desc_sort()
        result = ''
        for ls in new_list:
            result += str(ls)

        return result