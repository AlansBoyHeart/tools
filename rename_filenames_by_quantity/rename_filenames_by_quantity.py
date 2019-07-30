import os

def rename_file(folder, flag=None ):
    """
    :param folder:
    :param flag:1是单级目录，2是两级目录
    :return:
    """
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
        suffix = filename.split(".")[-1]
        # number += 100

        name_new = os.path.join(folder, str(number)+"."+suffix)


        if os.path.isfile(name_old):
            # rename() could only change file, renames() could change file and directory
            os.rename(name_old, name_new)