

if __name__ == "__main__":
    s1 = input("String 1: ")
    s2 = input("String 2: ")
    ans = ""

    for character in s1:
        if character in s2:
            ans += character

    print(ans)

