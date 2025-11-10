def has_adjacent_duplicate(L):
    if not isinstance (L,list):
        return False
    if len(L) < 2:
        return False
    for i, value in enumerate (L[:-1]):
        if value == L[i + 1]:
            return True
    return False 
        
    