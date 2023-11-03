import re

def extract_strings_from_source_code(file_path):
    strings = []
    pattern = r'"(?:\\.|[^"\\])*"'  # 匹配双引号之间的文本

    with open(file_path, 'r') as file:
        code = file.read()
        matches = re.findall(pattern, code)

        for match in matches:
            string = match[1:-1]  # 去除双引号
            decoded_string = bytes(string, 'utf-8').decode('unicode_escape')  # 还原转义字符
            strings.append(decoded_string)

    return strings

# 示例用法
file_path = "your_source_code_file.py"
extracted_strings = extract_strings_from_source_code(file_path)
for string in extracted_strings:
    print(string)