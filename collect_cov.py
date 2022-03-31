import time
import subprocess
import shlex
import re

now = int((time.time()))

report_file_name = "report.txt"
project_name = "json-2017-02-12-afl"
project_path = ""+ project_name

while(True):
    now = int (time.time())
    f = open(report_file_name, "a")

    # afl-collect
    command_line_afl =  "afl-collect -r ./CORPUS-" + project_name +" ./collect_crash/ -- " + project_name + " @@" 
    split_afl = shlex.split(command_line_afl)
    process = subprocess.run(split_afl, capture_output=True)
    output = process.stdout.decode("utf-8")
    if (re.search("No samples", output)):
        f.write(str(now) + " No samples found. Check directory settings!\n")
    elif (re.search("No unseen", output)):
        f.write(str(now) + "No unseen samples found. Check your database for results!\n")
    else:
        match = re.search("Successfully indexed (\d+) crash samples.", output)
        if match:
            f.write(str(now) + " " + match.group(0) + "\n")

    # gcov
    # command_line_gcov = "gcov -b " + project_path
    command_line_gcov = "gcov -b RUNDIR-sqlite-2016-11-14/sqlite3" # for testing
    splited_gcov = shlex.split(command_line_gcov)
    process_gcov = subprocess.run(splited_gcov, capture_output=True)
    output = process_gcov.stdout.decode("utf-8")
    match = re.search("(Lines executed:(\d+\.*\d*)% of \d+)", output)
    if (match):
        f.write(str(now) + " " + match.group(0) + "\n")
    match = re.search("(Branches executed:(\d+\.*\d*)% of \d+)", output)
    if (match):
        f.write(str(now) + " " + match.group(0) + "\n")
    match = re.search("(Taken at least once:(\d+\.*\d*)% of \d+)", output)
    if (match):
        f.write(str(now) + " " + match.group(0) + "\n")


    f.close()
    print(str(now))
    time.sleep(300) # sleep for 5 mins