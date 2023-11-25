import os
def get_base_path(file):
    return os.path.dirname(os.path.abspath(file))

def get_prev_path(file):
    return os.path.dirname(os.path.dirname(os.path.abspath(file)))