from datetime import datetimedatetime
from time import time


def div_log1 (r1, r2, result):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} / {} = {} Time {}\n'.format(r1, r2, result, time_calc))

def div_log2 (r1, r2, result):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} // {} = {} Time {}\n'.format(r1, r2, result, time_calc))

def div_log3 (r1, r2, result):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} % {} = {} Time {}\n'.format(r1, r2, result, time_calc))


def mult_log(r1, r2, result):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} * {} = {} Time {}\n'.format(r1, r2, result, time_calc))


def sub_log(r1, r2, result):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} - {} = {} Time {}\n'.format(r1, r2, result, time_calc))


def sum_log(r1, r2, result):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} + {} = {} Time {}\n'.format(r1, r2, result, time_calc))


def pow_log(r1, r2, result):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} ** {} = {} Time {}\n'.format(r1, r2, result, time_calc))


def sgrt_log(r1, result):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} ** 0,5 = {} Time {}\n'.format(r1, result, time_calc))


def error_enter():
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('Enter error at {}\n'.format(time_calc))


def start_app():
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('Start work with app at {}\n'.format(time_calc))

def next_step():
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('User make new choice at {}\n'.format(time_calc))