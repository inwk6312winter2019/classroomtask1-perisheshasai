import string
def string_operation():
    myfile = open("book.txt","r")
    punct = string.punctuation
    for my in myfile:
        my = my.strip()
        my = my.replace(" ","\n")
        for c in punct:
           my = my.replace(c,"")
        my = my.lower()
        print(my)
string_operation()
