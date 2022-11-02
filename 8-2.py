from collections import defaultdict

def find_dupe(arr):
    hash_table = defaultdict(list)

    for item in arr:
        if hash_table[item] == 1:
            return item
        else:
            hash_table[item] = 1


print(find_dupe(['a', 'b', 'c', 'd', 'c', 'e', 'f']))
