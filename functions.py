def get_todo(): 
    with open("save.txt",'r') as files:
        To=files.readlines() 
    return To

def write_todos(to):
    with open("save.txt",'w') as files: 
        Todos=files.writelines(to)   
    


# THIS IS USED TO TEST ONE OF THE FUNCTIONSss
#IT WILL ONLY PRINT IF WE RUN THE SCRIPT HERE
#IT WILL NOT PRINT IF WE RUN main.py
# THAT IS IT WILL RUN HERE BUT WILL NOT RUN WHEN IMPORTED INTO ANOTHER FILE OR SCRIPT
#ANY OTHER CODE OUTSIDE THIS CONDITION WILL RUN IN main.py
if __name__=="__main__":
    print(get_todo()) 



#THIS WILL RUN EVEN IN main.py 
# print(get_todo()) 