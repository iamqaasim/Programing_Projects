# My imports
from os import scandir, rename               # Scan folders and Rename files
from os.path import splitext, exists, join   # Edit file names
from shutil import move                      # Move files

# Watchdog quick start imports
#import sys                                  # I passed the path directly, so we dont need this import anymore 
from time import sleep                       # Timer
import logging                               # Display infomation      
from watchdog.observers import Observer      # Schedules watching directories and dispatches calls to event handlers      
from watchdog.events import FileSystemEventHandler   # Is triggered when a change occurs on the monitored file system

# FILL IN PATHS BELOW
source_dir = "/Users/Qaasim/Downloads"
destination_directory_sounds = ""
destination_directory_music = ""
destination_directory_videos = ""
destination_directory_images = ""
destination_directory_documents = ""

# image extention types
image_extensions = [".jpg", ".jpeg", ".png", ".gif"]

# Video extention types
video_extensions = [".mp4", ".mov"]

# Audio extention types
audio_extensions = ["mp3"]

# Document extention types
document_extensions = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

# Used mainly for duplicate files
def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

# Move files between folders
def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)

# Monitor and update the source folder
class Organiser(FileSystemEventHandler): # Used inheritance to customise the handler
    
    # Monitor the source folder
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)
    
    """ 
    The following functions will filter the files in the folder and move them to their respected folder
    
    Default steps:
    - Checks all Document Files
    - Check extention 
    - Move files
    - Display intomation
    """

    # Checks all Audio Files
    def check_audio_files(self, entry, name):  
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                if entry.stat().st_size < 10_000_000 or "SFX" in name:
                    dest = destination_directory_sounds
                else:
                    dest = destination_directory_music
                move_file(dest, entry, name)
                logging.info(f"Moved audio file: {name}")

    # Checks all Video Files
    def check_video_files(self, entry, name):  
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(destination_directory_videos, entry, name)
                logging.info(f"Moved video file: {name}")

    # Checks all Image Files
    def check_image_files(self, entry, name):  
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(destination_directory_images, entry, name)
                logging.info(f"Moved image file: {name}")

    # Checks all Document Files
    def check_document_files(self, entry, name): 
        for documents_extension in document_extensions:                                          
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()): 
                move_file(destination_directory_documents, entry, name)                                       
                logging.info(f"Moved document file: {name}")                                    


# Watchdog Quick start code
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = Organiser() # Changed the event handler name to my custom one
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
