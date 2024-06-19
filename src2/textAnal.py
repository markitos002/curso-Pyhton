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