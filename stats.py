def wordcount(text):
    words = text.split()
    return len(words)
def charcount(text):
    lchars = text.lower()
    lichars = list(lchars)
    coundic = {}
    for ch in lichars:
        if ch.isalpha() == True:
            if ch in coundic:
                coundic[ch] += 1
            else:
                coundic.update({ch: 1})
    ccoundic = sorted(coundic.items(), key=lambda item: item[1], reverse = True)
    return ccoundic
print(charcount("hello i am hungry let me inside i want to eat dinner"))