from functools import partial
import os


def record_directory(child_content:str, parent_dir) -> str:
  child_dir = os.path.join(parent_dir, child_content)
  is_dir = os.path.isdir(child_dir)
  size = os.path.getsize(child_dir)
  
  result = f"- {child_content}: file_size={size}, is_dir={is_dir}"
  
  return result
  

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
    
    target_dir_content = os.listdir(target_dir)
    
    target_dir_content_details = "\n".join(list(map(partial(record_directory, parent_dir=target_dir), target_dir_content)))
        
    return target_dir_content_details
  except Exception as error:
    return f"Error: {error}"

