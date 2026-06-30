import os
#pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()
demo_key = os.environ.get("MY_API")
if(demo_key):
    print("Found",demo_key)
else:
    print("NOT")    