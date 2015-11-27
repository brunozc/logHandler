# unit test for Handling
import unittest
import Handling
import os
import sys
# add the src folder to the path to search for files
sys.path.append('../')


class TestHandler(unittest.TestCase):
    def setUp(self):
        self.file_path = './test.txt'

    def test_write_to_console(self):

        #
        # # self.tmp1.write_console('Message to console')
        # import os
        # p = os.popen(self.tmp1.write_console('Message to console'))
        # s = p.readline()
        # p.close()
        #
        # proc = subprocess.Popen(1, shell=True, stdout=subprocess.PIPE, )
        # output = proc.communicate()[0]
        # print(output)
        #
        # self.assertEqual(output, 'Message to console')
        pass

    def test_write_file(self):
        loge = Handling.ErrorHandling(self.file_path)

        loge.write_file('Text file message')
        loge.write_file('Text file message - new line')
        loge.close()

        # check if file exist
        self.assertTrue(os.path.isfile(self.file_path))

        # check if file is correctly written
        with open(self.file_path) as f:
            file = f.readlines()

        self.assertTrue(file[0].split('\n')[0], 'Text file message')
        self.assertTrue(file[1].split('\n')[0], 'Text file message - new line')
        return

    def test_warning(self):
        log = Handling.ErrorHandling(self.file_path)

        log.warning('warning message')
        log.write_file('warning message - new line')
        log.close()

        # check if file exist
        self.assertTrue(os.path.isfile(self.file_path))

        # check if file is correctly written
        with open(self.file_path) as f:
            file = f.readlines()

        self.assertTrue(file[0].split('\n')[0], 'Warning: warning message')
        self.assertTrue(file[1].split('\n')[0], 'Warning: warning message - new line')
        return

    def test_exit(self):
        log = Handling.ErrorHandling(self.file_path)

        # check is exit message is raised
        with self.assertRaises(SystemExit) as cm:
            log.exit('error message')
        self.assertEqual(cm.exception.code, 'Exit: error message\n')

        # check if file exist
        self.assertTrue(os.path.isfile(self.file_path))

        return

    def tearDown(self):
        if os.path.isfile('./test.txt'):
            os.remove('./test.txt')


if __name__ == '__main__':
    unittest.main()
