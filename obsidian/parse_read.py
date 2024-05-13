import os
import re
import sys
from dotenv import load_dotenv
from markdown2 import markdown

load_dotenv()
directory_path = os.getenv('DIRECTORY_PATH')

print('Folders in Notes:')
print([name for name in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, name))])