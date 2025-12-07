from os import listdir, rmdir
from os.path import isdir, isfile, splitext, join
from shutil import move

# Get the path of the folder to deorganize and make sure it's valid
valid = False
while not valid:
    folder_path = input("""Enter the path of the folder you want to deorganize.
Example: C:\\Users\\Me\\Downloads:\n""")
    folder_path = folder_path.replace("\\", "/")
    if isdir(folder_path):
        valid = True
    else:
        print("Invalid path. Please try again.")

folders = ["audios", "videos", "images", "documents", "compressed files", "others"]
old_names = []
new_names = []

for folder in folders:
    folder_dir = join(folder_path, folder)

    # check if the folder exists so that we don't get an error
    if not isdir(folder_dir):
        continue

    # Move files from the subfolder to the main folder
    for f in listdir(folder_dir):
        src = join(folder_dir, f)
        dst = join(folder_path, f)

        # check if the file already exists in the main folder
        if not isfile(dst):
            move(src, dst)

        else:
            # if the file already exists, rename it until it doesn't exist
            old_names.append(f)
            file_name, file_ext = splitext(f)
            new_file = f
            n = 1
            while isfile(join(folder_path, new_file)):
                new_file = f"{file_name}_{n}{file_ext}"
                n += 1
            new_names.append(new_file)

            final_dst = join(folder_path, new_file)
            move(src, final_dst)

    # Delete the subfolder
    try:
        rmdir(folder_dir)
    except:
        pass

print("The files have been deorganized successfully!")

# Print the renamed files
if old_names:
    print("To avoid overwriting, the following files have been renamed:")
    for i in range(len(old_names)):
        print(f"{old_names[i]} --> {new_names[i]}")
