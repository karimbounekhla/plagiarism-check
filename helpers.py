def lines(a, b):
    """Return lines in both a and b"""
    alist = set(a.split("\n"))
    blist = set(b.split("\n"))

    return list(alist & blist)

from nltk.tokenize import sent_tokenize

def sentences(a, b):
    """Return sentences in both a and b"""

    alist = set(sent_tokenize(a))
    blist = set(sent_tokenize(b))
    return list(alist & blist)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    alist = set()
    blist = set()

    for x in range(len(a) - n + 1):
        alist.add(a[x:x+n])
    for y in range(len(b) - n + 1):
        blist.add(b[y:y+n])

    return list(alist & blist)
