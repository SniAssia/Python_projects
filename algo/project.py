def show_possible_matches(my_word):
    permutations = []
    def helper(my_word, permutation):
        if len(my_word) == 0:
            permutations.append(permutation)
            return
        for i in range(len(my_word)):
            new_word = my_word[: i] + my_word[i + 1:]
    helper(my_word, "")
    return permutations
print(show_possible_matches())

