import json
import sys
from pathlib import Path

def update_json_file(date):
    json_file_path = './date.json' 
    json_file = Path(json_file_path)
    if not json_file.is_file():
        data = {"date": []}
    else:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
    
    if date not in data['date']:
        data['date'].append(date)
        data['date'].sort() 

    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_json.py <date>")
        sys.exit(1)
    
    date = sys.argv[1]
    update_json_file(date)