


if __name__ == "__main__":
    s1 = input("First string: ")
    s2 = input("Second string: ")

    if (s1.find(s2) == -1):
        print("Couldn't find your friend!")

    else:
        print("Found {0} in the position {1}".format(s2, s1.find(s2)))
