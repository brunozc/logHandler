# logHandler

A simple log handler for python.


## Features

The handler offers the following possibilities:

+ write_console > write a message to the console.
+ write_file > write a message to the log file.
+ write_all > write a message to the console and to the log file.
+ exit > exit with error message.
+ warning > write a warning to the console.


## How to use it

First you need to initialise the handler:

    import Handling 
    
    log.Handling('./my_log_file')
    
To use the write to console handler call:

    log.write_console('your message')

The other handlers are called in a similar manner.
