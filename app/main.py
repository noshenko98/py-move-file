import shutil
import os


def move_file(command: str) -> None:
    command = command.split()
    if command[0] == "mv" and len(command) == 3:
        print(command)
        path = command[2].split("/")
        path_start = ""
        for part_patch in path[:-1]:
            try:
                os.mkdir(path_start + part_patch)
            except FileExistsError:
                pass
            finally:
                path_start += part_patch + "/"
        shutil.copy2(command[1], command[2])
        os.remove(command[1])
