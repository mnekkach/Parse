from dataclasses import dataclass

@dataclass
class CQUAD4:
    name           : str  = 'CQUAD4'
    type           : str  = '2D'
    multipleLine   : bool = True
    maxLine        : int  = 1
    
    #First line
    eid        : int             #field12
    pid        : int             #field13
    g1         : int             #field14
    g2         : int             #field15
    g3         : int             #field16
    g4         : int             #field17
    theta      : float           #field18
    zoffs      : float           #field19

    #Second line
    tflags     : int             #field23
    t1         : float           #field24
    t2         : float           #field25
    t3         : float           #field26
    t4         : float           #field27
    
    def set(self, line):
        '''

        '''
        self.eid    = line[0:]
        self.pid    = line[0:]
        self.g1     = line[0:] 
        self.g2     = line[0:] 
        self.g3     = line[0:] 
        self.g4     = line[0:] 
        self.theta  = line[0:]
        self.zoffs  = line[0:]
