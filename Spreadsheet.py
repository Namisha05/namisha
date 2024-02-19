#===================================

class Spreadsheet:
    def __init__(self):
        '''
        Predefined member variables. 
        
        WARNING:DO NOT MODIFY THE FOLLOWING VARIABLES
        '''
        self.sheet = None   # 2D array of values
        self.rows = 0       
        self.cols = 0
        self.cursor=[0,0]   # cursor's current position
        self.selection = [None, None, None, None]
        
        #======================
        # Insert your Member
        #   variables here (if any):
        #----------------------
        
        self.selectedvals = []   #list that stores all selected positions
        #======================
        
#======================
    def CreateSheet(self, rows, cols):
        '''
        Creates a new 2 dimensional array assigned
          to the self.sheet member variable.
        Initialize the 2D array with 'None' type.
 
        Parameters:
            rows --> total number of rows in this spreadsheet
            cols --> total number of cols in this spreadsheet
        
        Return value:
            None
        '''
        self.sheet = [[None]*cols for i in range(rows)]
        self.rows = rows
        self.cols = cols
#======================

#======================
    def Goto(self, row, col):
        '''
        Moves the cursor to the location indicated by the 
          row and col parameters
 
        Parameters:
            row --> row number to move to
            col --> column number to move to
        
        Return value:
            None
        '''
        self.cursor = [row,col]
#======================

#======================        
    def Insert(self, val):
        '''
        Inserts value at the position indicated by the cursor.
 
        Parameters:
            val --> value to be inserted at the cursor location
        
        Return value:
            None
        '''
        
        self.sheet[self.cursor[0]][self.cursor[1]] = val
#======================

#======================        
    def Delete(self):
        '''
        Deletes a value from the position indicated by the cursor.
 
        Parameters:
            None
        
        Return value:
            None
        '''

        self.sheet[self.cursor[0]][self.cursor[1]] = None 
#======================

#======================    
    def ReadVal(self):
        '''
        Prints the value from the position indicated by the cursor.
 
        Parameters:
            None
        
        Return value:
            value stored at the cursor location 

        '''
        
        print(self.sheet[self.cursor[0]][self.cursor[1]])
#======================

#======================    
    def Select(self,row, col):   
        '''
        Selects values between the position indicated in arguments with row and col and the position indicated by the cursor
 
        Parameters:
            row --> Row number to be selected 
            col --> Column number to be selected
        
        Return value:
            None
        '''
        #storing range of selection
        self.selectedvals = []
        self.selection[0] = self.cursor[0]
        self.selection[1] = self.cursor[1]
        self.selection[2] = row
        self.selection[3] = col
        
        #storing all positions between selection in self.selectedvals
        for i in range(self.cursor[0],row+1):
            for j in range(self.cursor[1],col+1):
                self.selectedvals.append((i,j))
#======================

#======================        
    def GetSelection(self):
        '''
        Returns a tuple with current selecion cooridnates
        Parameters:
            None
        
        Return value:
            Returns a tuple with row and column of the selection:
                position 1 of the tuple indicates the stating row of the selection
                position 2 of the tuple indicates the stating col of the selection
                position 3 of the tuple indicates the ending row of the selection
                position 4 of the tuple indicates the ending col of the selection
            
            Example: (1,1,3,4)
        '''
        
        return (self.selection[0],self.selection[1],self.selection[2],self.selection[3])
#======================

#======================        
    def Sum(self,row,col):
        '''
        Stores the sum of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the sum
            col --> Column number to store the sum
        
        Return value:
            None
        '''
        
        self.sheet[row][col] = sum([self.sheet[i[0]][i[1]] for i in self.selectedvals if self.sheet[i[0]][i[1]] != None])
#======================

#======================    
    def Mul(self,row,col):
        '''
        Stores the product of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the product
            col --> Column number to store the product
        
        Return value:
            None
        '''   
        newlst=[self.sheet[i[0]][i[1]] for i in self.selectedvals if self.sheet[i[0]][i[1]] != None]
        product = 1
        for i in newlst:
            product = product*i
        self.sheet[row][col] = product
#======================

#======================        
    def Avg(self,row,col):
        '''
        Stores the average of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the average
            col --> Column number to store the average
        
        Return value:
            None
        '''
        newlst=[self.sheet[i[0]][i[1]] for i in self.selectedvals if self.sheet[i[0]][i[1]] != None]
        self.sheet[row][col] = (sum(newlst)/len(newlst))
#======================

#======================
    def Max(self,row, col):
        '''
        Stores the maximum of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the maximum
            col --> Column number to store the maximum
        
        Return value:
            None
        '''        
        
        self.sheet[row][col] = max([self.sheet[i[0]][i[1]] for i in self.selectedvals if self.sheet[i[0]][i[1]] != None])
#======================

#======================
    def PrintSheet(self):
        '''
        Prints the sheet in a human readable from
        Parameters:
            None
        Return value:
            None    

        Note: This is an example output your values will differ
        PrintSheet()
        row/col:    0   1   2   3   4
            0       
            1   
            2           10               
            3                   12
            4 
        '''
        #Fixing the values to have same length
        maxval = 0
        for i in range(self.rows):
            for j in range(self.cols):
                maxval = max(maxval,len(str(self.sheet[i][j])))
        print('row/col:',end=' ')
        for i in range(self.cols):
            if len(str(i))<maxval :
                print(i,end='')
                print((maxval-len(str(i)))*' ',end=' ')
            else:
                print(i,end=' ')
        print()
        #printing the sheet in excel format
        for i in range(self.rows):
            print('  ',i,'  ',end=' ')
            for j in range(self.cols):
                if len(str(self.sheet[i][j]))<maxval:
                    print(self.sheet[i][j],end='')
                    print((maxval-len(str(self.sheet[i][j])))*' ',end=' ')
                else:
                    print(self.sheet[i][j],end=' ')
            print()
#======================

#======================
#
#    DRIVER FUNCTION
#
#======================

def main():
    # -----------------------------
    # Implement your own logic here:
    # -----------------------------
    sheet = Spreadsheet()
    # sheet.CreateSheet(5,5)
    #
    # EXAMPLE LOOP:
    # ------------
    # while True:
    #     sheet.Goto(2,2)
    #     sheet.insert(4)
    #     sheet.Print()
    import sys
    
    print("Welcome to DS SpreadSheet Program")
    print("Enter commands at the prompt")
    
    #Loop to prompt till user asks to Quit
    while True:
        
        function = input(">>>").split()
        if function[0] == "CreateSheet":
            rows = int(function[1])
            cols = int(function[2])
            sheet.CreateSheet(rows,cols)
            print("Sheet successfully created !")
        elif function[0] == "Goto":
            row = int(function[1])
            col = int(function[2])
            sheet.Goto(row,col)
        elif function[0] == "Insert":
            val = int(function[1])
            sheet.Insert(val)
        elif function[0] == "Delete":
            sheet.Delete()
        elif function[0] == "ReadVal":
            sheet.ReadVal()
        elif function[0] == "Select":
            row = int(function[1])
            col = int(function[2])
            sheet.Select(row,col)
        elif function[0] == "GetSelection":
            print("Selection is:", sheet.GetSelection())
        elif function[0] == "Sum":
            row = int(function[1])
            col = int(function[2])
            sheet.Sum(row,col)
        elif function[0] == "Mul":
            row = int(function[1])
            col = int(function[2])
            sheet.Mul(row,col)
        elif function[0] == "Avg":
            row = int(function[1])
            col = int(function[2])
            sheet.Avg(row,col)
        elif function[0] == "Max":
            sheet.Max(row,col)
        elif function[0] == "PrintSheet":
            sheet.PrintSheet()
        elif function[0] == "Quit":
            sys.exit()

if __name__ == '__main__':
    main()
    
#======================


