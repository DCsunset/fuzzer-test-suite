import time
import subprocess
import shlex
import re
import sys
import os
import glob

# usage:  python3 collect_cov.py <project_name>
def main(argv):
    if len(argv) < 1:
        print("Please input the project name (eg. json-2017-02-12)")
        return

    project_name = argv[0] # eg. "json-2017-02-12"
    project_path = "./RUN_EXPERIMENT/RUNDIR-" + project_name + "/"  # hardcode path eg. /RUN_EXPERIMENT/RUNDIR-json-2017-02-12/
    project_short_name = project_name.split("-")[0]  # eg. json
    project_name_afl =  project_name + "-afl"  # eg. json-2017-02-12-afl
    corpus_folder_name = "CORPUS-" + project_name_afl # eg. CORPUS-json-2017-02-12-afl
    report_file_name = project_name + "_report.txt" # output file for analysis eg. json-2017-02-12_report.txt
    count = 0
    while(count >= 0):
        now = int (time.time())
        f = open(report_file_name, "a")

        # afl-collect -r ./CORPUS-boringssl-2016-02-12-afl ./collect_crash -- boringssl-2016-02-12-afl @@
        command_line_afl =  "afl-collect -r " + project_path + corpus_folder_name + " ./collect_crash -- " + project_path + project_name_afl + " @@" 
        split_afl = shlex.split(command_line_afl)
        process = subprocess.run(split_afl, capture_output=True)
        output = process.stdout.decode("utf-8")
        error = process.stderr.decode("utf-8")
        print("error: " + error)
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
        # since gcov could not recognize *, manully loop the gcda file one by one
        for file in glob.glob( project_path + "*.gcda"):
            command_line_gcov = "gcov -b " + file
            print("EXCUTE: " + command_line_gcov)
            splited_gcov = shlex.split(command_line_gcov)
            process_gcov = subprocess.run(splited_gcov, capture_output=True, cwd=os.getcwd())
            output = process_gcov.stdout.decode("utf-8")
            error = process_gcov.stderr.decode("utf-8")
            print("Error: " + error)

            # Split the files information
            blocks = output.split("\n\n")
            # Drop the library files information
            for block in blocks:
                if re.search("/usr/include", block) is None:
                    # write the coverage info to report
                    match = re.search("(Lines executed:(\d+\.*\d*)% of \d+)", block)
                    if (match):
                        f.write(str(now) + " " + match.group(0) + "\n")
                    match = re.search("(Branches executed:(\d+\.*\d*)% of \d+)", block)
                    if (match):
                        f.write(str(now) + " " + match.group(0) + "\n")
                    match = re.search("(Taken at least once:(\d+\.*\d*)% of \d+)", block)
                    if (match):
                        f.write(str(now) + " " + match.group(0) + "\n")

        f.close()
        count += 1
        print(str(now) + "   round " + str(count))
        time.sleep(300) # sleep for 5 mins

if __name__ == "__main__":
   main(sys.argv[1:])