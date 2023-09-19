spam = ['apples', 'bananas', 'tofu', 'cats']

def concatAndCommas(list):
    if len(list) == 0:
        return 'Empty list!'
    elif len(list) == 1:
        return list[0]
    else:
        return ', '.join(list[:-1]) + ', and ' + list[-1]
    

print(concatAndCommas(spam))