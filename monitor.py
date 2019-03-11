import inotify.adapters
import os
import sys

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)


def main(dir_to_watch):
    """
    Use inotify to watch the provided directory for changes
    """
    i = inotify.adapters.Inotify()

    i.add_watch(dir_to_watch)

    events = i.event_gen(yield_nones=False, timeout_s=1)
    events = list(events)
    if events:
        try:
            # Read the file event tuple
            event = events[1][1]
            dir_accessed = events[1][2]
            file_accessed = events[1]
            file_abs_path = "{}/{}".format(dir_accessed, file_accessed[3])
            f_size = file_size(file_abs_path)
            f_event = event[0][3:]
            print("{} -- {} -- {}".format(f_event, f_abs_path, f_size))
        except Exception as ex:
            pass

if __name__ == '__main__':
    try:
       dir_to_watch = sys.argv[1]
       while(1):
           main(dir_to_watch)
    except Exception as e:
       print("Error watching ...invalid command line argument")
