import argparse


"""以下脚本可提取一个或多个文件名，并可选择要显示的行数"""
parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file'
)
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)