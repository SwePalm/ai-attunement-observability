import json
import os
from pathlib import Path
from typing import Dict, Optional, Any

from attunement.config import SCENARIO_STORE_PATH, SCENARIO_SUB_KEYS, THEMES_LIST

from dotenv import load_dotenv

# It's good practice to load environment variables once at the module level
load_dotenv()

def load_file(filepath):
    if filepath is None:
        filepath = SCENARIO_STORE_PATH

    if not filepath:
        print("Error: Filepath not provided and THEMES_STORE_PATH variable not set.")
        return {}

    path_obj = Path(filepath)

    if not path_obj.exists():
        print(f"Error: File not found at '{path_obj}'")
        return {}

    try:
        with path_obj.open('r', encoding='utf-8') as file:
            themes = json.load(file)
            # print(f"Successfully loaded {len(themes)} themes from {path_obj}.")
            return themes
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file: {e}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred during file loading: {e}")
        return {}

def get_themes(filepath: Optional[str] = None):
    """
    Reads the JSON file and returns its keys as a Python dictionary.
    
    Args:
        filepath (Optional[str]): The path to the JSON file. If None, it uses
                                  the THEMES_STORE_PATH environment variable.
        
    Returns:
        dict: The themes dictionary, or an empty dictionary if loading fails.
    """
    all_themes = load_file(filepath)
    return list(all_themes.keys())

    
def get_theme_question(theme: str, filepath: Optional[str] = None):
    """
    Reads the THEMES STORE file and returns the question for the given theme.
    
    """
    all_themes = load_file(filepath)

    return all_themes[theme]["question"]

def get_theme_exploration(theme: str, filepath: Optional[str] = None):
    """
    Reads the THEMES STORE file and returns the Exploration Conversation for the given theme.
    
    """
    all_themes = load_file(filepath)

    return all_themes[theme]["exploration"]

def get_theme_pestle(theme: str, filepath: Optional[str] = None):
    """
    Reads the THEMES STORE file and returns the PESTLE Analysis for the given theme.
    
    """
    all_themes = load_file(filepath)

    return all_themes[theme]["pestle"]

def get_theme_forces_feelings(theme: str, filepath: Optional[str] = None):
    """
    Reads the THEMES STORE file and returns the Forces and Feelings Analysis for the given theme.
    
    """
    all_themes = load_file(filepath)

    return all_themes[theme]["forces_feelings"]

def get_theme_scenario(theme: str, filepath: Optional[str] = None):
    """
    Reads the THEMES STORE file and returns the Scenario for the given theme.
    
    """
    all_themes = load_file(filepath)

    return all_themes[theme]["scenario"]


def get_all_themes_data_to_framework(filepath=""):
    """
    Reads the THEMES STORE file and returns all themes, questions and scenarios
    
    """
    if filepath == "":
        filepath = os.getenv("THEMES_STORE_PATH")

    themes_list = get_themes(filepath)

    data_to_framework = {}
    for theme in themes_list:
        data_to_framework[theme] = {}
        data_to_framework[theme]["question"] = get_theme_question(theme, filepath=filepath)
        data_to_framework[theme]["scenario"] = get_theme_scenario(theme, filepath=filepath)

    return data_to_framework


def save_response_to_theme(theme: str, subkey: str, response: str, filepath = ""):

    if subkey not in SCENARIO_SUB_KEYS:
        print(f"Error: Subkey '{subkey}' is not a valid, valid keys are {SCENARIO_SUB_KEYS}.")
        return False
  
    if filepath == "":
        filepath = os.getenv("THEMES_STORE_PATH")
    
    themes_file_path = os.path.abspath(str(filepath))


    if not os.path.exists(themes_file_path):
        print(f"Error: File not found at '{filepath}'")
        return False

    try:
        with open(themes_file_path, 'r+', encoding='utf-8') as f:
            try:
                data: Dict[str, Any] = json.load(f)
            except json.JSONDecodeError:
                print(f"Error: Could not decode JSON from '{filepath}'. File might be empty or corrupt.")
                return False

            if theme in data:
                # Update the dictionary for the existing theme
                data[theme][subkey] = response
                
                # Go back to the beginning of the file to overwrite it
                f.seek(0)
                # Write the updated data back to the file
                json.dump(data, f, indent=4)
                # Truncate the file in case the new content is smaller than the old
                f.truncate()
                
                # print(f"Successfully updated theme '{theme}' with subkey '{subkey}'.")
                return True
            else:
                print(f"Error: Theme '{theme}' not found in '{filepath}'.")
                return False
    except IOError as e:
        print(f"An I/O error occurred: {e}")
        return False
    
def create_new_data_store(filepath):

    if os.path.exists(filepath):
        print(f"Error: File found at '{filepath}'")
        return False
    
    themes = THEMES_LIST
    default_content = {}
    for theme in themes:
        default_content[theme] = {}

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(default_content, f, ensure_ascii=False, indent=2)
    except OSError as e:
        print(f"Error creating file '{filepath}': {e}")
        return False