import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.exists(os.path.dirname(target_dir)):
            os.makedirs(os.path.dirname(target_dir))
        with open(target_dir, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file_content",
    description="Writes or overwrites files in the specified file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path where files are located to write or overwrite, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write or overwrite a given file"
            )
        },
    ),
)