import argparse
 
parser = argparse.ArgumentParser()
 
parser.add_argument('--file', type=str, default="")
args = parser.parse_args()
 
if args.file:
    try:
        with open(args.file, "r") as file:
            print(len(file.readlines()))
    except Exception:
        print(0)
 
 
def count_lines(path):
    try:
        with open(path, "r") as file:
            return len(file.readlines())
    except Exception:
        return 0
