# (С) Masahiko AMANO a.k.a. H1K0, 2021

def shichiro_encode(num):
    if num < 256:
        return bin(num)[2:].rjust(8, '0')
    num = bin(num)[2:]
    bitlen = bin(len(num))[2:]
    bits = ''
    if len(bitlen) > 7:
        while len(bitlen) > 7:
            bits += '1' + bitlen[:7]
            bitlen = bitlen[7:]
        bits += bitlen.rjust(8, '0') + bin(len(bitlen))[2:].rjust(8, '0')
    else:
        bits += bitlen.rjust(8, '0')
    bits += num
    return bits


def shichiro_decode(bits):
    if len(bits) <= 8:
        return int(bits, 2)
    if bits[0] == '0':
        bitlen = int(bits[:8], 2)
        bits = bits[8:]
    else:
        bitlen = ''
        while bits[0] == '1':
            bitlen += bits[1:8]
            bits = bits[8:]
        bitlen = int(bitlen + bits[8-int(bits[8:16], 2):8], 2)
        bits = bits[16:]
    num = int(bits[:bitlen], 2)
    return num
