from glob import glob


def get_file_data():
    files = glob("diary/*.txt")
    sorted_files = sorted(files)
    file_data = []
    for file in sorted_files:
        name = file.strip(".txt").strip("diary/")
        filename = file.split("/")[1]
        file_data.append((name, filename))
    return file_data


if __name__ == "__main__":
    data = get_file_data()
    print(data)
