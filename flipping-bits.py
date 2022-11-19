# -------------------------------------------------#
# -----------flipping_bits_(see_notes)-------------#
# -------------------------------------------------#
def flippingBits(n):
    # convert decimal to 32bit binary
    result = format(n, '032b')
    print(result)
    # flip the 32bit binary bits
    flip_bits = ''
    for i in result:
        if i == '0':
            flip_bits += '1'
        else:
            flip_bits += '0'
    print(flip_bits)

    # convert binary to decimal
    return (int(flip_bits, 2))


binary_to_decimal = flippingBits(9)
print(binary_to_decimal)
