# 1. Print Numbers from 1 to N
def one_to_nNumbers(n):
    # Base Case
    if n == 0:
        return
    one_to_nNumbers(n-1) # recursive case
    print(n)
one_to_nNumbers(5)    