import sys


class ErrorHandling:
    r"""
    Basic error handling class.
    
    Contains:
    
    + write_console: write a message to the console.
    + write_file: write a message to the log file.
    + write_all: write a message to the console and to the log file.
    + exit: exit with error message.
    + warning: write a warning to the console.
    
    To run:

    .. code-block:: python

       def some_function():
           import Handling

           # creates log file
           tmp = Handling.ErrorHandling('./test.txt')
           # writes to console
           tmp.write_console('test line in console')
           # writes to log file
           tmp.write_file('test line in log file')
           # writes to console and log file
           tmp.write_all('test line in console and log file')
           # warning
           tmp.warning('this is a warning')
           # error
           tmp.error('this is an error')

    """

    def __init__(self, file_path):
        f = open(file_path, 'w')
        self.file = f

    @staticmethod
    def write_console( message):
        print(message)
        return

    def write_file(self, message):
        self.file.write(message + '\n')
        return

    def write_all(self, message):
        print(message)
        self.file.write(message + '\n')
        return

    def exit(self, message):
        # print('Exit: ' + message)
        self.file.write('Exit: ' + message + '\n')
        self.file.close()
        raise SystemExit('Exit: ' + message + '\n')
        return

    def warning(self, message):
        print('Warning: ' + message)
        self.file.write('Warning: ' + message + '\n')
        return

    def close(self):
        self.file.close()
        return
