def decimal_to_binary(n: int) -> str:
    if n == 0:
        return '0b0'
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return '00' + binary
n = int(input("input the number："))
print(decimal_to_binary(n))