
# I'm thinking of a number from 0 to 2^32 - 1
# Can you guess it?

import random

def generate(seed):
  random.seed(seed)
  c = 0
  while c != ord('}'):
    c = random.randint(97, 126)
    print(chr(c), end='')
  print()

secret = 'ly9ppw=='

import base64

generate(int(base64.b64decode(secret).hex(), 16))