# Imports
from unittest import main, TestCase, mock
from work_log import clear_screen, new_task,\
                     menu_loop, search_menu_loop,\
                     display_task


class TestClearScreen(TestCase):
    @mock.patch('work_log.os')
    def test_clear_screen(self, mock_os):
        mock_os.name = 'nt'
        clear_screen()
        mock_os.system.assert_called_once_with('cls')

    @mock.patch('work_log.os')
    def test_clear_screen_not_nt(self, mock_os):
        mock_os.name = 'bob'
        clear_screen()
        mock_os.system.assert_called_once_with('clear')


class NewTaskTest(TestCase):
    @mock.patch('builtins.input')
    @mock.patch('work_log.clear_screen')
    @mock.patch('work_log.Tasks.create')
    def test_new_task(self, m_create, m_clear, m_input):
        m_input.side_effect = ['Michael', 'Assignment', 300,
                               'python_rocks!', 'c']
        new_task()
        m_create.assert_called_once_with(employee='Michael',
                                         task_name='Assignment',
                                         time_elapsed=300,
                                         notes='python_rocks!')
        self.assertEqual(4, m_clear.call_count)


class MenuTest(TestCase):
    @mock.patch('builtins.input')
    def test_menu(self, m_input):
        m_input.side_effect = 'q'
        menu_loop()
        self.assertRaises(SystemExit)

    @mock.patch('builtins.input')
    def test_search_menu(self, m_input):
        m_input.side_effect = 'q'
        search_menu_loop()
        self.assertRaises(SystemExit)


class DisplayTest(TestCase):
    @mock.patch('builtins.input')
    def test_display(self, m_input):
        m_input.side_effect = '3'
        display_task(search_employee='Michael')
        self.assertRaises(SystemExit)


if __name__ == '__main__':
    main()
