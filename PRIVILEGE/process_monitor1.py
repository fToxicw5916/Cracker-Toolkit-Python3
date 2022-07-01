'''
A script that monitors your computer's process.
'''
import os
import sys

import win32api  # Windows API
import win32con
import win32security  # Windows security

import wmi  # For process monitoring


def log_to_file(message):
    '''
    Write a log to a file
    '''
    with open('process_monitor_log.csv', 'a') as fd:
        fd.write(f'{message}\r\n')


def monitor():
    '''
    Main function
    '''
    log_to_file('CommandLine, Time, Executable, Parent PID, PID, User, Privileges')
    c = wmi.WMI()  # Create monitor object
    process_watcher = c.Win32_Process.watch_for('creation')
    while True:
        try:
            new_process = process_watcher()
            cmdline = new_process.CommandLine
            create_date = new_process.CreationDate
            executable = new_process.ExecutablePath
            parent_pid = new_process.ParentProcessId
            pid = new_process.ProcessId
            proc_owner = new_process.GetOwner()

            privileges = 'N/A'
            process_log_message = (
                f'{cmdline} , {create_date} , {executable},'
                f'{parent_pid} , {pid} , {proc_owner} , {privileges}'
                )
            print(process_log_message)
            print()
            log_to_file(process_log_message)
        except Exception:  # Skip error
            pass


if __name__ == '__main__':
    monitor()
