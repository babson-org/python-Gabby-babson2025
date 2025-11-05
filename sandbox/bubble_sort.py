def bubble_sort(values):
    sorted = values.copy()
    size = len(sorted)

    for pass_num in range(size - 1):
        swaps = False
        for idx in range(size - 1 - pass_num):
            if sorted[idx] > sorted[idx + 1]:
                sorted[idx], sorted[idx + 1] = sorted[idx + 1], sorted[idx]
                swaps = True
        if not swaps: break

    return(sorted)