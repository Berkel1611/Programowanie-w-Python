def isIdValid(id):
    return bool(id.isdigit())


def isIdUnique(id, ids):
    return id in ids
