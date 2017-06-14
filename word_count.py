def words(text):
    text = text.replace('\t', ' ') #convert tabs to spaces
    text = text.replace('\n', ' ') #convert new lines to spaces
    tokens = text.split(' ')    #break sentence into words

    getResult = {}              #create an empty dictionary
    for token in tokens:
        if token not in ['', '\n', '\t']: 
            if token not in getResult:
                if token.isdigit():  
                    key = int(token) #convert numbers from string to digits
                else:
                    key = token
                getResult.update({key: tokens.count(token)}) #update the count each times the word appears
    return getResult
print(words("olly olly in come free")) # test    