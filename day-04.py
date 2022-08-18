#!/usr/bin/python3
import hashlib

def five_zeros(digits):
    if digits[0] == '0' and digits[1] == '0' and digits[2] == '0' and digits[3] == '0' and digits[4] == '0':
        return True
    else:
        return False

def find_five_zero_hash(secret_key):
    x = 1
    while True:
        result = hashlib.md5((secret_key + str(x)).encode())
        digits = result.hexdigest()
        if five_zeros(digits):
            break
        else:
            x += 1
    return x

#####################

def test_find_five_zero_hash():
    assert find_five_zero_hash('abcdef') == 609043
    assert find_five_zero_hash('pqrstuv') == 1048970

#####################

# Part 1
test_find_five_zero_hash()
number = find_five_zero_hash('bgvyzdsv')
print("Part 1: the lowest positive number is " + str(number))
