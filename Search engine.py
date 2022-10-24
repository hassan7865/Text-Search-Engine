import os,re,datetime
v=[]
def Findfile(path,word):
    a = os.scandir(path)
    for i in a:
        if i.is_file():
            x=re.findall(".txt",str(i))
            if x:
                f=open(i,"r")
                b=re.findall(word,f.read())
                if b:
                    v.append(i)
        else:
            Findfile(i.path,word)
def PhysicalFile(v=v):
    if v==[]:
        print("Not Found")
    else:
        print("Found",len(v),"File")
        gap=' '*3
        heading=f"{'RNo':2s}{gap}{'Name':15s}{gap}{'Path':50s}{gap}{'Size':10s}{gap}{'C-Date':40s}{gap}{'M-Date'}"
        print("="*144)
        print(heading)
        print("-"*144)
        for k in range(len(v)):
            Name_of_file=v[k].name
            Path_of_file=v[k].path
            Size_of_file=str(v[k].stat()[6])+" Bytes"
            Created_date=datetime.datetime.fromtimestamp(os.path.getctime(Path_of_file))
            Modified_date=datetime.datetime.fromtimestamp(os.path.getmtime(Path_of_file))
            gd=f"{k+1:2d}{gap}{Name_of_file:15s}{gap}{Path_of_file:50s}{gap}{Size_of_file:10s}{gap}{Created_date}{gap}{Modified_date}"
            print(gd)
        print("-"*144)
User = str(input("ENTER THE PATH:"))
word = str(input("ENTER THE WORD TO SEARCH:"))
Findfile(User,word)
PhysicalFile()
    
    
