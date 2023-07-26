import platform
import getpass

def getSystemInfo():
        uname = platform.uname()
        os = uname[0] + " " + uname[2] + " " + uname[3]
        computer_name = uname[1]
        user = getpass.getuser()
        return "Operating System:\t" + os +  "\nComputer Name:\t\t" + computer_name + "\nUser:\t\t\t\t" + user
