# File renaming logic

import os

def rename_files(file_name, prefix, suffix, find_text, replace_text, wildcards):
    file_name_without_ext, file_ext = os.path.splitext(file_name)

    # Apply find & replace if needed
    if find_text and find_text in file_name_without_ext:
        file_name_without_ext = file_name_without_ext.replace(find_text, replace_text)

    # Apply prefix and suffix
    new_name = f"{prefix}{file_name_without_ext}{suffix}"

    # Append wildcards if any
    if wildcards:
        new_name += "_" + "_".join(wildcards)
    
    return new_name + file_ext