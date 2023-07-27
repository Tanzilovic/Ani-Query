import re

class Get:
    def text(file: str):
        quality= "1080p"
        with open(f"{file}", "r") as fl:
            for _, line in enumerate(fl):
                if f'{quality}'in line:
                    true_line = re.findall(f"'([^']*)'", line)
                    print(f'url: {true_line}')