from typing import List

add_bracket = lambda so_far, bracket: [brackets+bracket for brackets in so_far] 

class Solution:
    def helper(self, n: int, parenthesis_so_far: List[str], open_brackets: int) -> List[str]:
        if n == 0 and open_brackets != 0:
            return add_bracket(parenthesis_so_far, ')'*open_brackets)
        
        if open_brackets == 0:
            return self.helper(n-1, add_bracket(parenthesis_so_far, '('), open_brackets+1)

        return (self.helper(n-1, add_bracket(parenthesis_so_far, '('), open_brackets+1) +
            self.helper(n, add_bracket(parenthesis_so_far, ')'), open_brackets-1))
        

    def generateParenthesis(self, n: int) -> List[str]:
        return self.helper(n, [""], 0)

 