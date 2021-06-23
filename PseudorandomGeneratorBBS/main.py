# BBS

import os
import zipfile
import sympy
from datetime import datetime


def generate_large_prime():
    current_prime = sympy.randprime(2 ** 511, 2 ** 1024)
    while current_prime % 4 != 3:
        current_prime = sympy.randprime(2 ** 511, 2 ** 1024)
    return current_prime


def bit_freq(bit_out):
    freq = {}
    for i in range(len(bit_out)):
        if bit_out[i] in freq:
            freq[bit_out[i]] += 1
        else:
            freq[bit_out[i]] = 1
    for i in freq:
        print(i + ": " + str((freq[i] * 100 / len(bit_out))) + "%")


def current_time_to_seconds():
    current_time = datetime.now().time()
    in_seconds = current_time.second + current_time.minute * 60 + current_time.hour * 3600
    return in_seconds


def write_file(filename, bit_out):
    file = open(filename, "w")
    file.write(bit_out)
    file.close()


def compress_file(filename):
    file = zipfile.ZipFile(filename + ".zip", "w")
    file.write(filename, compress_type=zipfile.ZIP_DEFLATED)
    file.close()


def main():
    bit_out = ""
    p = generate_large_prime()
    q = generate_large_prime()
    while p == q:
        q = generate_large_prime()
    n = p * q

    seed = current_time_to_seconds()
    x0 = (seed ** 2) % n
    for i in range(2 ** 20):
        bit_res = str(x0 % 2)
        x0 = (x0 ** 2) % n
        bit_out += bit_res
    print(bit_out)
    bit_freq(bit_out)

    write_file("bbs.txt", bit_out)
    file_size = os.path.getsize("bbs.txt")
    compress_file("bbs.txt")
    file_compressed_size = os.path.getsize("bbs.txt.zip")
    print("Size file before compression: " + str(file_size))
    print("Compressed file: " + str(file_compressed_size))

    just_ones = ""
    for i in range(2 ** 20):
        just_ones += (str(1))

    write_file("ones.txt", just_ones)
    file_size = os.path.getsize("ones.txt")
    compress_file("ones.txt")
    file_compressed_size = os.path.getsize("ones.txt.zip")
    print("Size file before compression: " + str(file_size))
    print("Compressed file: " + str(file_compressed_size))


if __name__ == '__main__':
    main()
