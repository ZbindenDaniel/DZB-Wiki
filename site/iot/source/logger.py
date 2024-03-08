
import os

class logger:
    def __init__(self, name, logLevel = 0, alwaysPrint = False) -> None:
        self.__debugQ = []
        self.__warningQ = []
        self.__errorQ = []
        self.file_name = name
        self.logLevel =  int(logLevel)
        self.aPrint = alwaysPrint

    def debug(self, message):
        self.__debugQ.append(f'{message}\n')
        if self.logLevel > 1 and self.aPrint:
            print(message)

    def warning(self, message):
        self.__warningQ.append(f'{message}\n')
        if self.logLevel > 0 and self.aPrint:
            print(message)

    def error(self, message):
        self.__errorQ.append(f'{message}\n')
        if self.aPrint:
            print(message)

    def toFile(self):
        if self.logLevel > 1:
            logfile = open(f'logs/{self.file_name}_d.log','w')
            logfile.write(f'{self.__debugQ}')
            logfile.close()
        if self.logLevel > 0:
            logfile = open(f'logs/{self.file_name}_w.log','w')
            logfile.write(f'{self.__warningQ}')
            logfile.close()
        logfile = open(f'logs/{self.file_name}_e.log','w')
        logfile.write(f'{self.__errorQ}')
        logfile.close()

    def toFileWhenError(self):
        if any(self.__errorQ):
            logfile = open(f'logs/{self.file_name}_e.log','w')
            logfile.write(f'{self.__errorQ}')
            logfile.close()
