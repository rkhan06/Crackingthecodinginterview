

def urlify(s, size):
    l = list(s)
    for i in range(size):
        if l[i] == " ":
            l[i] = "%20"
    return "".join(l)


if __name__ == "__main__":
    n = input()
    size = int(input())
    res = urlify(n, size)
    print(res)