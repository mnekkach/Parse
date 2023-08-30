from dataclasses import dataclass
from keyWords import keyWords
from quickNastran import quickNastran


@dataclass
class Parser:
    file : str = ""
    linesNotSupported = []
    newLine : str = ""

    def parse(self):
        beginBulk=False

        with open(self.file, 'r') as bulk:
            for lines in bulk:
                if(self.newLine != ""):
                    line=self.newLine.rstrip()
                    self.newLine=""
                else:
                    line=lines.rstrip()
                
                if(self.isBeginBulk(line)):
                    beginBulk=True
                
                if(beginBulk):
                    cardName=line[0:8].strip()
                    nastranCard = quickNastran(cardName=cardName)
                    
                    if(self.isEmptyLine(line) or self.isCommentLine(line)):
                        #TODO : Check if a line can start with space if it is not a multipleLine of a card
                        pass
                    
                    elif(cardName==keyWords._INCLUDE.value):
                        print(f'INCLUDE LINE : {line}')
                    
                    elif(nastranCard.isNastranCard() and nastranCard.isSupported()):
                        print(line)
                        cardObject=getattr(nastranCard,  cardName)
                        print(cardObject)
                        if(cardObject.multipleLine):
                            #Parse the first line
                            cardObject.parse(line)
                            #Parse the multiple lines
                            i=0
                            while(i < cardObject.maxLine):
                                i+=1
                                nextLine=next(bulk, '')
                                if(nextLine.startswith(' ')):
                                    cardObject.parse(line)
                                    print(nextLine.rstrip())
                                else:
                                    self.newLine=nextLine
                        else :
                            #TODO : Parser the cardObject
                            cardObject.parse(line)
                            pass
                    
                    else:
                        self.linesNotSupported.append(line + '/n')
    
    def isEmptyLine(self, line):
        '''
        Method to check if a line is empty or not
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
