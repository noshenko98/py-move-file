import shutil
import os


def move_file(command: str) -> None:
    mv_token = command.split()
    if len(mv_token) == 3 and mv_token[0] == "mv":
        path = mv_token[2].split("/")
        path_start = ""
        print(path)
        for part in path[:-1]:
            try:
                os.mkdir(os.path.join(path_start, part))
            except FileExistsError:
                pass
            finally:
                path_start = os.path.join(path_start, part)
                print(path_start)
        path_start = os.path.join(path_start, path[-1])
        shutil.copy2(mv_token[1], path_start)
        os.remove(mv_token[1])
