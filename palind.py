##def palind(s):
##    rev=""
##    for i in s:
##        rev=i+rev
##    if rev==s:
##        return True
##    return False
##
##print(palind("madammimadam"))
##print(palind("madamimadam"))
##print(palind("ratsliveonnoevilstar"))
##
def palind2(s):
    alist=list(s)
    alist.reverse()
    revs="".join(alist)
    if revs==s:
        return True
    return False

print(palind2("madammimadam"))
print(palind2("madamimadam"))
print(palind2("ratsliveonnoevilstar"))
