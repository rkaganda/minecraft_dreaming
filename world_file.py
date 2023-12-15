import subprocess


def load_chunk_file(r, x, z, m):
    # server container id
    container_id = '48153eb5e33e020ef3bc8235d4f552ffa7a12f9dea776348cc6ce2c9e3845060'
    # path to regions
    path_in_container = '/data/world/region'
    path_to_save = 'C:/Users/rkaganda/PycharmProjects/minecraft_dreamer/data/region'

    # copy the file
    command = f'docker cp {container_id}:{path_in_container}/r.{x}.{z}.mca {path_to_save}/r.{x}.{z}.mca'
    print(command)

    # Execute the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()

    # Print the output
    if process.returncode == 0:
        print("Exported file.")
    else:
        print("Error:")
        print(err.decode())


def list_chunk_files():
    # server container id
    container_id = '48153eb5e33e020ef3bc8235d4f552ffa7a12f9dea776348cc6ce2c9e3845060'
    # path to regions
    path_in_container = '/data/world/region'

    # copy the file
    command = f'docker exec {container_id} ls {path_in_container}/'
    print(command)

    # Execute the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()

    files = []

    # Print the output
    if process.returncode == 0:
        print("Files found:")
        for lin in out.decode().split('\n'):
            coordinates = lin.split('.')
            if 'mca' in coordinates:
                print(lin)
                files.append({'x': coordinates[1], 'z': coordinates[2]})

    else:
        print("Error:")
        print(err.decode())

    return files


chunk_files = list_chunk_files()
for fn in chunk_files:
    load_chunk_file(r=None, x=fn['x'], z=fn['z'], m=None)


