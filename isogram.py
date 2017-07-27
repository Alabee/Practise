def is_isogram(word):
    ded = list(word)
    slice = 1
    tuple = (word, True)
    count = 1
    if word == "":
        tuple = ("", False)
    
    elif type(word) is not str:
        tuple = "Argument should be a string"

    else:
        while slice < len(word):
            for char in ded:
                for character in ded[slice:]:
                    if character is char:
                        tuple = (word, False)
                        break
                    slice +=1
                count += 1
                slice = count
            

    return tuple
        

print(is_isogram(""))
