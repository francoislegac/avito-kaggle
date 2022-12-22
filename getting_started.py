import pandas as pd
import psutil
import os

ROOT_DIR = "/mnt/f/avito-kaggle"

# UserInfo.tsv
user_info = pd.read_csv(f"{ROOT_DIR}/UserInfo.tsv", delimiter="\t", encoding="utf-8")
print(list(user_info.columns.values))  # file header
print(user_info.tail(35))  # last N rows

# Location.tsv
location = pd.read_csv(f"{ROOT_DIR}/Location.tsv", delimiter="\t", encoding="utf-8")
print(list(location.columns.values))  # file header
print(location.tail(35))  # last N rows

# category.tsv
category = pd.read_csv(f"{ROOT_DIR}/Category.tsv", delimiter="\t", encoding="utf-8")
print(list(category.columns.values))  # file header
print(category.tail(5))  # last N rows

# big csv file...
search_info = pd.read_csv(
    f"{ROOT_DIR}/SearchInfo.tsv", delimiter="\t", nrows=20, encoding="utf-8-sig"
)  # skiprows=1000000,
print(list(search_info.columns.values))  # file header
print(
    search_info[
        [search_info.columns[0], search_info.columns[1], search_info.columns[2]]
    ]
)

def print_python_mem_usage():
    process = psutil.Process(os.getpid())
    print(f"{process.memory_info().rss:.1e}")  # in bytes


print(print_python_mem_usage())