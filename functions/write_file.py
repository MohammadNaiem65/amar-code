from os import path
import os

from pydantic import FilePath


def write_file(working_directory: str, file_path: str, content: str) -> str:
  try:
    # Validate the `file_path` exists under working directory
    working_dir_abs_path = path.abspath(working_directory)
    target_file_abs_path = path.normpath(path.join(working_dir_abs_path, file_path))
    
    common_path = path.commonpath([working_dir_abs_path, target_file_abs_path])
    
    is_under_working_dir = common_path == working_dir_abs_path
    
    if not is_under_working_dir:
      return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    # Validate if the `file_path` is not a directory
    is_dir = path.isdir(target_file_abs_path)
    
    if is_dir:
      return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    # Create required directories and file with it's content
    os.makedirs(path.dirname(target_file_abs_path), exist_ok=True)
    
    with open(target_file_abs_path, 'w') as file:
      file.write(content)
      
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  except Exception as error:
    return f"Error: {error}"
  
