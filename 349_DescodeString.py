class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":   #if s[i] is not euqal to close bracket
                stack.append(s[i])  # we append s[i] to stack
            else: # we encountered a closing bracket
                substr = ""  #initialize substring to be empty
                while stack[-1] != "[":   #while stack is not empty and last empty of stack is not an opening bracket
                    substr = stack.pop() + substr #until then,we pop and save it to substring
                stack.pop() #initialize num to be zero

                k ="" #intialize k to be zero
                while stack and stack[-1].isdigit():   #until stack is not empty and last element of stack is digit
                    k = stack.pop()+ k #we pop from the stack and add it to the k
                stack.append(int(k) * substr) #we multiply both substring and convert k to int so that we get the total amount of decode strings
        return "".join(stack) #appending all the decoded srts using .join func
