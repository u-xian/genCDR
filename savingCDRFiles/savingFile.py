import os
import csv
from datetime import datetime
from savingCDRFiles import dircreate
import call_detail_records
from cdr import CallRecord

today = datetime.now()
cdr = CallRecord()

def saveFile(file_name):
    rundate  = today.strftime("%Y%m%d%I%M%S")
    filename = file_name +'_'+ rundate + '.csv'
    folder_name = "dumps"
    dir_path = dircreate.get_directory(folder_name)
    full_path = os.path.join(dir_path, filename)
    return full_path

def save_to_csv(filename, data):
    try:
        if not data:
            raise ValueError("No data provided to save.")
        headers = list(cdr.__dict__.keys())
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"Success: '{filename}' has been created.")

    except Exception as e:
        print(f"Error occurred: {e}")
        print("File creation aborted.")
        if os.path.exists(filename):
            os.remove(filename)