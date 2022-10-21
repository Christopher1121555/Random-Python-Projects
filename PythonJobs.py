
import threading
import time
#job run
global memory

memory = 8

print ("*Available memory =", memory, "Kbyte*\n\n")


def func1():
    global memory
    time.sleep(1)
    jobA =  open("C:\\Users\\christopher.procum\\Desktop\\Jobs\\1.txt", 'r')
    fileA = jobA.readline(28)
    print (fileA)

    time.sleep(7)

    #Job state
    with open ("C:\\Users\\christopher.procum\\Desktop\\Jobs\\1.txt", "r") as file:
        lastLine = file.readline()
        for lastLine in file:
            pass
    
        print((75*("-")), "\n\n")
        print(lastLine) 
    
    jobA.close()
    
    memoryA = memory - 2
    memory = memoryA
    
    if memoryA < 1:
        print ("\nNot enough memory, allocating room for more storage\n")
        memory = memory + 5
        
        
    print("*Job 1 has a size of 2Kbyte. Available memory after processing =", memory, "Kbyte*\n\n")
    print((75*("-")))
    
    
    
 
def func2():
    global memory
    time.sleep(2)
    jobA =  open("C:\\Users\\christopher.procum\\Desktop\\Jobs\\2.txt", 'r')
    fileA = jobA.readline(28)
    print (fileA)

    time.sleep(8)

    #Job state
    with open ("C:\\Users\\christopher.procum\\Desktop\\Jobs\\2.txt", "r") as file:
        lastLine = file.readline()
        for lastLine in file:
            pass
    
        print((75*("-")), "\n\n")
        print(lastLine)
    
    memoryA = memory - 3
    memory = memoryA
    
    
    if memoryA < 1:
        print ("\nNot enough memory, allocating room for more storage\n")
        memory = memory + 5
        
        
    print("*Job 2 has a size of 3Kbyte. Available memory after processing =", memory, "Kbyte*\n\n")
    print((75*("-")))
    
    
def func3():
    global memory
    time.sleep(3)
    jobA =  open("C:\\Users\\christopher.procum\\Desktop\\Jobs\\3.txt", 'r')
    fileA = jobA.readline(28)
    print (fileA)

    time.sleep(6)

    #Job state
    with open ("C:\\Users\\christopher.procum\\Desktop\\Jobs\\3.txt", "r") as file:
        lastLine = file.readline()
        for lastLine in file:
            pass
    
        print((75*("-")), "\n\n")
        print(lastLine)
        
    memoryA = memory - 4
    memory = memoryA
    
    if memoryA < 1:
        print ("Not enough memory, allocating room for more storage")
        memory = memory + 5
        
    
    print("*Job 3 has a size of 4 Kbyte. Available memory after processing =", memory, "Kbyte*\n\n")
    print((75*("-")))
        
        
def func4():
    global memory
    time.sleep(4.1)
    jobA =  open("C:\\Users\\christopher.procum\\Desktop\\Jobs\\4.txt", 'r')
    fileA = jobA.readline(28)
    print (fileA)

    time.sleep(6)

    #Job state
    with open ("C:\\Users\\christopher.procum\\Desktop\\Jobs\\4.txt", "r") as file:
        lastLine = file.readline()
        for lastLine in file:
            pass
        
        print((75*("-")), "\n\n")
        print(lastLine)  
        
    memoryA = memory - 3
    memory = memoryA
    
    if memoryA < 1:
        print ("\nNot enough memory, allocating room for more storage\n")
        memory = memory + 5
        
    print("*Job 4 has a size of 3 Kbyte. Available memory after processing =", memory, "Kbyte*\n\n")
    print((75*("-")))   
        
        
def func5():
    global memory
    time.sleep(5)
    jobA =  open("C:\\Users\\christopher.procum\\Desktop\\Jobs\\5.txt", 'r')
    fileA = jobA.readline(28)
    print (fileA)

    time.sleep(9)

    #Job state
    with open ("C:\\Users\\christopher.procum\\Desktop\\Jobs\\5.txt", "r") as file:
        lastLine = file.readline()
        for lastLine in file:
            pass
    
        print((75*("-")), "\n\n")
        print(lastLine)  



    memoryA = memory - 2
    memory = memoryA
    
    if memoryA < 1:
        print ("\nNot enough memory, allocating room for more storage\n")  
        memory = memory + 5
        
    print("*Job 5 has a size of 2 Kbyte. Available memory after processing =", memory, "Kbyte*\n\n")
    print((75*("-")))
    
    
    
    
    
def func6():
    global memory
    time.sleep(6)
    jobA =  open("C:\\Users\\christopher.procum\\Desktop\\Jobs\\6.txt", 'r')
    fileA = jobA.readline(28)
    print (fileA)

    time.sleep(6)

    #Job state
    with open ("C:\\Users\\christopher.procum\\Desktop\\Jobs\\6.txt", "r") as file:
        lastLine = file.readline()
        for lastLine in file:
            pass
    
        print((75*("-")), "\n\n")
        print(lastLine) 
        
    memoryA = memory - 3
    memory = memoryA
    
    if memoryA < 1:
        print ("\nNot enough memory, allocating room for more storage\n")
        memory = memory + 5
        
    print("*Job 6 has a size of 3 Kbyte. Available memory after processing =", memory, "Kbyte*\n\n")
    print((75*("-")))
        
        

def func7():
    global memory
    time.sleep(7)
    jobA =  open("C:\\Users\\christopher.procum\\Desktop\\Jobs\\7.txt", 'r')
    fileA = jobA.readline(28)
    print (fileA)

    time.sleep(6)

    #Job state
    with open ("C:\\Users\\christopher.procum\\Desktop\\Jobs\\7.txt", "r") as file:
        lastLine = file.readline()
        for lastLine in file:
            pass
    
        print((75*("-")), "\n\n")
        print(lastLine) 
        
        
        memoryA = memory - 2
        memory = memoryA
        if memoryA < 1:           
            print ("\nNot enough memory, allocating room for more storage\n")
            memory = memory + 5
            
    print("*Job 7 has a size of 2 Kbyte. Available memory after processing =", memory, "Kbyte*\n\n")
    print((75*("-")))
    
 
#Starts each function simultaneousely 

Thread1 = threading.Thread(target = func1)
Thread2 = threading.Thread(target = func2)
Thread3 = threading.Thread(target = func3)
Thread4 = threading.Thread(target = func4)
Thread5 = threading.Thread(target = func5)
Thread6 = threading.Thread(target = func6)
Thread7 = threading.Thread(target = func7)

Thread1.start()
Thread2.start()
Thread3.start()
Thread4.start()
Thread5.start()
Thread6.start()
Thread7.start()








































        





