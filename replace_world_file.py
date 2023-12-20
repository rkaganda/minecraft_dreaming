import subprocess


def copy_in_file(source_mca_path, dest_mca_path):
    # server container id
    container_id = '48153eb5e33e020ef3bc8235d4f552ffa7a12f9dea776348cc6ce2c9e3845060'
    # path to regions
    path_in_container = '/data/world/region'
    path_to_save = 'C:/Users/rkaganda/PycharmProjects/minecraft_dreamer/data/region'

    # backup the file
    command = f'docker exec {container_id} cp {path_in_container}/{dest_mca_path} {path_in_container}/{dest_mca_path}_bak'
    print(command)

    # Execute the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()

    # Print the output
    if process.returncode == 0:
        print("OK")
    else:
        print("Error:")
        print(err.decode())

    # copy the file
    command = f'docker cp {path_to_save}/{source_mca_path} {container_id}:{path_in_container}/{dest_mca_path}'
    print(command)

    # Execute the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()

    # Print the output
    if process.returncode == 0:
        print("OK")
    else:
        print("Error:")
        print(err.decode())

    # copy the file
    command = f'docker exec {container_id} chmod 664 {path_in_container}/{dest_mca_path}'
    print(command)

    # Execute the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()

    # Print the output
    if process.returncode == 0:
        print("OK")
    else:
        print("Error:")
        print(err.decode())

    # copy the file
    command = f'docker exec {container_id} chown minecraft:minecraft {path_in_container}/{dest_mca_path}'
    print(command)

    # Execute the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()

    # Print the output
    if process.returncode == 0:
        print("OK")
    else:
        print("Error:")
        print(err.decode())


def main():
    copy_in_file("r-Copy1.-1.-1.mca", "r.-1.-1.mca")


if __name__ == "__main__":
    main()



