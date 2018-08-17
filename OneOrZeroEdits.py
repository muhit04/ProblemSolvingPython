# Source: Cracking the coding interview 6th Edition
# Problem 1.5: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, pIe -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

class OneAway:
    def __init__(self, input_str: str):
        self.input_str = input_str

    def get_hash_val(self):
        hash_tbl = {}
        for inp in self.input_str:
            if not inp in hash_tbl:
                hash_tbl[inp] = 1
            else:
                hash_tbl[inp] += 1

        return hash_tbl

if __name__ == "__main__":

    o1 = OneAway('pale')
    o2 = OneAway('bale')
    set_one = set(o1.get_hash_val().items())
    set_two = set(o2.get_hash_val().items())

    set_length = len(set_one - set_two)

    if set_length > 1:
        print("false")
    else:
        print("true")

# Time complexity: O(n)