import re

class Res:
   def __init__(self, file: str, quality: str, backup: str):
       self.file = file
       self.quality = quality
       self.backup = backup
   
   def find(self) -> str:
       with open( self.file, "r" ) as fl:
            for _, line in enumerate(fl):
                if self.quality in line:
                    true_line = re.findall(f"'([^']*)'", line)
                    l: str = true_line[1]
                    return f'url ({self.quality}): {l.strip()}'
                elif self.quality not in line:
                    if self.backup in line:
                        true_line = re.findall(f"'([^']*)'", line)
                        l: str = true_line[1]
                        print(f'url ({self.backup}): {l.strip()}')
