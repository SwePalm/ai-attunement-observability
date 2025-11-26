import json
import os
from pathlib import Path
from typing import Dict, Optional, Any

from attunement.config import FRAMEWORK_STORE_PATH


def create_new_framework_store(filepath):

    if os.path.exists(filepath):
        print(f"Error: File found at '{filepath}'")
        return False
    
    blank_content = {}

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(blank_content, f, ensure_ascii=False, indent=2)
    except OSError as e:
        print(f"Error creating file '{filepath}': {e}")
        return False


def load_framework(filepath):
    if filepath is None:
        filepath = FRAMEWORK_STORE_PATH

    if not filepath:
        print("Error: Filepath not provided and FRAMEWORK_STORE_PATH variable not set.")
        return {}

    path_obj = Path(filepath)

    if not path_obj.exists():
        print(f"Error: File not found at '{path_obj}'")
        return {}

    try:
        with path_obj.open('r', encoding='utf-8') as file:
            framework = json.load(file)
            # print(f"Successfully loaded {len(themes)} themes from {path_obj}.")
            return framework
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file: {e}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred during file loading: {e}")
        return {}
    

def get_framework_draft(filepath: Optional[str] = None):
    """
    Reads the JSON file and returns its keys as a Python dictionary.
    
    Args:
        filepath (Optional[str]): The path to the JSON file. If None, it uses
                                  the THEMES_STORE_PATH environment variable.
        
    Returns:
        dict: The themes dictionary, or an empty dictionary if loading fails.
    """
    the_framework = load_framework(filepath)
    return the_framework["draft"]

    
def save_response_to_framework(key: str, response: str, filepath = ""):
  
    if filepath == "":
        filepath = FRAMEWORK_STORE_PATH
    
    framework_file_path = os.path.abspath(str(filepath))


    if not os.path.exists(framework_file_path):
        create_new_framework_store(framework_file_path)
        print(f"Created new framework store {framework_file_path}")

    try:
        with open(framework_file_path, 'r+', encoding='utf-8') as f:
            try:
                data: Dict[str, Any] = json.load(f)
            except json.JSONDecodeError:
                print(f"Error: Could not decode JSON from '{framework_file_path}'. File might be empty or corrupt.")
                return False

            # Update the dictionary for the existing theme
            data[key] = response
            
            # Go back to the beginning of the file to overwrite it
            f.seek(0)
            # Write the updated data back to the file
            json.dump(data, f, indent=4)
            # Truncate the file in case the new content is smaller than the old
            f.truncate()
            
            # print(f"Successfully updated theme '{theme}' with subkey '{subkey}'.")
            return True

    except IOError as e:
        print(f"An I/O error occurred: {e}")
        return False