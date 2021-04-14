return_string = []
counter = 0


def reverse_recursive(string, counter):

    while len(return_string) != len(string):
        return_string.insert(0, string[counter])
        counter += 1
        reverse_recursive(string, counter)

    else:
        output = ""

        for char in return_string:
            output += char
        return output


print(reverse_recursive("reverse me", counter))
