import re


def check(word, n, k):
    pattern = "(.{{{},}}?)".format(n) + "\\1" + "{{{}}}".format(k)
    print(pattern)
    r = re.compile(pattern)
    if r.search(word):
        print(0)
        return 0
    else:
        print(1)
        return 1


check("ABABABABBCCEF", 3, 2)
