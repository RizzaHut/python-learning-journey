def find_longest_word(document: str, longest_word: str = "") -> str:
    # base case
    if document == "" or document == " ":
        return longest_word
    # make data smaller
    words = document.split(maxsplit=1)
    current_word = words[0]
    if len(words) > 1:
        rest_of_words = words[1]
    else: 
        rest_of_words = ""

    if len(current_word) > len(longest_word):
        current_longest_word = current_word
    else: 
        current_longest_word = longest_word

    # recursive step
    return find_longest_word(rest_of_words, current_longest_word)
