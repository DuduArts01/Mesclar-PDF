import PyPDF2
import os

def receive_files():
    merger = PyPDF2.PdfMerger()
    list_files = os.listdir("Files_to_merger")
    list_files.sort()

    if list_files != []:
        for file in list_files:
            if ".pdf" in file:
                merger.append(f"Files_to_merger/{file}")
        Convert_files(merger)
    else:
        print("You did not put the files in the Files_to_merger folder!!!")
        print("Try again.")
    
    

def Convert_files(files_merger):
    list_files_convert = os.listdir("Files_Convert")
    n = 1
    while True:
        if f"{n}_Final.pdf" in list_files_convert:
            n += 1
        else: 
            files_merger.write(f"Files_Convert/{n}_Final.pdf")
            break

merger_files = receive_files()
print("Program Finished!!!")

