def find_first_non_dupe(str):
    hash_table = {}

    for char in str:
        if char not in hash_table:
            hash_table[char] = 1
        else:
            hash_table[char] += 1

    for char in str:
        if hash_table[char] == 1:
            return char


print(find_first_non_dupe("minimum"))
