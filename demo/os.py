import os

# Get the current working directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Try creating the "testdir" directory
try:
  os.mkdir("testdir")
  print("Directory 'testdir' created successfully.")
except FileExistsError:
  print("Directory 'testdir' already exists.")

# List the contents of the current directory
print("\nDirectory contents after creating (or finding) 'testdir':")
print(os.listdir())

# Remove the "testdir" directory (if it exists)
try:
  os.rmdir("testdir")
  print("Directory 'testdir' removed successfully.")
except OSError as e:
  # Handle other potential errors like directory not empty
  if e.errno == 39:  # Directory not empty (errno 39 on some systems)
    print("Directory 'testdir' could not be removed as it's not empty.")
  else:
    print(f"An error occurred while removing 'testdir': {e}")

# List the contents of the current directory after removal
print("\nDirectory contents after removing 'testdir':")
print(os.listdir())