from dataclasses import dataclass
from keyWords import keyWords
from quickNastran import quickNastran


@dataclass
class Parser:
    file : str = ""

    def parse(self):
        beginBulk=False

        with open(self.file, 'r') as bulk:
            for lines in bulk:
                line=lines.strip()
                
                if(self.isBeginBulk(line)):
                    beginBulk=True
                
                if(beginBulk):
                    cardName=line[0:8].strip()
                    nastranCard = quickNastran(cardName=cardName)
                    
                    if(self.isEmptyLine(line) or self.isCommentLine(line)):
                        pass
                    
                    elif(cardName==keyWords._INCLUDE.value):
                        print(f'INCLUDE LINE : {line}')
                    
                    elif(nastranCard.isNastranCard() and nastranCard.isSupported()):
                        print(line)
                    
                    else:
                        print(f'{line} : It is a wrong line')
    
    def isEmptyLine(self, line):
        '''
        Method to check il a line is empty or not
        '''
        if(len(line.strip())==0):
            return True
        else:
            return False


    def isCommentLine(self, line):
        '''
        Method to check if a line is a commented line
        '''
        if(line.startswith('$')):
            return True
        else:
            return False


    def isBeginBulk(self, line):
        if(line[0:10]==keyWords._BEGIN_BULK.value):
            return True
        else:
            return False



if __name__ == "__main__":
    bulkFile='./RUN101_KBR_UL_3c100.dat'
    parse=Parser(bulkFile)
    parse.parse()
