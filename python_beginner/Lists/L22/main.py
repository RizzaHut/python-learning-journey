def filter_messages(messages):
    filtered_dang = []
    dang_index = []

    for i in range(len(messages)):
        words = messages[i].split()
        good_words = []
        dang_counter = 0
        
        for w in words:
            if w == "dang":
                dang_counter += 1
            else:   
                good_words.append(w)
        
        good_word = " ".join(good_words)
        filtered_dang.append(good_word)
        dang_index.append(dang_counter)

    return filtered_dang, dang_index


