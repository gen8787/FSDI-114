def is_anagram(string_a, string_b):
    str_a = string_a.lower().replace(" ", "")
    str_b = string_b.lower().replace(" ", "")

    if len(str_a) != len(str_b):
        return False

    char_times_a = dict()
    char_times_b = dict()

    for i in range(len(str_a)):
        if str_a[i] not in char_times_a.keys():
            char_times_a[str_a[i]] = 0
        else:
            char_times_a[str_a[i]] += 1

        if str_b[i] not in char_times_b.keys():
            char_times_b[str_b[i]] = 0
        else:
            char_times_b[str_b[i]] += 1

    return char_times_a == char_times_b


print(is_anagram("cars", "scaar"))  # False
print(is_anagram("cars", "scar"))  # True
print(is_anagram("I am lord Voldemort", "Tom Marvolo Riddle"))  # True
