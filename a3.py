#===================================
#===================================
# Name   : Namisha Naseem
# Roll no: 251684246
# Section: A
# Date   : 
#===================================
#===================================
class Node:
    def __init__(self, name,data=None,type="dir", parent=None):
        self.name = name
        self.data = data
        self.type = type
        self.parent = parent
        self.children = []
result=0
class VirtualFileSystem:
    def __init__(self):
        self.rdirectory= Node("/") #root directory
        self.cdp = self.rdirectory #current directory pointer
    def navigate(self,string):
        walk = self.rdirectory
        dirlist = string.split("/")
        dirlist[0] = "/"
        for k in range(1,len(dirlist)): #navigating from root to directory
            for i in walk.children:
                if i.name == dirlist[k]:
                    walk = i
        return walk
    def mkdir(self,name):
        if name[0] != "/":
            new = Node(name,parent=self.cdp)   #creates new directory
            self.cdp.children.append(new)      #inside current pointer directory
        else:
            dirlist = name.split("/")
            dirlist[0] = "/"
            walk = self.rdirectory 
            for k in range(1,len(dirlist)-1): #navigating from root to directory 
                for i in walk.children:
                    if i.name == dirlist[k]:
                        walk = i                        
            if walk.name == dirlist[-2]:
                new = Node(dirlist[-1],parent=walk) 
                walk.children.append(new)
            else:
                raise Exception("mkdir: "+"/"+ "/".join(dirlist[1:-1])+":  No such file or directory")
    def mv(self,name,location):
         walk = self.rdirectory 
         if name[0] != "/":
            for i in self.cdp.children:
                if i.name == name:
                    walk = i
         else:
             walk = self.navigate(name)             
         newwalk = self.navigate(location)
         newwalk.children.append(walk)
         walk.parent.children.remove(walk)
         walk.parent = newwalk
    def ls(self,path=None):
        if path == None:
            for i in self.cdp.children:
                if i.type == "dir":
                    print("-d- ",i.name)
                else:
                    print("-f- ",i.name)
        else:
            walk = self.navigate(path)                      
            if walk.name == dirlist[-1]:
                for i in walk.children:
                    if i.type == "dir":
                        print("-d- ",i.name)
                    else:
                        print("-f- ",i.name)
            else:
                raise Exception("ls: "+"/"+ "/".join(dirlist[1:])+":  No such file or directory")
    def touch(self,path,newdata=None):
        if path[0] != "/":
            new=Node(path,newdata,"file",self.cdp)
            self.cdp.children.append(new)
        else:
            dirlist = path.split("/")
            dirlist[0] = "/"
            walk = self.rdirectory 
            for k in range(1,len(dirlist)-1): #navigating from root to directory 
                for i in walk.children:
                    if i.name == dirlist[k]: 
                        walk = i 
            if walk.name == dirlist[-2]:
                new=Node(dirlist[-1],newdata,"file",walk)
                walk.children.append(new)
            else:
                raise Exception("touch: "+"/"+ "/".join(dirlist[1:-1])+":  No such file or directory")
    def cat(self,path):
        if path[0] != "/":
            walk=self.cdp
        else:
            dirlist = path.split("/")
            dirlist[0] = "/"
            walk = self.rdirectory
            path = dirlist[-1]
            for k in range(1,len(dirlist)-1): #navigating from root to directory 
                for i in walk.children:
                    if i.name == dirlist[k]:
                        walk = i
            if walk.name != dirlist[-2]:
                raise Exception("ls: "+"/"+ "/".join(dirlist[1:])+":  No such file or directory")
        for i in walk.children:
            if i.name == path:
                if i.type == "file":
                    print(i.data)
                else:
                    print("cat: ",path,": ","is a directory")
    def cd(self,dir1):
        if dir1 == "/":
            self.cdp = self.rdirectory
        elif dir1[0] == "/":
            walk = self.navigate(dir1)
            if walk.name == dirlist[-1]:
                self.cdp = walk
            else:
                raise Exception("cd: "+"/"+ "/".join(dirlist[1:-1])+":  No such file or directory")
        elif dir1 == "..":
            self.cdp = self.cdp.parent
        elif dir1 == ".":
            self.cdp = self.cdp
        else:
            for i in self.cdp.children:
                if i.name == dir1:
                    self.cdp = i
    def pwd(self):
        walk = self.cdp
        lst =[]
        while walk.name != "/":
            lst.append(walk.name)
            walk = walk.parent
        lst.reverse()
        for i in lst:           #can current directory pointer point to root "/"
            print("/"+i,end="")
    def rm(self,name):
        if name[0] != "/":
            for i in self.cdp.children:
                if i.name == name:
                    self.cdp.children.remove(i)      #inside current pointer directory
        else:
            walk = self.navigate(name)                       
            if walk.name == dirlist[-1]:
                walk.parent.children.remove(walk)
            else:
                raise Exception("rm: "+"/"+ "/".join(dirlist[1:-1])+":  No such file or directory")
                
    def find(self,path,source):
        global result
        if type(path) == str:
            walk = self.navigate(path)
        else:
            walk = path
        if len(walk.children)<1:
            if walk.name == source:
                lst =[]
                while walk.name != "/":
                    lst.append(walk.name)
                    walk = walk.parent
                lst.reverse()
                print(lst)
                for i in lst:           #can current directory pointer point to root "/"
                    print("/"+i,end="")
                return 1
            else:
                return 0
        else:
            for i in walk.children:
                result = result+ self.find(i,source)
        return result
    def cp(self,source,destination):
        if type(source) == str:
            if source[0] != "/":
                for i in self.cdp.children:
                    if i.name == source:
                        source = i
            else:
                source = self.navigate(source) 
        if len(source.children)<1:
            destination = self.navigate(destination) 
            new = Node(source.name,source.data,source.type,destination)
            destination.children.append(new)
        else:
            for i in source.children:
                destination=self.cp(i,destination)
                
def _argCheck(argCount,argc):
    if argc < argCount:
        print("Too few arguments")
        return False
    return True

def main():
    vfs=VirtualFileSystem()
    import sys
    print("===============================")
    print("DSA Project 3")
    print("-------------------------------")
    print("Virtual File System Emulator")
    print("===============================")
    while True:
        function = input("namisha:~$").split()
        if function[0] == "exit":
            print("Terminating current session.Bye...")
            sys.exit()
        elif function[0] == "mkdir":
            if(not _argCheck(1, len(function)-1)):
                sys.exit()
            vfs.mkdir(function[1])
        elif function[0] == "ls":
            if len(function) == 1:
                vfs.ls()
            else:
                vfs.ls(function[1])
        elif function[0] == "touch":
            if(not _argCheck(1,len(function)-1)):
                sys.exit()
            if len(function) == 2:
                vfs.touch(function[1])
            else:
                vfs.touch(function[1]," ".join(function[2:]))
        elif function[0] == "cat":
            if(not _argCheck(1,len(function)-1)):
                sys.exit()
            vfs.cat(function[1])
        elif function[0] == "cd":
            if(not _argCheck(1,len(function)-1)):
                sys.exit()
            vfs.cd(function[1])
        elif function[0] == "rm":
            if(not _argCheck(1,len(function)-1)):
                sys.exit()
            vfs.rm(function[1])
        elif function[0] == "pwd":
            vfs.pwd(function[1])
        elif function[0] == "mv":
            if(not _argCheck(2,len(function)-1)):
                sys.exit()
            vfs.mv(function[1],function[2])
        elif function[0] == "cp":
            if(not _argCheck(2,len(function)-1)):
                sys.exit()
            vfs.cp(function[1],function[2])
        elif function[0] == "find":
            if(not _argCheck(2,len(function)-1)):
                sys.exit()
            vfs.find(function[1],function[2])
if __name__ == '__main__':
    main()

