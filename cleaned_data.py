'''
Takes the scraped data, cleans the data if needed, and creates a directory,
prompt_directory with a file for each prompt
'''
import pandas as pd
import os

df = pd.read_csv('Justia_data.csv')

new_directory = 'prompt_directory'
os.makedirs(new_directory, exist_ok=True)


i = 0
for index, row in df.iterrows():
    #Create dictionary
    dict = {}
    dict['question'] = row['question_title'] + row['question_description']
    dict['answer'] = row['answer']

    if i >= len(df):
        break
    else:
        file_name = str(i) + '.txt'
        file_path = os.path.join(new_directory, file_name)

        with open(file_path, 'w') as f:
            f.write(str(dict))

        i += 1



