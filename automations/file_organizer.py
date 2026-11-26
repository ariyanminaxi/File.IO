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
dest_location = {
    # Pictures
    "Images": "Pictures/FO_sample",

    # Videos
    "Videos": "Videos/FO_sample",
    "Video_Projects": "Videos/FO_sample/projects",

    # Music
    "Audio": "Music/FO_sample",

    # Documents
    "Documents": "Documents/FO_sample",
    "Spreadsheets": "Documents/FO_sample/spreadsheets",
    "Presentations": "Documents/FO_sample/presentations",
    "Certificates": "Documents/FO_sample/certificates",
    "Ebooks": "Documents/FO_sample/ebooks",

    # Downloads
    "Archives": "Downloads/FO_sample/archives",
    "Applications": "Downloads/FO_sample/applications",
    "Torrents": "Downloads/FO_sample/torrents",

    # Documents - Development
    "Code": "Documents/FO_sample/code",
    "Data": "Documents/FO_sample/data",
    "Configuration": "Documents/FO_sample/configuration",

    # Documents - Design
    "Fonts": "Documents/FO_sample/design/fonts",
    "3D_Models": "Documents/FO_sample/design/3d_models",

    # System
    "Disk_Images": "Documents/FO_sample/backups/disk_images",
    "Backups": "Documents/FO_sample/backups",
    "Logs": "Documents/FO_sample/logs",
    "Others": "Documents/Other_files"
}

class PlanItem:
    def __init__(self, source, cat) -> None:
        self.source = source
        self.category = cat
        self.dest_folder = Path(r"D:\VS_code\Projects\File_Automation\sample_folder\_organized") / Path(self.category) 
        self.dest_file = Path(self.dest_folder / Path(self.source).name)
        self.conflict = Path(self.dest_file).exists()

    # To display the data the object holds
    def display(self) -> str:
        print("|-----{Item Data}-----}")
        print(f"Source : {self.source}")
        print(f"Category : {self.category}")
        print(f"Destination folder : {self.dest_folder}")
        print(f"Destination file : {self.dest_file}")
        print(f"Conflict : {self.conflict}")

class Planner:
    def __init__(self, path, recursive = False) -> None:
        self.path =Path(path)
        self.recursive = recursive
        self.Build_plan()
    
    def Build_plan(self) -> dict[PlanItem]:
        self.plan = {}
        self.skipped = []
            # |----{Scanning for files to move}----|
        # We need to check if the path is a folder or a file
        if self.path.is_file(): # If the path contains only one file.
            self.files_ = [self.path]
        elif self.path.is_dir(): # If the path contains a folder dir
            self.sc = Scanner(self.path, self.recursive)
            self.files_ = self.sc.files
        else:
            raise FileNotFoundError(f"Path not found: {self.path}")

            # |----{Getting Category}----|
        # This separates between plan and skipped.
        for file in self.files_:
                if(self.check(file_path=file)):
                    self.plan[file]=PlanItem(file,File_Classifier(file).get_category())
                else:
                    self.skipped.append(file)
        return self.plan

    # Checks for any hidden folders 
    def check(self, file_path) -> bool:
        if Path(file_path).name.startswith("."):
            return False
        else:
            return True      

class File_Classifier:
    def __init__(self, file_path):
        self.file_path = file_path
    def get_category(self):
        self.name = Path(self.file_path).name.lower()
        self.extension = Path(self.name).suffix  # Here remember basename will give the name of the file with extension and suffixes will give the extension but suffixes can't work with Path function
        return Extension_types.get(self.extension, "Others")
             
class Scanner:
    def __init__(self, file_path, recursive=False):
        self.file_path = file_path
        self.recursive = recursive
        self.files = self.scan(self.file_path)
    def scan(self, file_path):
        files = []
        for file in Path(file_path).iterdir():
            if file.is_dir() and (not file.name.startswith(".")) and (self.recursive):
                files.extend(self.scan(file))
            elif file.is_file():
                files.append(file)
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
    for ds in sc.plan.values():
        print(ds.display())
    