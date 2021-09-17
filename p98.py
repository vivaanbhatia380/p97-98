def swapefiledata():
    file1=input('enter the file name ')
    file2=input('enter the file name ')
    with open (file1,'r') as a:
        data_a=a.read()
    with open (file2,'b') as b:
        data_b=b.read()