# Main Tkinter GUI application

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os

selected_files = []

def select_files():
    global selected_files
    selected_files = filedialog.askopenfilenames(filetypes=[ ("Audio Files", "*.mp3"),
                                                    ("Audio Files", "*.wav"),
                                                    ("Audio Files", "*.flac"),
                                                    ("Audio Files", "*.aiff")])
    update_audio_file_list()

def get_modified_filename(file_name_without_ext):
    prefix_text = prefix_entry.get().strip() or ""
    filename_text = filename.get().strip() or file_name_without_ext
    suffix_text = suffix_entry.get().strip() or ""

    new_filename = f"{prefix_text}{filename_text}{suffix_text}"

    #Append wildcards if any are selected
    if selected_wildcards_order:
        new_filename += f"_{'_'.join(selected_wildcards_order)}"

    return new_filename

def apply_find_replace(base_name):
    find_text = find_entry.get().strip()
    replace_text = replace_entry.get().strip()

    if find_text and find_text in base_name:
        return base_name.replace(find_text, replace_text)
    
    return base_name

def update_audio_file_list(*args):
    audio_file_list.delete("1.0", tk.END)
    
    for file in selected_files:
        file_name = os.path.basename(file)
        file_name_without_ext, file_ext = os.path.splitext(file_name)

        # Get modified filename (prefix, suffix, wildcards)
        modified_name = get_modified_filename(file_name_without_ext)

        final_name = apply_find_replace(modified_name)

        #Display original and modified filenames
        audio_file_list.insert(tk.END, file_name + "\n")
        audio_file_list.insert(tk.END, final_name + file_ext + "\n\n")








# def update_audio_file_list(*args):
#     audio_file_list.delete("1.0", tk.END)

#     prefix_text = prefix_entry.get().strip() or ""
#     filename_text = filename.get().strip() or ""
#     suffix_text = suffix_entry.get().strip() or ""
#     find_text = find_entry.get().strip()
#     replace_text = replace_entry.get().strip()

#     # Any defining file renaming that includes filename_text
#     if prefix_text and filename_text and suffix_text:
#         new_filename = f"{prefix_text}{filename_text}{suffix_text}"
#     elif prefix_text and filename_text:
#         new_filename = f"{prefix_text}{filename_text}"
#     elif filename_text and suffix_text:
#         new_filename = f"{filename_text}{suffix_text}"
#     else:
#         new_filename = f"{filename_text}"

#     # Writes to audio_file_list Textbox
#     for file in selected_files:
#         file_name = os.path.basename(file)
#         file_name_without_ext, file_name_extension = os.path.splitext(file_name) # Splits file name extension
#         audio_file_list.insert(tk.END, file_name + "\n")

#         # For renaming files without filename_text
#         if prefix_text and suffix_text and not filename_text:
#             audio_file_list.insert(tk.END, prefix_text + file_name_without_ext + suffix_text + "\n\n")
#         elif prefix_text and not filename_text:
#             audio_file_list.insert(tk.END, prefix_text + file_name_without_ext + "\n\n")
#         elif suffix_text and not filename_text:
#             audio_file_list.insert(tk.END, file_name_without_ext + suffix_text + "\n\n")
#         else:
#             audio_file_list.insert(tk.END, new_filename + "\n\n")

# Store selected wildcards in order
selected_wildcards_order = []

def update_filename_with_wildcards(event=None):
    # Updates the filename by adding/removing wildcards in the order they were selected.
    global selected_wildcards_order

    selected_indices = wildcards_list.curselection()  # Get selected wildcard indices
    current_selected = [wildcards_list.get(i) for i in selected_indices]  # Get wildcard text

    # Add newly selected wildcards in the order they were clicked
    for wildcard in current_selected:
        if wildcard not in selected_wildcards_order:
            selected_wildcards_order.append(wildcard)  # Maintain order

    # Remove wildcards that have been deselected
    selected_wildcards_order = [w for w in selected_wildcards_order if w in current_selected]

    # Extract base filename (remove any existing wildcards)
    base_filename = filename.get().split("_")[0].strip()

    if selected_wildcards_order:
        new_filename = f"{base_filename}_{'_'.join(selected_wildcards_order)}"
    else:
        new_filename = base_filename  # No wildcards, keep original

    filename.delete(0, tk.END)  # Clear current text
    filename.insert(0, new_filename)  # Update filename entry
    update_audio_file_list()  # Refresh displayed filenames in text box


def toggle_wildcards_list():
    if wildcards_list.winfo_ismapped():
        wildcards_list.grid_remove() #Hides List
    else:
        wildcards_list.grid(row=3, column=3, columnspan=2)

#Initialize TKinter
root = tk.Tk()
root.title("Audio File Renamer")

#Makes root window expand
root.columnconfigure(0, weight=1)
root.rowconfigure(3, weight=1)

frame = ttk.Frame(root, padding = 10)
frame.grid(row=3, column=0, sticky="nsew")

#Makes Frame expand when window expands
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
frame.rowconfigure(3, weight=1)

# By Row, Column
#Row1
prefix_frame = ttk.Frame(frame)
prefix_frame.grid(row=0, column=0, sticky="nsew")

prefix_label = ttk.Label(prefix_frame, text="Prefix:")
prefix_label.pack(side="left")
prefix_entry = ttk.Entry(prefix_frame)
prefix_entry.pack(side="right", fill="x", expand=True)
prefix_entry.bind("<KeyRelease>", update_audio_file_list) # Bind the event to update when the user types

find_frame = ttk.Frame(frame)
find_frame.grid(row=0, column=2, sticky="nsew")

find_label = ttk.Label(find_frame, text="Find:")
find_label.pack(side="left")
find_entry = ttk.Entry(find_frame)
find_entry.pack(side="right", fill="x", expand=True)
find_entry.bind("<KeyRelease>", update_audio_file_list)

#Row2
suffix_frame = ttk.Frame(frame)
suffix_frame.grid(row=1, column=0, sticky="nsew")

suffix_label = ttk.Label(suffix_frame, text="Suffix:")
suffix_label.pack(side="left")
suffix_entry = ttk.Entry(suffix_frame)
suffix_entry.pack(side="right", fill="x", expand=True)
suffix_entry.bind("<KeyRelease>", update_audio_file_list)  # Bind the event to update when the user types

replace_frame = ttk.Frame(frame)
replace_frame.grid(row=1, column=2, sticky="nsew")

replace_label = ttk.Label(replace_frame, text="Replace:")
replace_label.pack(side="left")
replace_entry = ttk.Entry(replace_frame)
replace_entry.pack(side="right", fill="x", expand=True)
replace_entry.bind("<KeyRelease>", update_audio_file_list)

#Row3
browse = tk.Button(frame, text="Browse", command=select_files)
browse.grid(row=2, column=0, sticky="w")

#Delimiter and Filename in a Frame
filename_frame = ttk.Frame(frame)
filename_frame.grid(row=2, column=2, sticky="nsew")
delimiter = ttk.Combobox(filename_frame, width=3)
delimiter.pack(side="left")
filename = ttk.Entry(filename_frame)
filename.pack(side="right", fill="x", expand=True)
filename.bind("<KeyRelease>", update_audio_file_list) # Bind the event to update when the user types

wildcards_btn = ttk.Button(frame, text="Wildcards", command=toggle_wildcards_list)
wildcards_btn.grid(row=2, column=3)
wildcards = ["$SampleRate", "$Bitrate", "$Length", "$Channels", "$BitsperSample", "$Codec"]
wildcards_list = tk.Listbox(frame, selectmode=tk.MULTIPLE, height=len(wildcards))
for wildcard in wildcards:
    wildcards_list.insert(tk.END, wildcard)
wildcards_list.bind("<<ListboxSelect>>", update_filename_with_wildcards)

#Row4
audio_file_list = tk.Text(frame, wrap="none")
audio_file_list.grid(row=3, columnspan=3, sticky="nsew")



root.mainloop()
