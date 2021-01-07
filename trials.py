import os
from pathlib import Path


f = open("output.txt", "w", encoding="latin_1")
f.write('\n')
f.close()
f = open("output.txt", "r", encoding="latin_1")
if f.read(1) =='\n':
    print("a7a")
print(len(f.read(1)))

# for i in range(256):
#
#     c = chr(i)
#     f.write(c)
#     f.close()
#     print(i, Path('output.txt').stat().st_size)
