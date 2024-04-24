def generateId(ids):
    i = 101
    while i in ids:
        i += 1
    return i
