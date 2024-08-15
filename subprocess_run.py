import subprocess

# subprocess.run(["ls","-l","lab14"])

# command="uname"
# commandArgument="-a"
# print(f'Gathering system information with command: {command} {commandArgument}')
# subprocess.run([command,commandArgument])

command="ps"
commandArgument="-x"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])