#===================================
#===================================
# Name   : 
# Roll no: 
# Section: 
# Date   : 
#===================================
#===================================


#------------------------------------
# Node class for a Doubly Linked List
#------------------------------------
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
#------------------------------------

class TextEditor:
    def __init__(self):
        '''
        Predefined member variables. 
        
        WARNING: DO NOT MODIFY THE FOLLOWING VARIABLES
        '''
        self.doc = None        # The root of everything. See page 3 for details
        
        #======================
        # Insert your Member
        #   variables here (if any):
        #----------------------
        
        
        #======================
        
#======================
    def goto(self, row, col):
        '''
        Moves the cursor to the location indicated by the 
          row and col parameters
 
        Parameters:
            row --> row number to move to
            col --> column number to move to
        
        Return value:
            None
        '''
        
        raise NotImplementedError
#======================

#======================
    def forward(self):
        '''
        Moves the cursor one step forward
 
        Parameters:
            None
        
        Return value:
            None
        '''
        
        raise NotImplementedError
#======================

#======================
    def back(self):
        '''
        Moves the cursor one step backwards
 
        Parameters:
            None
        
        Return value:
            None
        '''
        
        raise NotImplementedError
#======================

#======================
    def home(self):
        '''
        Moves the cursor to the start of the current line
 
        Parameters:
            None
        
        Return value:
            None
        '''
        
        raise NotImplementedError
#======================

#======================
    def end(self):
        '''
        Moves the cursor to the end of the current line
 
        Parameters:
            None
        
        Return value:
            None
        '''
        
        raise NotImplementedError
#======================

#======================
    def insert(self, string):
        '''
        Inserts the given string immediately after the cursor
 
        Parameters:
            a string
        
        Return value:
            None
        '''
        
        raise NotImplementedError
#======================

#======================
    def delete(self, num):
        '''
        Deletes specified number of characters from the cursor position
 
        Parameters:
            integer number of characters to delete
        
        Return value:
            None
        '''
        
        raise NotImplementedError
#======================

#======================
    def countCharacters(self):
        '''
        Moves the cursor to the start of the current line
 
        Parameters:
            None
        
        Return value:
            total number of characters in the document, basically
               the total number of pink nodes in the document.
        '''
        
        raise NotImplementedError
#======================

#======================
    def countLines(self):
        '''
        Count total of non-empty lines in the document.
 
        Parameters:
            None
        
        Return value:
            integer number of non-empty lines in the document
        '''
        
        raise NotImplementedError
#======================


#======================
    def printDoc(self):
        '''
        Prints the entire document on the screen.
        '''
        
        raise NotImplementedError
#======================

            
#======================
#======================
#    BONUS
#======================
    def undo(self):
        '''
        Undos the previous action by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def redo(self):
        '''
        Redos the previous action undone by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def save(self, fileName):
        '''
        Saves the spreadsheet to a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def load(self, fileName):
        '''
        Loads the spreadsheet from a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        
        raise NotImplementedError
            
#----------------------

    def find(self, substr):
        '''
        Finds a given substring within the entire document. If no such substring
          is found then return None.
 
        Parameters:
            substring to look for
        
        Return value:
            - reference to the first node of the substring found
            - None if substring is not found
        '''
        
        raise NotImplementedError
            
                
#======================


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
    editor = TextEditor()
    #
    # while True:
    #     editor.Goto(0,0)
    #     editor.insert("Hello comp200")
    #     editor.printDoc()
    

if __name__ == '__main__':
    main()
    
#======================


