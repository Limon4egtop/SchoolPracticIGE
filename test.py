import subprocess


files = ["2.py", "5.py"]  # файлы, которые нужно запустить
for file in files:
    subprocess.Popen(args=["start", "python", file], shell=True, stdout=subprocess.PIPE)