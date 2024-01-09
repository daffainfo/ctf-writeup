def main():

    flag_enc = ""

    with open("flag.enc.txt", "r") as infile:
        flag = infile.read()
        flag = list(flag)

        for each in flag:
            each = chr(ord(each) ^ 0x66)
            flag_enc += each

    print(flag_enc)

if __name__ == "__main__":
    main()