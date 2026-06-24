import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
  try:
    work_dir_abspath = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(work_dir_abspath, directory))
  
    valid_target_dir = os.path.commonpath([work_dir_abspath, target_dir]) == work_dir_abspath
  
    if not valid_target_dir:
      return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    target_dir_exists = os.path.isdir(target_dir)
    
    if not target_dir_exists:
      return f'Error: "{directory}" is not a directory'
    
    return f'Success: "{directory}" is within the working directory'
  except Exception as error:
    return f"Error: {error}"

