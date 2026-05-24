import os
from pathlib import Path

def get_files_info(working_directory: str, directory: str = '.') -> str:
    try:
        wd_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(wd_path, directory))

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        # Will be True or False
        valid_target_dir = os.path.commonpath([wd_path, target_dir]) == wd_path

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:
            file_info = []
            with os.scandir(target_dir) as it:
                for entry in it:
                    file_info.append(f'- {entry.name}: file_size={entry.stat().st_size} bytes, is_dir={entry.is_dir()}')
            return '\n'.join(file_info)

            # return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f'Error: {e}'
