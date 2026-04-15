import os
import shutil
import time
from fastmcp import FastMCP

mcp=FastMCP("Janitor")

@mcp.tool()
def list_files(directory: str) -> list[str]:
    """Return the list of filenames in a given directory"""
    print(f"Listing files; 15 sec rate limit bypass countdown")
    time.sleep(15)
    
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        return [f"Error: Directory '{directory}' not found."]
    except Exception as e:
        return [f"Error: {str(e)}"]

@mcp.tool()
def read_file(filename:str,directory:str) -> str:
    """Read and return the text content of a file so you can analyze its subject matter"""
    print(f"Reading '{filename}'; 15 sec rate limit bypass countdown")

    time.sleep(15)
    
    filepath=os.path.join(directory,filename)
    try:
        with open(filepath,'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found in '{directory}'."
    except UnicodeDecodeError:
        return f"Error: '{filename}' is a binary file or not readable text."
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def move_file(filename:str,source_dir:str, category:str) -> str:
    """Move a file from source_dir into a sub directory named after the category"""
    print(f"Moving '{filename}'; 15 sec rate limit bypass countdown")
    time.sleep(15)
    
    source_path=os.path.join(source_dir,filename)
    target_dir=os.path.join(source_dir,category)
    target_path=os.path.join(target_dir,filename)

    try:
        if not os.path.exists(source_path):
            return f"Error: Source file '{filename}' does not exist in '{source_dir}'."
        os.makedirs(target_dir,exist_ok=True)
        shutil.move(source_path,target_path)
        return f"Success: Moved '{filename}' to '{category}/'."
    except Exception as e:
        return f"Error: Failed to move file. {str(e)}"

if __name__ == "__main__":
    mcp.run()