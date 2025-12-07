from os import listdir, mkdir
from os.path import isfile, isdir, join, splitext
from shutil import move

print('*******************************')
print("""This program will organize your files in the folder you specify.
The files will be organized into the following folders:
      - audios
      - videos
      - images
      - documents
      - compressed files
      - others

If the folders already exist, you can choose eather to overwrite them or to skip them.""")
print('*******************************\n')


# Get the folder path from the user and make sure it is valid
valid = False
while not valid:
    folder_path = input("""Enter the path of the folder you want to organize.')
Example: C:\\Users\\Me\\Downloads:\n""")
    folder_path = folder_path.replace('\\','/') 
    if isdir(folder_path):
        valid = True
    else:
        print('Invalid path! Please try again.')

# Get the list of files in the given folder
files_list = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]

# print(files_list)


# Define the folders and their extensions
audio = ['mp3','wav','ogg','flac','aiff','aac','wma','m4a','alac','dsd','pcm']
video = ['mp4','mov','wmv','avi','avchd','flv','f4v','swf','mkv','webm','html5','mpeg-2']
image = ['jpg','jpeg','png','gif','bmp','svg','tiff','eps','raw','cr2','nef','orf','sr2']
doc = ['doc','docx','pdf','txt','rtf','odt','xls','xlsx','ppt','pptx','csv','xml','json','yaml','html','css','js','php','java','c','cpp','py','rb','go','swift','kt','dart','sh','ps1','psm1','bat','cmd','vbs','vba','psd','ai','indd','pub','xps','epub','mobi','azw','azw3','ibooks','djvu','fb2','lit','lrf','lrx','pdb','pml','tcr','tpz']
compressed = ['zip','rar','7z','tar','gz','bz2','xz','z','tgz','tbz2','txz','iso','dmg','img','vcd','bin','cue','mdf','nrg','toast','vhd','vmdk','vdi','qcow','qcow2','qed','vpc','vbox','ova','ovf','raw','sparsebundle','sparseimage','vhdx','vmdk','vdi','qcow2','qcow','qed','vpc','vbox','ova','ovf','raw','sparsebundle','sparseimage','vhdx']


# Create the folders (audios, videos, images, documents, compressed files, others)
direcories = [f'{folder_path}/audios',f'{folder_path}/videos',f'{folder_path}/images',f'{folder_path}/documents',f'{folder_path}/compressed files',f'{folder_path}/others']
for directory in direcories:
    try:
        mkdir(directory)
    except FileExistsError:
        print(f'The directory {directory} already exists. So a new one won\'t be created.')


# Function to change the file directory
old_names = []
new_names = []
def change_file_directory(folder_path, file, Type):
    src = join(folder_path, file)
    dst_dir = join(folder_path, Type)
    dst = join(dst_dir, file)
    
    # Check if the file already exists in the destination directory
    if not isfile(dst):
        move(src, dst)
    else:
        # If the file already exists, rename the file to avoid overwriting
        old_names.append(file)

        file_name, file_ext = splitext(file)
        new_file = file
        n = 1

        # keep renaming the file until it doesn't exist in the destination directory
        while isfile(join(dst_dir, new_file)):
            new_file = f"{file_name}_{n}{file_ext}"
            n += 1
        new_names.append(new_file)
        new_dst = join(dst_dir, new_file)
        move(src, new_dst)

# Organize the files
for file in files_list:
    file_name, file_extension = splitext(file)
    file_extension = file_extension[1:]
    if file_extension in audio:
        change_file_directory(folder_path,file,'audios')
    elif file_extension in video:
        change_file_directory(folder_path,file,'videos')
    elif file_extension in image:
        change_file_directory(folder_path,file,'images')
    elif file_extension in doc:
        change_file_directory(folder_path,file,'documents')
    elif file_extension in compressed:
        change_file_directory(folder_path,file,'compressed files')
    else:
        change_file_directory(folder_path,file,'others')     

print('The files have been organized successfully!')

# Print the renamed files
if old_names:
    print('To avoid overwriting, the following files have been renamed:')
    for i in range(len(old_names)):
        print(f'{old_names[i]} --> {new_names[i]}')