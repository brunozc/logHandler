import Handling

log1 = Handling.ErrorHandling('./log_file_1.txt')
log2 = Handling.ErrorHandling('./log_file_2.txt')

log1.write_console('test console')
log2.write_console('test console')

log1.write_file('test file')
log2.write_file('test file')

log1.write_all('test all')
log2.write_all('test all')
log1.warning('This is a warning')
log1.exit('This is a system exit')
log1.close()
