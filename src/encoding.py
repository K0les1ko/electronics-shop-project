import os

def instantiate_from_csv():
    file_path = os.path.join(os.path.dirname(__file__), 'items.csv')

    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        print(file_content)

instantiate_from_csv()