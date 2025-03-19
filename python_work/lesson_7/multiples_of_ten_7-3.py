# PRACTICE CHAPTER 7 | 1/12/25 #
# MULTIPLES OF TEN #

number = int(input('Give me a number. ')) # PROMPT USER FOR A NUMBER AND CONVERT TO INT #
if number % 10 == 0:
    print(f'You gave me the number {number}, which is a multiple of 10!')
else:
    print(f'You gave me the number {number}, which is not a multiple of 10!')