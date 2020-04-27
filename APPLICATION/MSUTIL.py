'''
MakerSpace Utility
'''

def stripSingleQuotes(word):
    word = word.strip("'")
    return word

def stripSpecialCharacters(word):
    word = word.replace("*", "")
    word = word.replace(";", "")
    word = word.replace(":", "")
    word = word.replace("\\", "")
    word = word.replace("/", "")
    word = word.replace('"', '')
    word = word.replace("<", '')
    word = word.replace(",", '')
    word = word.replace(">", '')
    word = word.replace("?", '')
    word = word.replace("[", '')
    word = word.replace("{", '')
    word = word.replace("]", '')
    word = word.replace("}", '')
    word = word.replace("|", '')
    word = word.replace("=", '')
    word = word.replace("+", '')
    word = word.replace(")", '')
    word = word.replace("(", '')
    word = word.replace("*", '')
    word = word.replace("_", '')
    word = word.replace("-", '')
    return word



def debugFormat():
    print("==========================================")