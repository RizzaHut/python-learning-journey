def reverse_list(items):
    reverse_list = []
    for i in range(len(items)-1,-1,-1):
        item = items[i]
        reverse_list.append(item)
    return reverse_list
    
         
