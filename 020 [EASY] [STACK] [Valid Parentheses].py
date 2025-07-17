class Solution:
    def isValid(self, s: str) -> bool:

        '''
        Steps
        1) If paren is an opening, insert into stack
        2) If paren is closing, pop from stack
        3) If items dont match OR stack isn't empty at false, return False
        4) Otherwise, return True
        '''

        stack = []
        opens = '({['

        for item in s:
            if item in opens:## If its an opening
                stack.append(item)
            else: ## If its a closing
                if len(stack) == 0:
                    return False
                else:
                    removedItem = stack.pop()

                if removedItem == '(' and item != ')':
                    return False
                elif removedItem == '[' and item != ']':
                    return False
                elif removedItem == '{' and item != '}':
                    return False
        return len(stack) == 0