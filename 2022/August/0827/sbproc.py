#項目52 subprocessを使って子プロセスを管理する

import subprocess

result = subprocess.run(
    ["echo", "Hello from the child!"],
    capture_output = True,
    encoding= "utf-8"
    )

result.check_returncode()
#print(result.stdout)

proc = subprocess.Popen(["sleep", "1"])
while proc.poll() is None:
    print("Working...")

print("Exit Status", proc.poll())