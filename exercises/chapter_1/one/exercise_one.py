def rearrange_numbers(l: list):
    l.append(l[1])
    l[1] = l[2]
    l[2] = l[3]
    l[3] = l[0]
    l[0] = l[4]
    l.pop(-1)
    return l
