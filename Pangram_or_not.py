def Pan(s):
    k='abcdefghijklmnopqrstuvwxyz'
    for i in k:
        if i not in s.lower():
            return False
    return True
s=input()
print(Pan(s))