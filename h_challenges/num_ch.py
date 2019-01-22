def count(str):
    if str == "" or str in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
        return 1

    if int(str[0]) * 10 + int(str[1]) <= 26:
        return count(str[1:]) + count(str[2:])
    else:
        return count(str[1:0])


print(count("1221"))

print(count("132"))

print(count("345"))
