import random
key = open('key.txt').read()
random.seed(2023)
enc_key = ""

for j in range(8):
    i = 0
    lst = []
    while i < len(key):
        lst.append(key[i+j])
        i += 8

    random.shuffle(lst)
    for c in lst:
        enc_key += c

print("this may be helpful:")
print(enc_key)



blacklist = [
    "import",
    "os",
    "sys",
    "ls",
    "cat",
    "la",
    "flag",
    "tac",
    "key",
]

strictly_prohibited = [
    "apt",
    "install",
    "cd",
    "builtins",
    "subprocess",
    "exec",
    "eval",
    "input",
    "blacklist",
    "strictly_prohibited",
    "echo",
    "grep",
    "find",
    "pickle",
    "key",
    "write"
]

while True:
    cmd = input(">>> ")
    evl_cmd = eval(cmd)
    can_run = True
    for word in strictly_prohibited:
        if word in evl_cmd.lower():
            can_run = False
            break

    if can_run:
        if evl_cmd[0:len(key)] == key:
            exec(evl_cmd[len(key):])
        else:
            for word in blacklist:
                if word in evl_cmd.lower():
                    can_run = False
                    break

            if can_run:
                exec(evl_cmd)