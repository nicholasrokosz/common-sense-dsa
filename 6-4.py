def contains_X(str):
    for char in str:
        if char == 'X':
            return True

    return False



print(contains_X("wufplwyfuplXywuflpXywuflpwylX"))
print(contains_X("ywfuplwyufplywuflpywuplywufplyup"))
