import argparse
import subprocess

from zowe.zos_jobs_for_zowe_sdk import Jobs

from config import connection
from find_error_code import get_error_code
from scrape import fetch_help

parser = argparse.ArgumentParser(
    description="Submit jobs to Mainframe and in case of error get the details on the error code."
)
parser.add_argument("type", choices=['local', 'mainframe'],
                    help="place where the job file is residing")
parser.add_argument("path", help="complete path of the JCL file")

args = parser.parse_args()
my_jobs = Jobs(connection)
print("Submitting your job...", end='\r')
if args.type == "mainframe":
    job = my_jobs.submit_from_mainframe(args.path)
elif args.type == "local":
    job = my_jobs.submit_from_local_file(args.path)
print(job["phase-name"], end='\r')
i = 0
while job["retcode"] is None:
    status = my_jobs.get_job_status(job["jobname"], job["jobid"])
    if status["retcode"] is not None:
        print("Job processing is complete.")
        break
    if i == 1:
        print("Waiting for job to complete.", end='\r')
    elif i == 2:
        print("Waiting for job to complete..", end='\r')
    elif i == 3:
        print("Waiting for job to complete...", end='\r')
        i = 0
    i += 1

if status["retcode"] == "CC 0000":
    print("Job was successfully completed!!!")
else:
    print(status)
    print("Downloading Job output files for analysis...", end='\r')
    subprocess.call(["zowe", "jobs", "download", "output", str(job["jobid"])])
    error_code = get_error_code(job["jobid"])
    print("Error Code: " + str(error_code))
    fetch_help(error_code)
