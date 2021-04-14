counter = 0
ret_list = []


def product_list(list_of_ints, counter):
    result = 1
    temp = []

    for i in list_of_ints:
        temp.append(i)

    if counter < len(temp):
        temp.pop(counter)
        counter += 1

        for i in temp:
            result *= i
        ret_list.append(result)
        product_list(list_of_ints, counter)
    return ret_list


# [1, 2, 3, 4] would return [24, 12, 8, 6] by performing [2x3x4, 1x3x4, 1x2x4, 1x2x3]
print(product_list([1, 2, 3, 4], counter))
