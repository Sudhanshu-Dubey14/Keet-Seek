from pathlib import Path

jes_files = []


def find_jes_files(dir_path):
    for item in dir_path.iterdir():
        if item.is_dir():
            find_jes_files(item)
        elif item.is_file():
            if item.name == "JESYSMSG.txt":
                jes_files.append(item)
        else:
            print(item.name)


def get_error_code(jobid):
    print("Job ID: " + jobid)
    path = Path("output/" + jobid)
    find_jes_files(path)
    for jes_file in jes_files:
        with open(jes_file) as jes:
            for line in jes:
                for word in line.split():
                    if word.startswith("I") and word.isalnum() and not word.isalpha():
                        return word
