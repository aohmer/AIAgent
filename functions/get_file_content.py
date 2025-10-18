import os
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_dir):
       return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        MAX_CHARS = 10000
        with open(target_dir, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            extra = f.read(1)
            if extra != '':
                return f'{file_content_string}[...File "{file_path}" truncated at 10000 characters]'
            else:
                return file_content_string

    except Exception as e:
        return f"Error: {e}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read file content in the specified file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of where to read the file content, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)