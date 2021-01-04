def canCompleteCircuit(A, B):
    start = 0
    index = 1
    tank = 0
    while(start != index):
        if index == 0:
            prev_index = len(A)-1
        else:
            prev_index = index -1
        tank = tank + A[prev_index]
        if(tank >= B[prev_index]):
            tank = tank - B[prev_index]
        else:
            if start<index:
                start = index
                tank = 0
            else:
                return -1
        index = (index+1) % len(A)
    if index == 0:
        prev_index = len(A)-1
    else:
        prev_index = index-1
    tank = tank + A[prev_index]
    if tank>=B[prev_index]:
        return index
    else:
        return -1


print(canCompleteCircuit([959, 329, 987, 951, 942, 410, 282, 376, 581, 507, 546, 299, 564, 114, 474, 163, 953, 481, 337, 395, 679, 21, 335, 846, 878, 961, 663, 413, 610, 937, 32, 831, 239, 899, 659, 718, 738, 7, 209],
                         [862, 783, 134, 441, 177, 416, 329, 43, 997, 920, 289, 117, 573, 672, 574, 797, 512, 887, 571, 657, 420, 686, 411, 817, 185, 326, 891, 122, 496, 905, 910, 810, 226, 462, 759, 637, 517, 237, 884]))
