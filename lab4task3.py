import string
def string_operation():
    myfile = open("book.txt","r")
    punct = string.punctuation
    hist = dict()
    counter = 0
    listofwords = []
    for my in myfile:
        my = my.strip()
        for c in punct:
           my = my.replace(c,"")
        my = my.lower()
        lis = my.split()
        for li in lis:
            listofwords.append(li)
    for lists in listofwords:
        if lists not in hist:
            hist[lists] = 1
        else:
            hist[lists] += 1
    for key, value in histo.items():
        if(value == 20):
            print(key)

string_operation()

