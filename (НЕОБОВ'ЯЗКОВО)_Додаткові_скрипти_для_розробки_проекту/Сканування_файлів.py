import os

def extract_file_contents(directory, output_file):
    with open(output_file, 'a', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(directory):
            if not files:
                print(f'No files found in directory: {root}')
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except Exception as e:
                    content = f'Error reading file: {e}'
                
                outfile.write('==========\n')
                outfile.write(f'1) {file}\n')
                outfile.write(f'2) {file_path}\n')
                outfile.write(f'3) {content}\n')
                outfile.write('==========\n\n')
                
                print(f'Processed file: {file_path}')

if __name__ == '__main__':
    directory_to_search = r'C:\Users\Lenovo\Desktop\Home_Work_ 2\quotes_site\templates'  # Заміни на шлях до твоєї директорії
    output_file = 'document.txt'
    extract_file_contents(directory_to_search, output_file)
