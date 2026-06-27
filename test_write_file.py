
from functions.write_file import write_file


def print_result(path:str, content:str) -> None:
  result = write_file("calculator", path, content)
  
  print(result)


print_result("lorem.txt", "wait, this isn't lorem ipsum")
print_result("pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print_result("/tmp/temp.txt", "this should not be allowed")
