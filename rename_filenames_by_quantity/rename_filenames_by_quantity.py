import os

def rename_file(folder, flag=None ):
    if flag==None:
        print("please set a number for flag, 1 or 2")
    elif flag==1:
        _rename_filenames(folder)
    elif flag==2:
        for i in os.listdir(folder):
            dir_name = os.path.join(folder,i)
            if os.path.isdir(dir_name):
                _rename_filenames(dir_name)

def _rename_filenames(folder):
    for number, filename in enumerate(os.listdir(folder)):
        name_old = os.path.join(folder, filename)
        name_mew = os.path.join(folder, str(number))
        if os.path.isfile(name_old):
            # rename() could only change file, renames() could change file and directory
            os.rename(name_old, name_mew)