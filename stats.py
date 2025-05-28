def wordcount(text):
    words = text.split()
    return len(words)
def charcount(text):
    lchars = text.lower()
    lichars = list(lchars)
    coundic = {}
    for ch in lichars:
        if ch in coundic:
            coundic[ch] += 1
        else:
            coundic.update({ch: 1})
    return coundic