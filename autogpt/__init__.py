import os
import random
import sys
import os

from dotenv import load_dotenv

if "pytest" in sys.argv or "pytest" in sys.modules or os.getenv("CI"):
    print("Setting random seed to 42")
    random.seed(42)

# Load the users .env file into environment variables
load_dotenv(verbose=True, override=True)

os.environ["http_proxy"]="192.168.31.14:7890"
# os.environ["http_proxy"]="127.0.0.1:7890"
os.environ["https_proxy"]="192.168.31.14:7890"
# os.environ["https_proxy"]="192.168.31.14:7890"

del load_dotenv
