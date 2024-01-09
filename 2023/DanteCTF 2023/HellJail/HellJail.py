#!/usr/bin/env python3

from string import ascii_letters

code = input('> ')

if any(c in ascii_letters for c in code):
    print('You will never leave this place!')
elif any(c in '.:;,-_@"=/%\\' for c in code):
    print('You will never reach this point, but still, you CANNOT leave!')
else:
    exec(code)
