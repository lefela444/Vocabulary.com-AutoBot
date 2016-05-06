import random
import string
import time
import os
import platform
usr = os.getenv('username')[2]
base = platform.uname()[0][0]

_authour_ = "Sayan Bhowmik"

#+++++++++++++++++++++++++++++++++++++++++++++#
           # The Infamous KeyGen #
#+++++++++++++++++++++++++++++++++++++++++++++#
# KeyGen is not required now


def key_gen(z):
    strg = random.choice(string.ascii_uppercase)
    num = random.choice(string.digits)
    final = ""
    for i in range(z):
        final = final + ''.join(random.choice([strg, num]))
        strg = random.choice(string.ascii_uppercase)
        num = random.choice(string.digits)

    print final + usr + base

# To make 10 digit key use "8" as parameter (n-2)
key_gen(8)
time.sleep(5)
