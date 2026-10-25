from pathlib import Path

#File Detector 
Extension_types ={
    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".webp": "Images",
    ".svg": "Images",
    ".ico": "Images",
    ".tiff": "Images",
    ".tif": "Images",
    ".heic": "Images",
    ".heif": "Images",
    ".raw": "Images",
    ".psd": "Images",
    ".ai": "Images",

    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".wmv": "Videos",
    ".flv": "Videos",
    ".webm": "Videos",
    ".m4v": "Videos",
    ".mpeg": "Videos",
    ".mpg": "Videos",
    ".3gp": "Videos",

    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".aac": "Audio",
    ".flac": "Audio",
    ".ogg": "Audio",
    ".m4a": "Audio",
    ".wma": "Audio",
    ".aiff": "Audio",
    ".opus": "Audio",
    ".mid": "Audio",
    ".midi": "Audio",

    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".odt": "Documents",
    ".rtf": "Documents",
    ".txt": "Documents",
    ".tex": "Documents",
    ".md": "Documents",
    ".pages": "Documents",

    # Spreadsheets
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
    ".ods": "Spreadsheets",
    ".tsv": "Spreadsheets",
    ".numbers": "Spreadsheets",

    # Presentations
    ".ppt": "Presentations",
    ".pptx": "Presentations",
    ".odp": "Presentations",
    ".key": "Presentations",

    # Archives and compressed files
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".bz2": "Archives",
    ".xz": "Archives",
    ".zst": "Archives",
    ".tgz": "Archives",
    ".iso": "Archives",

    # Programming and source code
    ".py": "Code",
    ".pyw": "Code",
    ".java": "Code",
    ".class": "Code",
    ".jar": "Code",
    ".c": "Code",
    ".h": "Code",
    ".cpp": "Code",
    ".hpp": "Code",
    ".cs": "Code",
    ".js": "Code",
    ".jsx": "Code",
    ".ts": "Code",
    ".tsx": "Code",
    ".html": "Code",
    ".css": "Code",
    ".scss": "Code",
    ".php": "Code",
    ".rb": "Code",
    ".go": "Code",
    ".rs": "Code",
    ".swift": "Code",
    ".kt": "Code",
    ".kts": "Code",
    ".dart": "Code",
    ".lua": "Code",
    ".pl": "Code",
    ".r": "Code",
    ".m": "Code",
    ".sh": "Code",
    ".bat": "Code",
    ".cmd": "Code",
    ".ps1": "Code",
    ".sql": "Code",
    ".ipynb": "Code",
    ".vue": "Code",
    ".svelte": "Code",

    # Configuration and structured data
    ".json": "Data",
    ".jsonl": "Data",
    ".xml": "Data",
    ".yaml": "Data",
    ".yml": "Data",
    ".toml": "Data",
    ".ini": "Data",
    ".cfg": "Data",
    ".conf": "Data",
    ".env": "Configuration",
    ".properties": "Configuration",

    # Executables and installers
    ".exe": "Applications",
    ".msi": "Applications",
    ".app": "Applications",
    ".apk": "Applications",
    ".aab": "Applications",
    ".deb": "Applications",
    ".rpm": "Applications",
    ".dmg": "Applications",
    ".appx": "Applications",
    ".msix": "Applications",

    # Fonts
    ".ttf": "Fonts",
    ".otf": "Fonts",
    ".woff": "Fonts",
    ".woff2": "Fonts",
    ".eot": "Fonts",

    # 3D models and design
    ".blend": "3D_Models",
    ".fbx": "3D_Models",
    ".obj": "3D_Models",
    ".stl": "3D_Models",
    ".gltf": "3D_Models",
    ".glb": "3D_Models",
    ".dae": "3D_Models",
    ".3ds": "3D_Models",
    ".max": "3D_Models",
    ".ma": "3D_Models",
    ".mb": "3D_Models",

    # Video editing and project files
    ".prproj": "Video_Projects",
    ".drp": "Video_Projects",
    ".aep": "Video_Projects",
    ".veg": "Video_Projects",

    # E-books
    ".epub": "Ebooks",
    ".mobi": "Ebooks",
    ".azw": "Ebooks",
    ".azw3": "Ebooks",

    # Disk images and backups
    ".vhd": "Disk_Images",
    ".vhdx": "Disk_Images",
    ".vmdk": "Disk_Images",
    ".vdi": "Disk_Images",
    ".bak": "Backups",
    ".backup": "Backups",
    ".old": "Backups",

    # Torrents
    ".torrent": "Torrents",

    # Log files
    ".log": "Logs",

    # Certificates and keys
    ".pem": "Certificates",
    ".crt": "Certificates",
    ".cer": "Certificates",
    ".pub": "Certificates",
    ".p12": "Certificates",
    ".pfx": "Certificates",
}

class Planner:
    def __init__(self, path):
        self.path =Path(path)
        self.Build_plan()
    
    def Build_plan(self):
        self.plan = []
        self.skipped = []
            # |----{Scanning for files to move}----|
        # We need to check if the path is a folder or a file
        if self.path.is_file(): # If the path contains only one file.
            self.files = [self.path]
        elif self.path.is_dir(): # If the path contains a folder dir
            self.files_ = Scanner(self.path).files

            # |----{Getting Category}----|
        # This separates between plan and skipped.
        for file in self.files_:
                if(self.check(file_path=file)):
                    self.plan.append(f"{file}:{File_Classifier(file).get_category()}")
                else:
                    self.skipped.append(file)

            # |----{Execution of Plan}----|
        # This will execute the move sequence for plan list
        if self.plan:
            # Format of p_file is that "File_Path : File_Category"
            for p_file in self.plan:
                self.p_path = Path(p_file.split(":")[0])
                self.p_cat = p_file.split(":")[1]
                Executor(self.p_cat, self.get_c_path(self.p_cat).mkdir(parents=True, exist_ok=True)).dry_run()
        else:
            print("No files planned to move.")

    # Checks for any hidden folders 
    def check(self, file_path):
        if Path(file_path).name.startswith("."):
            return False
        else:
            return True      
    
    # Get Path for the category
    def get_c_path(self, cat):
        self.cat = cat
        if self.cat == "Images":
            return Path(r"C:\Users\minax\OneDrive\Pictures\FOA_folder")

        elif self.cat == "Videos":
            return Path(r"C:\Users\minax\Videos\FOA_Folder")

        elif self.cat == "Audio":
            return Path(r"C:\Users\minax\Music\FOA_Folder")

        elif self.cat in ("Documents", "Spreadsheets", "Presentations", "Ebooks"):
            return Path(r"C:\Users\minax\OneDrive\Documents\FOA_Folder")

        elif self.cat == "Archives":
            return Path(r"C:\Users\minax\Downloads\FOA_Folder")

        elif self.cat == "Code":
            return Path(r"C:\Users\minax\Documents\FOA_Folder\Code")

        elif self.cat in ("Data", "Configuration"):
            return Path(r"C:\Users\minax\Documents\FOA_Folder\Data")

        elif self.cat == "Applications":
            return Path(r"C:\Users\minax\Downloads\FOA_Folder\Applications")

        elif self.cat == "Fonts":
            return Path(r"C:\Users\minax\Documents\FOA_Folder\Fonts")

        elif self.cat == "3D_Models":
            return Path(r"C:\Users\minax\Documents\FOA_Folder\3D_Models")

        elif self.cat == "Video_Projects":
            return Path(r"C:\Users\minax\Videos\FOA_Folder\Video_Projects")

        elif self.cat == "Disk_Images":
            return Path(r"C:\Users\minax\Documents\FOA_Folder\Disk_Images")

        elif self.cat == "Backups":
            return Path(r"C:\Users\minax\Documents\FOA_Folder\Backups")

        elif self.cat == "Torrents":
            return Path(r"C:\Users\minax\Downloads\FOA_Folder\Torrents")

        elif self.cat == "Logs":
            return Path(r"C:\Users\minax\Documents\FOA_Folder\Logs")

        elif self.cat == "Certificates":
            return Path(r"C:\Users\minax\Documents\FOA_Folder\Certificates")

        else:
            return Path(r"C:\Users\minax\Documents\FOA_Folder\Other")

class File_Classifier:
    def __init__(self, file_path):
        self.file_path = file_path
    def get_category(self):
        self.name = Path(self.file_path).name.lower()
        self.extension = Path(self.name).suffix  # Here remember basename will give the name of the file with extension and suffixes will give the extension but suffixes can't work with Path function
        return Extension_types.get(self.extension, "Others")
             
class Scanner:
    def __init__(self, file_path):
        self.file_path = file_path
        self.files = self.scan(self.file_path)
        recursive = False
    def scan(self, file_path):
        recursive = False
        files = []
        for file in Path(file_path).iterdir():
            if file.is_dir() and (not file.name.startswith(".")):
                files.extend(self.scan(file))
                recursive = True
            elif file.is_file():
                files.append(file)
                recursive = recursive
        return files

class Executor:
    def __init__(self, category, destination_path):
        self.d_path = Path(destination_path)
        self.cat = category    

    #A dry run to check if it is working or not
    def dry_run(self):
        would_moved=[]
        errors=[]
        if self.d_path in Scanner(self.d_path.parent.name):
            errors.append(self.d_path)
        else:
            would_moved.append(self.d_path)
        print(f"{self.cat} --> {self.d_path}")
        
    def run(self):
        moved = []
        errors = []
        if self.d_path in Scanner(self.d_path.parent.name):
            errors.append(self.d_path)
        else:
            moved.append(self.d_path)
        
if __name__ == "__main__":
    FP = str(input("Enter File path: "))
    sc = Planner(FP)
    print(sc.Build_plan())
    