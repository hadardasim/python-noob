import getopt
import sys
import pandas as pd
import os


def main(argv):
    base_dir = None
    usage_str = "-d <base dir>"
    try:
        opts, args = getopt.getopt(argv, "hd:", ["dir="])
    except getopt.GetoptError:
        print(usage_str)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage_str)
            sys.exit()
        elif opt in ("-d", "--dir"):
            base_dir = arg

    if base_dir is None:
        sys.exit(2)

    my_columns = ['dummy', 'file']
    my_list = []

    for f in os.listdir(base_dir):
        if os.path.isfile(os.path.join(base_dir, f)):
            # print(f)
            row = [1, f]
            my_list.append(row)

    df = pd.DataFrame(my_list, columns=my_columns)
    df.to_csv(os.path.join(base_dir, 'data.csv'), index=False)


if __name__ == "__main__":
    main(sys.argv[1:])
