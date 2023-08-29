from dataclasses import dataclass
from supportedCard import supportedCard
from CQUAD4 import CQUAD4

@dataclass
class quickNastran:
    '''
    This class contains all Nastran cards referenced in the Quick Nastran book
    '''
    _version  : str    = '2012.2'
    cardName  : str    = ''
    CQUAD4    : CQUAD4 = CQUAD4()

    def isNastranCard(self):
        '''
        Method to check if a card is a Nastran card
        '''
        if(hasattr(self, self.cardName)):
            return True
        else:
            return False

    def isSupported(self):
        '''
        Method to check if a card is supported or not
        '''
        if(hasattr(supportedCard(), self.cardName)):
            return True
        else :
            return False


if __name__ == "__main__":
    
    cardName='CQUAD4'
    nastranObject=quickNastran(cardName=cardName)
    
    if(nastranObject.isNastranCard()):
        print(f'{cardName} is a Nastran Card')
    else:
        print(f'{cardName} is not a Nastran Card')


    if(nastranObject.isSupported()):
        print(f'{cardName} is a supported')
    else:
        print(f'{cardName} is not supported')
