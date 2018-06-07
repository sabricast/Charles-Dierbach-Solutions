# Write a function called palindromeChecker using iteration to return True if a
# provided string is a palindrome, and False otherwise. Make sure to include
# docstring specification for the function.

def palindromeChecker(s):

    """ Returns True if the provided string is a palindrome.
        Uses the stack Module (added in this directory) and the Let's Apply it section from the chapter.
    """

    import stack

    # init
    char_stack = stack.getStack()

    while s != '':
        if len(s) == 1:
            return True
        else:
            # init
            is_palindrome = True

            # to handle strings of odd length
            compare_length = len(s) // 2

            # push second half of input string on stack
            for k in range(compare_length, len(s)):
                stack.push(char_stack, s[k])

            # pop chars and compare to first half of string

            k = 0
            while k < compare_length and is_palindrome:
                ch = stack.pop(char_stack)
                if s[k].lower() != ch.lower():
                    is_palindrome = False

                k = k + 1

            # return values
            if is_palindrome:
                return True
            else:
                return False
