def variable_byte_encode(n):
    b = []
    while 1:
        if len(b) == 0:
            b.append(bin(n % 128 + 128))
        else:
            b.append(bin(n % 128))
        n //= 128
        if n == 0:
            break
    return b

test = variable_byte_encode(2456785423)

print(test)