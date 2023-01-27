
import os
from pathlib import Path

# Function to rename multiple files
def main():
    folder = 'combine_split'
    paths = sorted(Path(folder).iterdir(), key=os.path.getmtime) 
    for count, filename in enumerate(paths):
        filename = filename.name
        dst = f"sistem_dodo_b{str(count)}.csv"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
        print(src)
        print(dst)

        # rename() function will
        # rename all the files
        os.rename(src, dst)
 
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()