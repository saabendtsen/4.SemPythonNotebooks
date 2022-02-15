import string
string.ascii_letters 

class Text_container():

    def __init__(self,text):
        self.text = text

    def printMe(self):
        return self.text

    def countWords(self):
        words = self.text.split(" ")
        print(len(words))
    
    def countChars(self):
        print(len(self.text))

    def countAscii(self):
        letters= []
        for cha in self.text:
            if cha in string.ascii_letters:
                letters.append(cha)

        print(len(letters))

    def removePunctuation(self):
        letters= []
        for cha in self.text:
            if cha not in string.punctuation:
                letters.append(cha)
        print(letters)


if __name__ == '__main__':

    tc = Text_container("test med flere ord!!!!");
    tc.removePunctuation()