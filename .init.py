import shutil, sys, os

path = f'./{sys.argv[1]}'
files = os.listdir(path)
dirs = [f for f in files if os.path.isdir(os.path.join(path, f))]
for dir in dirs:
  shutil.copy('./.template/main.py', f'{path}/{dir}')