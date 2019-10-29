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

def extract_keys_with_numbers(input_values):
  result = []

    for key, value in input_value.items():
        for char in value:
            try:
                int(char)
                result.append(key)
                break
            except Exception:
                continue
    return result

def merge_dicts(input_in):
    result = {}

    for input_value in values_in:
        print("Current dict is {}".format(input_value))
        for key, value in input_value.items():
            print("Current dict key is {} and value is {}".format(key, value))
            print("Results is currently {}".format(result))
            if key in result:
                print("Key {} is in the results".format(key))
                if result[key] != input_value[key]:
                    print("Key is on conflict as result value is {} and current dict value is {}".format(result[key], input_value[key]))
                    result[key] = "conflict"
            else:
                print("Key is not results so add key {} with value {}".format(key, value))
                result[key] = input_value[key]
            print("++++++++++++++++++++++++++++++++++")
        print()
        print("--------------------------------------")

    return result
