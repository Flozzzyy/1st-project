def persistence(num:int) -> int:
    counter = 0
    while num >=10:
        product = 1
        for el in str(num):
            product *= int(el)
        num =  product
        counter += 1

    return counter
print(persistence(39))