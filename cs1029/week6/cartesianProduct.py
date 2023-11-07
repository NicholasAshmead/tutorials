def cartesianProduct(set1, set2):
    result = []
    for i in set1:
        for j in set2:
            result.append((i, j))
    return result
