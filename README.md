# File Organizer & Deorganizer

This repository contains two Python scripts:

1. **File Organizer (`FileOrganizer.py`)**  
   - Automatically organizes files in a folder into categorized subfolders: audios, videos, images, documents, compressed files, and others.  
   - Handles file name conflicts by renaming files to prevent overwriting.

2. **File Deorganizer (`FileDeorganizer.py`)**  
   - Reverts the organization process by moving files from categorized folders back to the main folder.  
   - Handles file name conflicts when moving files back.

## Features

- Fully automated file organization
- Safe renaming for duplicate file names
- Works with most common file types (audio, video, images, documents, compressed files)

## Requirements

- Python 3.x
- No additional libraries required (uses standard Python libraries)

## Example Folder Structure
 Before running Organizer:
 ```
Downloads/
  file1.mp3
  file2.jpg
  file3.pdf
```
After running Organizer:
```
Downloads/
  audios/file1.mp3
  images/file2.jpg
  documents/file3.pdf
```
After running Deorganizer:
```
Downloads/
  file1.mp3
  file2.jpg
  file3.pdf
```
