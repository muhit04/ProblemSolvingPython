# Take an input string parameter and determine if exactly 3 question marks 
# exist between every pair of numbers that add up to 10. If so, return true, 
# otherwise return false. Some examples test cases are below:
# "arrb6???4xxbl5???eee5" => true
# "acc?7??sss?3rr1??????5" => true
# "5??aaaaaaaaaaaaaaaaaaa?5?5" => false
# "9???1???9???1???9" => true
# "aa6?9" => false
# Source url: https://bit.ly/2qYZjxc


class ThreeQuestionMarks:
    def __init__(self, input_str: str):
        self.input_str = input_str

    #TODO: Refactor the code in to fewer lines.
    def count_q_marks(self):
        result = 0
        count_marks = 0
        flag = False
        for i in self.input_str:
            try:
                result += int(i)
                if result == 10:
                    if count_marks == 3:
                        flag = True
                        result = int(i)
                        count_marks = 0
                    else: flag = False
            except ValueError:
                if i == '?' and result > 0:
                    count_marks += 1
                else: continue
        return flag