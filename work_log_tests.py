# Imports
from unittest import main, TestCase, mock
from work_log import clear_screen, new_task, menu_loop
                     search_menu_loop, display_task


class TestClearScreen(TestCase):
    @mock.patch('work_logs.os')
    def test_clear_screen(self, mock_os):
        mock_os.name = 'nt'
        clear_screen()
        mock_os.system.assert_called_once_with('cls')

    @mock.patch('work_logs.os')
    def test_clear_screen_not_nt(self, mock_os):
        mock_os.name = 'bob'
        clear_screen()
        mock_os.system.assert_called_once_with('clear')

class NewTaskTest(unittest.TestCase):
    def setUp(self):
        self.employee = 'michael'
        self.task_name = 'python class'
        self.time_elapsed = '40'
        self.notes='none'

    def test_new_task(self):
        new_task(employee_name='Bryce',
                 notes='none',
                 task_name='Coding',
                 time_elapsed='15')





if __name__ == '__main__':
    unittest.main()