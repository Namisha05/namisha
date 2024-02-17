import tkinter as tk
import ttkbootstrap as ttk
import time 

#GUI window
window = ttk.Window(themename='minty')
window.title('Simulator')
window.geometry('700x500')

heading = ttk.Label(master=window,text="Memory Paging Simulator",font='calibri 20 italic')
heading.pack(pady=20)


#this is the virtual memory of process with 8 pages
logicalmemory = ['A','B','C','D','E','F','G','H']

#memory with size of 6 frame
memory = ['free','free','free','free','free','free']


#page table index is page number, 0 index of tuple is frameno(-1 when no frame), i is invalid bit
pagetable = [[-1, 'i'], [-1, 'i'], [-1, 'i'], [-1, 'i'], [-1, 'i'], [-1, 'i'], [-1, 'i'], [-1, 'i']]

#order in which pages were accessed
seq=[0,1,2,5,6,4,2,3,7,5]

#display sequence of pages
seqlabel= ttk.Label(master=window, text='Sequence:'+str(seq),font='calibri 12')
seqlabel.pack()

info = ttk.StringVar()
info.set("Hello")
infotext = ttk.Label(master=window,textvariable=info,font='calibri 14')
infotext.pack(pady=10)

#display logical memory
buttons=[]
logmemory = ttk.Frame(master = window)
for page in range(len(logicalmemory)):
    var = ttk.StringVar()
    var.set(str(page)+'         '+logicalmemory[page])
    button = ttk.Button(master=logmemory, width=10, textvariable=var,bootstyle='secondary')
    button.pack()
    buttons.append((var, button))
label= ttk.Label(master=logmemory,text='Logical Memory')
label.pack()
logmemory.pack(side='left',padx=70)

#display page table
buttons1=[]
pgtable = ttk.Frame(master=window)
for pages in range(len(pagetable)):
    var1 = ttk.StringVar()
    val2= ttk.StringVar()
    var1.set(str(pages)+'       '+str(pagetable[pages][0])+'        '+pagetable[pages][1])
    button1 = ttk.Button(master=pgtable, width=15, textvariable=var1,bootstyle='success-outline')
    button1.pack()
    buttons1.append((var1, button1))
label= ttk.Label(master=pgtable,text='Page Table')
label.pack()
pgtable.pack(side='left',padx=70)

#display memory
memoryf = ttk.Frame(master = window)
buttons2 =[]
for pag in range(len(memory)):
    var2 = ttk.StringVar()
    var2.set(str(pag)+'         '+memory[pag])
    button2 = ttk.Button(master=memoryf, width=10, textvariable=var2,bootstyle='primary')
    button2.pack()
    buttons2.append((var2, button2)) #incase buttons need to accessed sperately
label2= ttk.Label(master=memoryf,text='Memory')
label2.pack()
memoryf.pack(side='left',padx=70)

 #update display
    
def update_logical_memory_display():
    for page, (var, button) in enumerate(buttons):
        var.set(f"{page}         {logicalmemory[page]}")

def update_page_table_display():
    for pages, (var1, button1) in enumerate(buttons1):
        var1.set(f"{pages}       {pagetable[pages][0]}        {pagetable[pages][1]}")

def update_memory_display():
    for pag, (var2, button2) in enumerate(buttons2):
        var2.set(f"{pag}         {memory[pag]}")

def update_displays():
    update_logical_memory_display()
    update_page_table_display()
    update_memory_display()

#order in which frames get occupied
order = []
freeframe = -1 


for i in seq:
    time.sleep(5)
    found = False #to check if memory is full
    for frameno in range(len(memory)):
        if memory[frameno]== 'free':
            found=True
            freeframe = frameno
            break
    if found == True:   #if there is free frame in memory
        memory[freeframe] = logicalmemory[i]
        pagetable[i][0]= freeframe
        pagetable[i][1]= 'v'
        order.append(i)
        info.set("Page "+str(logicalmemory[i])+" sent to memory")
    elif logicalmemory[i] not in memory:       #replacing first frame using FIFO
        victimpageno = order[0]
        order = order[1:]
        for freeframe in range(len(memory)):
            if memory[freeframe]==logicalmemory[victimpageno]:
                break
        memory[freeframe] = logicalmemory[i]
        pagetable[i][0]=freeframe
        pagetable[i][1]= 'v'
        pagetable[victimpageno][0]= -1
        pagetable[victimpageno][1]= 'i'
        info.set("Memory full! \n Using FIFO page: "+str(logicalmemory[i])+" replaces page:"+str(logicalmemory[victimpageno]))
    else:
        info.set("Page "+str(logicalmemory[i])+ " already in memory")
    # Add the following function to update the displays after each iteration
    update_displays()
    window.update() 

info.set("Finished!")
#run
window.mainloop()