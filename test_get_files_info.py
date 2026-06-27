from functions.get_files_info import get_files_info

def print_result(path:str) -> None:
  files_details = get_files_info("calculator", path)
  splitted_details = "\n".join(f"    {l}" for l in files_details.splitlines())
  
  print_result = ""
  
  if path == ".":
    print_result = f"Result for current directory:\n{splitted_details}"
  else:
    print_result = f"Result for '{path}' directory:\n{splitted_details}"
    
  print(print_result)


print_result(".")
print_result("pkg")
print_result("/bin")
print_result("../")
