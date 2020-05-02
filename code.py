import os

def validates_path(path): # Valida o caminho até o diretório.
    if (os.path.exists(path) == False) or (os.path.isdir(path) == False):
        path = str(input("Error! Insert a valid path: "))
        validates_path(path)
    return True

def join(path, file):
    return (str(path)+'/'+str(file))    

def in_quotes(arg):
    return str('"'+arg+'"')

def reverse_slash(arg):
    return (arg.replace('/','\\'))

def walk_and_heal(dirname):
    for archive in os.listdir(dirname):
        path = join(dirname, archive)
        if (os.path.isfile(path) == True):
            if ".opqz" in archive:
                name = archive.split(".opqz")[0]
                win_cmd = "rename" + ' ' + reverse_slash(in_quotes(path)) + ' ' + reverse_slash(in_quotes(name))
                print(win_cmd) #debugging
                os.system(win_cmd)
                #os.rename(path, join(dirname,name))
        else:
            walk_and_heal(path)

def main():
    user_dir = input("Insert path: ")
    validates_path(user_dir)
    conf = str(input("You is in "+user_dir+". Are you sure to proceed (y/N)?: "))
    if conf in ['y','Y']:
        walk_and_heal(user_dir)
        print("\n\tDone!")
        return 1
    elif conf in ['N', 'n']:
        print("End process.")
        return 0
    else:
        print("Invalid input!")
        return -1
main()
