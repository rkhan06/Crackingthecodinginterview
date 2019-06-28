

def string_compression(s):
    l = list()
    count = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            l.append(s[i])
            l.append(str(count))
            count = 1
    l.append(s[len(s)-1])
    l.append(str(count))
    if len(l) < len(s):
        return "".join(l)
    else:
        return s


if __name__ == '__main__':
    print(string_compression(input()))