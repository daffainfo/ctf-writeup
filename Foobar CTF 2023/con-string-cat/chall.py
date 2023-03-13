flag = open('flag.txt').read()

class foobar:
    def __init__(self, uname):
        self.uname = uname

    def display(self):
        print(self.uname)



foo = foobar("welcome_to_foobarctf")


def resolver(template, resolv):
    return template.format(param = resolv)



text = "This is for u :) {param}"

offset = int(input("enter the offset: "))
string_to_insert = input("enter string to insert: ")

if offset > len(text):
    print("invalid input")
else:
    text = text[0:offset] + string_to_insert + text[offset:]
    print(resolver(text, foo))