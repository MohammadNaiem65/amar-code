from os import path

from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
  try:
    working_dir_abs_path = path.abspath(working_directory)
    file_abs_path = path.normpath(path.join(working_dir_abs_path, file_path))
    
    common_path = path.commonpath([working_dir_abs_path, file_abs_path])
    is_within_workspace = common_path == working_dir_abs_path
    
    if not is_within_workspace:
      return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    is_file = path.isfile(file_abs_path)
    
    if not is_file:
      return f'Error: File not found or is not a regular file: "{file_path}"'

    with open(file_abs_path) as file:
      content = file.read(MAX_CHARS)
      
      # After reading the first MAX_CHARS...
      if file.read(1):
        content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
      return content
  except Exception as error:
    return f"Error: {error}"
