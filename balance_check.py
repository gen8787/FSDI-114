def balance_check(s):
    if len(s) % 2 != 0:
        return False

    opening = set("([{")
    matches = set([("")])
