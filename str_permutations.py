def permutations(word):

    if len(word) == 1:
        return word

    perms = permutations(word[1:])
    char = word[0]
    result = []

    for i in perms:
        for j in range(len(i)+1):
            result.append(perms[:j] + char + perms[j:])

    return result


test = 'lse'

print(permutations(test))
