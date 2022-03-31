import time
import subprocess
import shlex
import re
import sys

# usage:  python3 collect_cov.py <project_name>
def main(argv):
    if len(argv) < 1:
        print("Please input the project name (eg. json-2017-02-12)")
        return

    project_name = argv[0] # eg. "json-2017-02-12"
    project_path = "/RUN_EXPERIMENT/RUNDIR-" + project_name + "/"  # hardcode path eg. /RUN_EXPERIMENT/RUNDIR-json-2017-02-12/
    project_short_name = project_name.split("-")[0]
    project_name_afl =  project_name + "-afl"
    corpus_folder_name = "CORPUS-" + project_name_afl
    report_file_name = project_name + "_report.txt" # output file for analysis
    count = 0
    while(count >= 0):
        now = int (time.time())
        f = open(report_file_name, "a")

        # afl-collect -r ./CORPUS-boringssl-2016-02-12-afl ./collect_crash -- boringssl-2016-02-12-afl @@
        command_line_afl =  "afl-collect -r ." + project_path + corpus_folder_name + " ./collect_crash -- " + project_path + project_name_afl + " @@" 
        split_afl = shlex.split(command_line_afl)
        process = subprocess.run(split_afl, capture_output=True)
        output = process.stdout.decode("utf-8")
        # write the crash info to report
        if (re.search("No samples", output)):
            f.write(str(now) + " No samples found. Check directory settings!\n")
        elif (re.search("No unseen", output)):
            f.write(str(now) + "No unseen samples found. Check your database for results!\n")
        else:
            match = re.search("Successfully indexed (\d+) crash samples.", output)
            if match:
                f.write(str(now) + " " + match.group(0) + "\n")

        # gcov -b 
        # command_line_gcov = "gcov -b RUNDIR-sqlite-2016-11-14/sqlite3" # for testing
        command_line_gcov = "gcov -b " + project_path + project_short_name
        splited_gcov = shlex.split(command_line_gcov)
        process_gcov = subprocess.run(splited_gcov, capture_output=True)
        output = process_gcov.stdout.decode("utf-8")
        # write the coverage info to report
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
        count += 1
        print(str(now) + "   round " + str(count))
        time.sleep(300) # sleep for 5 mins

if __name__ == "__main__":
   main(sys.argv[1:])