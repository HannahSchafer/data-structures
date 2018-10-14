def first_duplicate(a):
    """return first duplicate in an array"""
    
    i = 0
    seen_set = set()
    
    while i < len(a):
        if a[i] in seen_set:
            return a[i]
        else:
            seen_set.add(a[i])
            i += 1
    return -1
