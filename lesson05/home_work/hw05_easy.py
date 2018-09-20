import shutil
import sys
import os

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def create_dir(dir_path):
    dir_path = os.path.join(os.getcwd(), dir_path)
    print(dir_path)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Папка {} уже существует'.format(os.path.basename(dir_path)))
 
 
def remove_dir(dir_path):
    dir_path = os.path.join(os.getcwd(), dir_path)
    print(dir_path)
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print('Папка {} не существует'.format(os.path.basename(dir_path)))
    except OSError:
        print('Папка {} не пустая'.format(os.path.basename(dir_path)))

#dir_new_name = input('Input new directory name:')
#dir_rem_name = input('Input directory name to remove:')
#create_dir(dir_path)
#remove_dir(dir_path)

#for i in range(9):
#    dir_new_name = os.path.join(os.getcwd(), 'dir_' + str(i + 1))
#    create_dir(dir_path)
    
#for i in range(9):
#    dir_rem_name = os.path.join(os.getcwd(), 'dir_' + str(i + 1))
#    remove_dir(dir_path)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def local_dir():
    for each in os.listdir(os.getcwd()):
        if os.path.isdir(os.path.join(os.getcwd(), each)):
            print(each, end=' ')

#print('Local directory consist of:')
#local_dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_current_file():
    file = os.path.basename(os.path.realpath(sys.argv[0]))
    shutil.copy2(file, '_copy_' + file)

#copy_current_file()

# для файла средних заданий
def get_dir_name():
    return os.path.join(os.getcwd(), input('Введите имя папки: '))



def change_dir(dir_path):
    try:
        os.chdir(dir_path)
    except FileNotFoundError:
        print('Папка {} не существует'.format(os.path.basename(dir_path)))
        

#change_dir()