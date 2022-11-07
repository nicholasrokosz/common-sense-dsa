def index_of_x(str, i=0):
    if str[i].lower() == 'x':
        return i

    return index_of_x(str, i+1)




print(index_of_x('abcdefghijklmnopqrstuvwxyz'))
