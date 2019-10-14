def sum_all_even(test_in):
    result = 0

    for i in test_in:
        if i % 2 == 0:
            result += i

    return result

def count_characters(test_senc, characters):
    result = {}

    for i in characters:
        result[i] = 0
        for j in test_senc:
            if i == j:
                result[i] += 1

    return result

def reserve_sentence(test_senc):
    result = []
    for i in test_senc:
        test_senc = i.split(' ')

    for i in range(len(test_senc)-1, -1, -1):
        result.append(test_senc[i])

    result = [' '.join(result)]

    return result

def list_difference(list_1, list_2):
    result = []

    for i in range(len(list_1)):
            result.append(list_2[i] + list_1[i])

    return result

def reserve_list_difference(list_1, list_2):
    result = []

    for i in range(len(list_1)):
        result.append(list_1[-1-i] + list_2[i])
    
    return result
