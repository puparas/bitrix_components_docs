import os
import re

def clean_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regex to match tables and code blocks
    table_regex = r'(\|.*?\|(?:\n\|.*?\|)+)'
    code_block_regex = r'(```.*?```|~~~.*?~~~)'

    # Find all tables and code blocks
    tables = re.findall(table_regex, content, re.DOTALL)
    code_blocks = re.findall(code_block_regex, content, re.DOTALL)

    # Combine tables and code blocks
    cleaned_content = '\n\n'.join(tables + code_blocks)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

def traverse_and_clean(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                clean_md_file(file_path)

if __name__ == '__main__':
    # Specify the root directory to start the search
    root_directory = 'f:/PHP_projects/puparasbitrix_components_docs/bitrix_docs'
    traverse_and_clean(root_directory)