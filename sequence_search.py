def sequence_search(list, target):
    for i in range(len(list)):
        if target == list[i]:
            return i
    return None


if __name__ == "__main__":
    print(sequence_search([99, 12, 33, 74, 521, 13, 14], 521))
