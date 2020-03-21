def dirReduc(dirs):
    contras = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST", None: ""}
    changed = True
    while changed:
        changed = False
        for i_dir in range(len(dirs) - 1):
            if dirs[i_dir] == contras[dirs[i_dir+1]]:
                dirs[i_dir] = None
                dirs[i_dir + 1] = None
                changed = True
        dirs = list(filter(lambda x: x is not None, dirs))
    return dirs
