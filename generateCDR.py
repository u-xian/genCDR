from config import ReadConfig
from savingCDRFiles import savingFile
import generateData
import call_detail_records

options = config = ReadConfig.getConfig('./config/menuOptions.json')

print("--- MENU ---")
for item_id, details in options.items():
    print(f"[{item_id}]  {details['name']}")
    
# 3. Get input and handle logic
choice = input("\nPlease enter your choice (1, 2, or 3 ): ")
numRecords = int(input("\nPlease enter the number of records to generate: "))
# 4. Use the dictionary's .get() method for safety
calltype = options.get(choice)['configfile']
file_name = options.get(choice)['file_name']

data = generateData.generate_cdrs_data(calltype,numRecords)

full_path = savingFile.saveFile(file_name)

savingFile.save_to_csv(full_path, data)