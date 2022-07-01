import random


class main:
    '''
    Attributes:
        __a (list): It holds the List
    '''
    __a:list
    def __init__(self):
        self.strt()
        self.print_a()
        
        swtch = {'a':self.left,
                 'd':self.right,
                 'w':self.up,
                 's':self.down}

        while True:
            try:
                print("'w' for up\n'a' for left\n'd' for right\n's' for down")
                ch = input("Enter your choice:")
                if ch == 'q':
                    exit()
                self.iszero = False
                swtch[ch]()
                self.random_ch()
                self.print_a()
                state = self.status()
                print(state)
                if state == 'won':
                    print("you won!!!!!!!!!")
                    break
                if state == 'lost':
                    print("you lost!!!")
                    break
            except KeyError:
                print("Try again invalid choice")
            

    def random_ch(self)->None:
        '''
        It chooses a random place to insert the value
        '''
        if not self.iszero:
            return False
        x = random.randint(0,3)
        y = random.randint(0,3)

        while(self.__a[x][y] != 0):
            x = random.randint(0,3)
            y = random.randint(0,3)

        print(x,y)

        self.__a[x][y] = 2



    def strt(self)->None:
        '''
        This function inialises the __a attribute and
        chooses a two random places to inserts the value 
        '''
        self.__a = [[0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0]]
        x = random.randint(0,3)
        y = random.randint(0,3)
        x1 = random.randint(0,3)
        y1 = random.randint(0,3)

        while(x1 == x and y1 == y):
            x1 = random.randint(0,3)
            y1 = random.randint(0,3)

        self.__a[x][y] = 2
        self.__a[x1][y1] = 2


    def print_a(self)->None:
        '''
        This function prints the list
        '''
        for i in self.__a:
            print(i)


    def comp_1(self, ch:str):
        '''
        This function compress the list upwards or
        downwards
        Parameters:
            ch (str): Holds the user's choice
        '''
        for i in range(4):
            c = 0
            temp = list([0]*4)
            chng = False
            if ch == 'u':
                for j in range(4):
                    if self.__a[j][i] != 0:
                        chng = True
                        temp[c] = self.__a[j][i]
                        c += 1
            else:
                for j in range(3,-1,-1):
                    if self.__a[j][i] != 0:
                        chng = True
                        temp[c] = self.__a[j][i]
                        c += 1
            if chng:
                temp = self.merge(temp,ch)
                for c, k in enumerate(temp):
                    self.__a[c][i] = k
                         
                        
                            

    def comp_2(self, ch:str):
        '''
        This function compress the list rightwards or 
        leftwards
        Parameters:
            ch (str): Holds the user's choice
        '''
        for i in range(4):
            c = 0
            temp = list([0]*4)
            chng = False
            if ch == 'l':
                for j in range(4):
                    if self.__a[i][j] != 0:
                        chng = True
                        temp[c] = self.__a[i][j]
                        c += 1
            else:
                for j in range(3,-1,-1):
                    if self.__a[i][j] != 0:
                        chng = True
                        temp[c] = self.__a[i][j]
                        c += 1
            if chng:
                temp = self.merge(temp,ch)
                for c,k in enumerate(temp):
                    self.__a[i][c] = k
                

                
    def merge(self, temp:list, ch:str)->str:
        '''
        This functions merges the two same elements in the 2D list
        Parameters:
            temp (List): The 1D list of 2D list
            ch (Str): The user's choice eg. up, down, right, left 
        '''
        for i in range(3):
            if temp[i] == temp[i+1] and temp[i] != 0:
                temp[i] = temp[i]*2
                temp[i+1] = 0
        a = list([0]*4)
        i = 0        
        for j in temp:
            if j != 0:
                a[i] = j
                i = i+1
        if i <= 3:
            self.iszero = True

        if ch == 'd' or ch == 'r':
            a.reverse()
        del temp

        return a
    

    def status(self)->str:
        '''
        This function returns the status of the game if user has won 
        lost or can continue
        '''
        for i in self.__a:
            for j in i:
                if j == 2048:
                    return 'won'
        
        if self.iszero:
            return 'cont'
        for i in range(4):
            for j in range(3):
                if self.__a[i][j] == self.__a[i][j+1]:
                    return 'cont'

        for i in range(4):
            for j in range(3):
                if self.__a[j][i] == self.__a[j+1][i]:
                    return 'cont'  
        self.iszero = False
        return 'lost'
        

    def up(self)->None:
        '''
        This function moves all the elements in the list
        upwards
        '''
        self.comp_1('u')

    def down(self)->None:
        '''
        This function moves all the elements in the list
        downwards
        '''
        self.comp_1('d')

    def right(self)->None:
        '''
        This function moves all the elements in the list
        towards right side
        '''
        self.comp_2('r')

    def left(self)->None:
        '''
        This function moves all the elements in the list
        towards the left side
        '''
        self.comp_2('l')

a = main()