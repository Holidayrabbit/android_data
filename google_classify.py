from google_play_scraper import app
import json
from tqdm import tqdm
from collections import Counter
import os
import re


with open(r"D:\lab-projects\piggyback\code\data\bengin_data_per10_uk.json") as f:
    bengin_data = json.load(f)
with open(r"D:\lab-projects\piggyback\code\data\apg-meta_new.json") as f:
    dataset = json.load(f)
json_name = r"D:\lab-projects\piggyback\code\data\category.json"
json_list=[]
for sha in tqdm(bengin_data):
    item = [element for element in dataset if 'sha256' in element and element['sha256'] == sha]
    if 'pkg_name' in item[0]:
        app_id = item[0]['pkg_name']
        try:
            app_info = app(app_id)
            json_data = {"sha256": str(sha), "App Name": str(app_info['title']), "category": str(app_info['genre'])}
            json_list.append(json_data)
        except Exception as e:
            pass
print(len(json_list))
with open(json_name, 'w') as file:
    json.dump(json_list, file, indent=4)