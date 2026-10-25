from ntpath import isfile
from automations.file_organizer import FileDetector
from pathlib import Path
class testing:
    def __init__(self) -> None  :
        folder = Path(r"D:\VS_code\Projects\File_Automation\sample_folder")
        for file in folder.iterdir():
            FileDetector(file)

if __name__ == "__main__":
    testing()