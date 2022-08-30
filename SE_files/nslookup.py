from re import RegexFlag
import subprocess


domain_name = input("Enter the domain name: ")

command = "nslookup {}".format(domain_name)
# Shell changed to False. Makes it possible only to give 1 argument.
# And makes it possible to run the file on Windows.
response = subprocess.check_output(command, shell=False, encoding="UTF-8")

print(response)

