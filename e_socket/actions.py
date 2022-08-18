
def str_to_list(text: str,key=' '):
    message = []
    val = 0
    for letter in range(len(text)):
        if text[letter] != key:
            if len(message) == val:
                message.append(text[letter])
            else:
                message[val] += text[letter]
        else:
            message.append('')
            val += 1
    return message