from collections import defaultdict

def list_intersection(arr1, arr2):
    hash_table = defaultdict(list)
    intersection = []

    if len(arr1) >= len(arr2):
        bigger_list = arr1
        smaller_list = arr2
    else:
        bigger_list = arr2
        smaller_list = arr1
    
    for item in bigger_list:
        hash_table[item] = True

    for item in smaller_list:
        if hash_table[item]:
            intersection.append(item)

    return intersection



print(list_intersection([1, 2, 3, 4, 5], [0, 2, 4, 6, 8]))
