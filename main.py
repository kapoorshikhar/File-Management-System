import os

def create_file(filename):
    try:
        with open(f'{filename}.txt','x')as f:
            print(f"{filename} is  created sucessfull with the use of python ")
    except FileExistsError:
        print(f" Try something else the file{filename} already present in the folder")
    except Exception as e :
        print (f"There is some error unexpected error in creating {filename}")

def view_all():
    files= os.listdir()
    if not files :
        print ("The file is not present ")
    else:
        print("The file is present")
        for file in files:
            print(file)
            
def delete_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        print(f" Try something else the file {filename} is not  present in the folder")
    except Exception as e :
        print (f"There is some error unexpected error in delete {filename}")
        
def read_file(filename):
    try:
        with open(f"{filename}", 'r') as f:
            content=f.read()
            print (content)
    except FileNotFoundError:
        print(f" Try something else the file name :{filename} is not  present in the folder")
    except Exception as e :
        print (f"There is some error unexpected error in reading {filename}")        
                
def write_file(filename):
    try:
        with open(f"{filename}", 'w')as f:
            w= input( "USER PLEASE ENTER THE CONTENT THAT HAS TO BE EDITED :")      
            f.write(w +'/n') 
    except FileNotFoundError:
        print(f" Try something else the file name :{filename} is not  present in the folder")              
    except Exception as e :
        print (f"There is some error unexpected error in reading {filename}")        
    
def main():
    while True:
        print(" File Mangaement System ")
        print(" 1: Creation of File")
        print(" 2: View of File")
        print(" 3: Deletion of File")
        print(" 4: Reading of File")
        print(" 5: Writing of File")
        print(" 6: For Exit the File Manager")
        choice = input (" Enter the choice( 1-6 ) : ")
        if choice=='1':
            filename= input("Enter the File name : ")
            create_file(filename)
        if choice=='2':
            view_all()
        if choice=='3':
            filename= input("Enter the File name : ")
            delete_file(filename)
        if choice=='4':
            filename= input("Enter the File name : ")
            read_file(filename)
        if choice=='5':
            filename= input("Enter the File name : ")
            write_file(filename)
        if choice=='6':
            print(" The file is exiting .......")
            break
if __name__=="__main__":
    main()
     
        
        