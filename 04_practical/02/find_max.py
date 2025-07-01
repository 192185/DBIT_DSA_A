def find_max(list):
    if len(list) == 0:
        return None
    max_val = list[0]
    for num in list:
        if num > max_val:
            max_val = num
    return max_val