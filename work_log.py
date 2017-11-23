# Imports

from collections import OrderedDict
import os

from tasks import Tasks, initialize


def clear_screen():
    '''Clears the command screen'''
    os.system('cls' if os.name == 'nt' else 'clear')


def new_task(employee=None, task_name=None,
             time_elapsed=None, notes=None):
    '''Report a new task'''
    if not employee:
        clear_screen()
        employee = input('What is your name?\n> ').strip()
    if not task_name:
        clear_screen()
        task_name = input('What is the task?\n> ').strip()
    if not time_elapsed:
        try:
            clear_screen()
            time_elapsed = int(input('How long (minutes) was '
                                     'spent on the task?\n> '))
        except ValueError:
            clear_screen()
            print('Not a valid amount of time.')
            input('Press any key to go back to main menu.\n')
            return menu_loop()

    if not notes:
        clear_screen()
        notes = input('Notes you would like to add?\n> ').strip()
    Tasks.create(employee=employee,
                 task_name=task_name,
                 time_elapsed=time_elapsed,
                 notes=notes)
    input('Your entry is added. Press any key to continue.\n')


def display_task(search_task=None, search_date=None,
                 search_time_spent=None, search_employee=None):
    '''View reported tasks'''
    tasks = Tasks.select().order_by(Tasks.timestamp.desc())
    if search_task:
        tasks = tasks.where(Tasks.task_name.contains(search_task)
                            + Tasks.notes.contains(search_task))
    elif search_employee:
        tasks = tasks.where(Tasks.employee.contains(search_employee))
    elif search_date:
        tasks = tasks.where(Tasks.date == search_date)
    elif search_time_spent:
        tasks = tasks.where(Tasks.time_elapsed == search_time_spent)

    for task in tasks:
        timestamp = task.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear_screen()
        print(timestamp)
        print('=' * len(timestamp))
        print('Task: ' + task.task_name)
        print('Employee: ' + task.employee)
        print('Time to complete: ' + task.time_elapsed + ' minutes')
        print('Notes: ' + task.notes)
        print('=' * len(timestamp))
        print('1. Next entry')
        print('2. Delete entry')
        print('3. Return to main menu')
        next_act = input('> ')

        if next_act == '3':
            break
        elif next_act == '2':
            delete_task(task)


def delete_task(task):
    '''Deletes the task'''
    if input('Are you sure? [Y/n] > ').lower() == 'y':
        task.delete_instance()
        clear_screen()
        input('Task deleted. Press any key to continue.')


def menu_loop():
    '''Beginning menu when app is launched'''
    menu_select = None
    while menu_select != 'q':
        print('Welcome to the Work Log Database!\n'
              'Enter "Q" to quit.\n\n'
              'Select "a", "b", or "c"')
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        menu_select = input('> ').lower().strip()
        if menu_select in menu:
            clear_screen()
            menu[menu_select]()


def search_menu_loop():
    '''Search for a record'''
    menu_select = None
    while menu_select != 'q':
        print('How would you like to search?\n'
              'Enter "Q" to return to main menu.\n\n'
              'Select "a", "b", "c", or "d"')
        for key, value in search_menu.items():
            print('{}) {}'.format(key, value.__doc__))
        menu_select = input('> ').lower().strip()
        if menu_select in search_menu:
            clear_screen()
            search_menu[menu_select]()


def exact_date():
    '''Search by exact entry date'''
    tasks = Tasks.select().order_by(Tasks.timestamp.desc())
    date_list = []
    clear_screen()
    print('Available dates to choose from:')
    for task in tasks:
        date_list.append(task.timestamp.strftime('%m/%d/%y'))
    print('\n'.join(set(date_list)))
    display_task(search_date=input('Search Date (MM/DD/YY): '))


def time_spent():
    '''Search by time spent'''
    clear_screen()
    display_task(search_time_spent=input('Please enter exact minutes spent: '))


def task_term():
    '''Search by task name or notes'''
    clear_screen()
    display_task(search_task=input('Enter search term: '))


def employee():
    '''Search by employee'''
    tasks = Tasks.select().order_by(Tasks.timestamp.desc())
    employee_list = []
    clear_screen()
    print('Available employees to choose from:')
    for task in tasks:
        employee_list.append(task.employee)
    print('\n'.join(set(employee_list)))
    display_task(search_employee=input('Search Employee Name: '))


menu = OrderedDict([
    ('a', new_task),
    ('b', display_task),
    ('c', search_menu_loop)
])

search_menu = OrderedDict([
    ('a', exact_date),
    ('b', task_term),
    ('c', employee),
    ('d', time_spent),
])


if __name__ == '__main__':
    initialize()
    menu_loop()
