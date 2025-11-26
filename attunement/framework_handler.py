import json
import os
import re
from pathlib import Path
from typing import Dict, Optional, Any, Union

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


def get_framework_signals(filepath: Optional[str] = None):
    """
    Reads the JSON file and returns its keys as a Python dictionary.
    
    Args:
        filepath (Optional[str]): The path to the JSON file. If None, it uses
                                  the FRAMEWORK_STORE_PATH environment variable.
        
    Returns:
        dict: The themes dictionary, or an empty dictionary if loading fails.
    """
    the_framework = load_framework(filepath)
    return the_framework["signals"]


def get_framework_timeline(filepath: Optional[str] = None):
    """
    Reads the JSON file and returns its keys as a Python dictionary.
    
    Args:
        filepath (Optional[str]): The path to the JSON file. If None, it uses
                                  the FRAMEWORK_STORE_PATH environment variable.
        
    Returns:
        dict: The themes dictionary, or an empty dictionary if loading fails.
    """
    the_framework = load_framework(filepath)
    return the_framework["timeline"]


def get_framework_final(filepath: Optional[str] = None):
    """
    Reads the JSON file and returns its keys as a Python dictionary.
    
    Args:
        filepath (Optional[str]): The path to the JSON file. If None, it uses
                                  the FRAMEWORK_STORE_PATH environment variable.
        
    Returns:
        dict: The themes dictionary, or an empty dictionary if loading fails.
    """
    the_framework = load_framework(filepath)
    return the_framework["final_framework"]


def get_framework_report(filepath: Optional[str] = None):
    """
    Reads the JSON file and returns its keys as a Python dictionary.
    
    Args:
        filepath (Optional[str]): The path to the JSON file. If None, it uses
                                  the FRAMEWORK_STORE_PATH environment variable.
        
    Returns:
        dict: The themes dictionary, or an empty dictionary if loading fails.
    """
    the_framework = load_framework(filepath)
    return the_framework["report"]

    
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
    
    
def clean_llm_markdown_tail(text_with_tail_mess):
    """
    Cleans up the trailing garbage, specifically targeting code fences and table residue,
    while being careful NOT to strip the final punctuation (like a period).
    """

    # --- Step 1: Remove common trailing code fences, table residue, and noise ---
    # Targets: \s*```, \s*|```, \s*| (from table ending), and leading/trailing quotes/periods near the fence.
    # This pattern looks for optional noise (whitespace, table pipes, periods, asterisks) followed by triple backticks, anchored to the end.
    # It replaces the noise pattern with nothing.
    pattern_fences = r"[\s]*[\|\.\*]*\s*```\s*$"
    cleaned_text = re.sub(pattern_fences, "", text_with_tail_mess, flags=re.DOTALL)
    
    # --- Step 2: Remove residual trailing whitespace (but not punctuation) ---
    # The built-in rstrip() is much safer than a broad regex for removing just whitespace.
    cleaned_text = cleaned_text.rstrip()
    
    # --- Step 3: Handle trailing quotes or single-character noise only if they are the very last thing ---
    # This specifically removes a final, lone single/double quote or a trailing pipe that might have slipped through.
    # We will avoid removing the period itself.
    
    # Pattern to remove unwanted trailing quotes, pipes, or colons
    pattern_final_noise = r"[\'\"\|:;]$"
    cleaned_text = re.sub(pattern_final_noise, "", cleaned_text)

    # Final trim of any remaining leading whitespace
    return cleaned_text.strip()

# --- Re-testing the extraction function with the new tail cleaner ---

def extract_and_clean(full_response_string):
    # Anchor to the start of the first '#'
    start_pattern = r"#"
    match = re.search(start_pattern, full_response_string, re.DOTALL)
    
    if match:
        start_index = match.start()
        # Get the content from the first # to the end
        content_from_hash = full_response_string[start_index:]
        # Now clean the tail mess
        return clean_llm_markdown_tail(content_from_hash)
    else:
        return "Error: Could not find the starting '#' anchor."


def save_final_frameworks_as_md(data_dir: Union[str, Path] = "data"):
    base_path = Path(data_dir)
    if not base_path.exists():
        raise FileNotFoundError(f"Data directory not found: {base_path}")

    for json_path in sorted(base_path.glob("framework*.json")):
        if not json_path.is_file():
            continue

        with json_path.open(encoding="utf-8") as handle:
            payload = json.load(handle)

        final_framework = payload.get("final_framework")
        if final_framework is None:
            raise KeyError(
                f'"final_framework" missing from {json_path.relative_to(base_path.parent)}'
            )

        clean_framework = extract_and_clean(final_framework)

        stem_parts = json_path.stem.split("_")
        key_name = "_".join(stem_parts[2:]) if len(stem_parts) > 2 else json_path.stem

        # The name of the file you want to create
        output_filename = f"docs/frameworks/{key_name}_2511_framework.md"

        try:
            # 'with open' is the recommended way to handle files in Python.
            # It ensures the file is properly closed even if errors occur.
            # 'w' means "write mode", which will create the file if it doesn't exist,
            # or overwrite it if it does.
            # 'encoding="utf-8"' is crucial for handling special characters correctly.
            with open(output_filename, "w", encoding="utf-8") as file:
                file.write(clean_framework)
            
            print(f"Successfully saved markdown to {output_filename}")

        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

    return True

def save_reports_as_md(data_dir: Union[str, Path] = "data"):
    base_path = Path(data_dir)
    if not base_path.exists():
        raise FileNotFoundError(f"Data directory not found: {base_path}")

    for json_path in sorted(base_path.glob("framework*.json")):
        if not json_path.is_file():
            continue

        with json_path.open(encoding="utf-8") as handle:
            payload = json.load(handle)

        final_framework = payload.get("report")
        if final_framework is None:
            raise KeyError(
                f'"final_framework" missing from {json_path.relative_to(base_path.parent)}'
            )

        clean_framework = extract_and_clean(final_framework)

        stem_parts = json_path.stem.split("_")
        key_name = "_".join(stem_parts[2:]) if len(stem_parts) > 2 else json_path.stem

        # The name of the file you want to create
        output_filename = f"docs/reports/{key_name}_2511_report.md"

        try:
            # 'with open' is the recommended way to handle files in Python.
            # It ensures the file is properly closed even if errors occur.
            # 'w' means "write mode", which will create the file if it doesn't exist,
            # or overwrite it if it does.
            # 'encoding="utf-8"' is crucial for handling special characters correctly.
            with open(output_filename, "w", encoding="utf-8") as file:
                file.write(clean_framework)
            
            print(f"Successfully saved markdown to {output_filename}")

        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

    return True