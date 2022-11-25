import definitions
import nonpareil

def load(lines):
    # pprint(lines)
    for line in lines:
        print("Adding Line: "+line)
        AddLine(line)
    # pprint(lines)

def AddLine(line):
    deskPop = False
    declarative = "DECLARATIVE HASN'T BEEN DEFINED YET!!"
    sentence = line.split(' ')
    deskPop, declarative, sentence = DeskPop(sentence)
    if(deskPop):
        nonpareil.testAndPop(sentence, ':')
    definitions.Definition(sentence)
        
def DeskPop(sentence):
    locals
    if sentence[0]=="#Definition":
        declarative = "Definition"
        sentence.pop(0)
        return True, declarative, sentence
    else:
        raise TypeError("First word in line given has not been assigned a method: \n "+pprint(sentence))

def testAndPop(sentence, operand):
    if sentence[0]!=operand:
            raise TypeError(OperandIsWrong(sentence, '='))                
    else:
        sentence.pop(0)
        return True

def OperandIsWrong(sentence, operand):
    return "ERROR: '"+ operand +"' \
            is not the first entity in " \
            + toString(sentence) + \
            "when running TestForEquals. \
            Please format nic correctly."


def toString(sentence):
    return ' '.join(sentence)