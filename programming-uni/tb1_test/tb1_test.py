def yearsToBecomeMillionaire(amount):
    interestRate = 0.055
    year = 0
    while amount <1000000:
        amount = amount *(1 + interestRate)
        year = year + 1
    return year

yearsToBecomeMillionaire(0)
