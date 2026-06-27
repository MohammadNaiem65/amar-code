from functions.get_file_content import get_file_content

def print_result(path:str) -> None:
  files_details = get_file_content("calculator", path)
  splitted_details = "\n".join(f"    {l}" for l in files_details.splitlines())
  
  print_result = ""
  
  if path == ".":
    print_result = f"Result for current directory:\n{splitted_details}"
  else:
    print_result = f"Result for '{path}' directory:\n{splitted_details}"
    
  print(print_result)

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

print_result("main.py")
print_result("pkg/calculator.py")
print_result("/bin/cat")
print_result("pkg/does_not_exist.py")

