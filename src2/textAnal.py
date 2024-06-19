givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

# Let's create a class called TextAnalyzer to analyze text.
class TextAnalyzer(object):
    # The __init__ method initializes the class with a 'text' parameter.
    # You will store the provided 'text' as an instance variable.
    def __init__(self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        # make text lowercase
        formattedText = formattedText.lower()

        self.fmtText = formattedText

    def freqAll(self): 
        wordList = self.fmtText.split(' ')
        freqMap = {}
        for word in set(wordList): #use set to remove duplicates
                freqMap[word] = wordList.count(word)
        return freqMap
        
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
            
# Create an object of the class and pass the text to the constructor.
analyzer = TextAnalyzer(givenstring)
# Call the freqAll method to get the frequency of all words in the text.
print("Formatted Text:", analyzer.fmtText)
freqMap = analyzer.freqAll()
print(freqMap)


word = "lorem"
frequency = analyzer.freqOf(word)
print("The word",word,"appears",frequency,"times.")


print(analyzer.freqAll())
# Call the freqOf method to get the frequency of a word in the text.
print(analyzer.freqOf('diam'))
print(analyzer.freqOf('lorem'))
print(analyzer.freqOf('et'))