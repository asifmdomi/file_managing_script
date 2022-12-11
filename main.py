import sys
import shutil
from os import walk, rmdir, listdir, mkdir
from os.path import join, split, exists, isfile
from file2ext import name2ext_dict


def the_inspector(path):
    dir_paths = []
    file_paths = []
    for root, ch_dirs, files in walk(path):
        for ch_dir in ch_dirs:
            dir_path = join(root, ch_dir)
            if dir_path not in dir_paths:
                dir_paths.append(dir_path)

        for file in files:
            file_path = join(root, file)
            if file_path not in file_paths:
                file_paths.append(file_path)

    return dir_paths, file_paths


def preprocessing_file_dirs(path):
    dir_path_list, file_path_list = the_inspector(path)
    for file_path in file_path_list:
        location, name = split(file_path)
        new_file_path = join(path, name)
        if file_path != new_file_path:
            print(f'moving file {name} from {location} to {path}')
            shutil.move(file_path, new_file_path)

    for dir_path in sorted(dir_path_list, key=len, reverse=True):
        print(f'removing directory {dir_path}')
        rmdir(dir_path)


def organizing_files(path):
    for element in listdir(path):
        ext = element.split('.')[-1].lower()
        file_path = join(path, element)
        if isfile(file_path):
            for dir_name in name2ext_dict:
                if ext in name2ext_dict[dir_name]:
                    dir_path = join(path, dir_name)
                    if not exists(dir_path):
                        print(f'making directory named {dir_name} in the directory {path}')
                        mkdir(dir_path)
                    new_file_path = join(dir_path, element)
                    print(f'{element} file is being moved to folder {dir_name}.')
                    shutil.move(file_path, new_file_path)


def control(source):
    preprocessing_file_dirs(source)
    organizing_files(source)


def main():
    if len(sys.argv) != 2:
        print('Usage: <program> <source path directory>')
        return
    source_path = sys.argv[1]

    control(source_path)


if __name__ == '__main__':
    main()
