# SHICHIRO encoding

__Shichiro__ is kinda XML-based linear binary encoding for integers developed by me. More optimized and flexible modification of [NANAKO encoding](https://github.com/H1K0/NANAKO).

## How it works

Shichiro is a Japanese male name that contains Japanese word 七 (_nana_ or _shichi_) which means "seven".

Firstly, we translate the number into binary and count its length in binary digits or bits. If the length is less than 128, it is being encoded straightly as one byte (_e.g._ 10 => `00001010`). Otherwise, it is being encoded using NANAKO encoding (_e.g._ 192 => `11100000 00000000 00000001`).

Finally, we just write the binary representation of the number bitwisely (__NOT__ bytewisely!).

Examples:

- 1089 => `00001011 10001000001`
- 2^126 + 1 => `01111111 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001`
- 2^127 + 1 => `11000000 00000000 00000001 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001`