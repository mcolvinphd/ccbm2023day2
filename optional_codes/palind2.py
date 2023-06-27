def palind2(s):
    alist=list(s)
    alist.reverse()
    revs="".join(alist)
    if revs==s:
        return True
    return False
print(palind3("madammimadam"))
print(palind3("madamimadam"))
print(palind3("ratsliveonnoevilstar"))
print(palind3("amanaplanacanalpanama"))