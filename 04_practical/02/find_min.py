def find_min(list):
    if len(list) == 0:
        return None
    min_val = list[0]
    for num in list:
        if num < min_val:
            min_val = num
    return min_val
