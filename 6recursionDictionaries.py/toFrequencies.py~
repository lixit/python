def lyrics_to_frequencies(lyrices):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] +=1
        else:
            myDict[word] = 1
    return myDict

def most_common_words(freqs):
    """freqs is a dictionary"""
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

def words_oftene(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

