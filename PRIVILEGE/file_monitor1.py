# Modified example, original given here:
# http://timgolden.me.uk/python/win32_how_do_i/watch_directory_for_changes.html
'''
Look for bugs when running a file.
'''
import os
import tempfile  # Create TEMP files
import threading  # Multithread
import win32con
import win32file  # File control on Windows

FILE_CREATED = 1
FILE_DELETED = 2
FILE_MODIFIED = 3
FILE_RENAMED_FROM = 4
FILE_RENAMED_TO = 5

FILE_LIST_DIRECTORY = 0x0001
PATHS = ['c:\\Windows\\Temp', tempfile.gettempdir()]


def monitor(path_to_watch):
    '''
    Main function
    '''
    h_directory = win32file.CreateFile(
        path_to_watch,
        FILE_LIST_DIRECTORY,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None,
        win32con.OPEN_EXISTING,
        win32con.FILE_FLAG_BACKUP_SEMANTICS,
        None
        )

    while True:
        try:
            results = win32file.ReadDirectoryChangesW(
                h_directory,
                1024,
                True,
                win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
                win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
                win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
                win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
                win32con.FILE_NOTIFY_CHANGE_SECURITY |
                win32con.FILE_NOTIFY_CHANGE_SIZE,
                None,
                None
            )
            for action, file_name in results:
                full_filename = os.path.join(path_to_watch, file_name)
                if action == FILE_CREATED:  # Created a file
                    print(f'[+] Created {full_filename}')
                   
                elif action == FILE_DELETED:  # Deleted a file
                    print(f'[-] Deleted {full_filename}')
                    
                elif action == FILE_MODIFIED:  # Modified a file
                    print(f'[*] Modified {full_filename}')
                    try:
                        with open(full_filename) as f:
                            contents = f.read()
                        print('[vvv] Dumping contents ... ')   # Print the contents of the changed file
                        print(contents)
                        print('[^^^] Dump complete.')
                    except Exception as e:
                        print(f'[!!!] Dump failed. {e}')
                    
                elif action == FILE_RENAMED_FROM:  # Renamed from another file
                    print(f'[>] Renamed from {full_filename}')
                elif action == FILE_RENAMED_TO:  # Renamed to another file
                    print(f'[<] Renamed to {full_filename}')
                else:
                    print(f'[?] Unknown action on {full_filename}')
        except KeyboardInterrupt:  # Stop by CTRL-C
            break
    
        except Exception:  # Bypass errors
            pass


if __name__ == '__main__':
    for path in PATHS:
        monitor_thread = threading.Thread(target=monitor, args=(path,))  # Generate thread
        monitor_thread.start()  # Start thread
