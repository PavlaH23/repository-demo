def fizzbuzz(n):
    if n <= 0:
        raise ValueError('n is not positive')
    #pokud to neni integer vyhod typeerror
    if not isinstance(n, int):
        raise TypeError("n is not an int")
    #nebo jen deleno 15
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    if n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    return str(n)
