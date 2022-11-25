import nonpareil

allDefinitions = {}

def Definition(sentence):
    DefinedWord = sentence.pop(0)
    nonpareil.testAndPop(sentence, "=")
    definition = {DefinedWord: {"Definition": nonpareil.toString(sentence)}}
    print("The definition of "+DefinedWord+" is '"+nonpareil.toString(sentence)+"'")
