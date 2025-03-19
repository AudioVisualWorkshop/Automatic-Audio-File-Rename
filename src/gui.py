import tkinter as tk
from tkinter import filedialog, ttk
import os
from renamer import rename_files
from wildcards import get_selected_wildcards

class AudioFileRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio File Renamer")
        self.selected_files = [] #instead of using a global variable
        self.selected_wildcards_order = []

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.grid(row=0, column=0, sticky="nsew")

        #Prefix Entry
        ttk.Label(frame, text="Prefix:").grid(row=0, column=0, sticky="w")
        self.prefix_entry = ttk.Entry(frame)
        self.prefix_entry.grid(row=0, column=1, sticky="ew")
        self.prefix_entry.bind("<KeyRelease>", self.update_audio_file_list)

        # Suffix Entry
        ttk.Label(frame, text="Suffix:").grid(row=1, column=0, sticky="w")
        self.suffix_entry = ttk.Entry(frame)
        self.suffix_entry.grid(row=1, column=1, sticky="ew")
        self.suffix_entry.bind("<KeyRelease>", self.update_audio_file_list)

        # Find & Replace
        ttk.Label(frame, text="Find:").grid(row=2, column=0, sticky="w")
        self.find_entry = ttk.Entry(frame)
        self.find_entry.grid(row=2, column=1, sticky="ew")
        self.find_entry.bind("<KeyRelease>", self.update_audio_file_list)

        ttk.Label(frame, text="Replace:").grid(row=3, column=0, sticky="w")
        self.replace_entry = ttk.Entry(frame)
        self.replace_entry.grid(row=3, column=1, sticky="ew")
        self.replace_entry.bind("<KeyRelease>", self.update_audio_file_list)

        # Browse Button
        browse_button = tk.Button(frame, text="Browse", command=self.select_files)
        browse_button.grid(row=4, column=0, columnspan=2)

        #Wildcards List
        self.wildcards_list = tk.Listbox(frame, selectmode=tk.MULTIPLE, height=5)
        self.wildcards_list.grid(row=5, column=0, columnspan=2)
        self.wildcards_list.bind("<<ListboxSelect>>", self.update_wildcards)

        # Audio File List Display
        self.audio_file_list = tk.Text(frame, wrap="none", height=10)
        self.audio_file_list.grid(row=6, column=0, columnspan=2, sticky="nsew")

    def select_files(self):
        self.selected_files = filedialog.askopenfilenames(filetypes=[ ("Audio Files", "*.mp3"),
                                                        ("Audio Files", "*.wav"),
                                                        ("Audio Files", "*.flac"),
                                                        ("Audio Files", "*.aiff")])
        self.update_audio_file_list()

    def update_wildcards(self, event=None):
        self.selected_wildcards_order = get_selected_wildcards(self.wildcards_list)
        self.update_audio_file_list()

    def update_audio_file_list(self, event=None):
        self.audio_file_list.delete("1.0", tk.END)
        prefix = self.prefix_entry.get().strip()
        suffix = self.suffix_entry.get().strip()
        find_text = self.find_entry.get().strip()
        replace_text = self.replace_entry.get().strip()

        for file in self.selected_files:
            file_name = os.path.basename(file)
            new_name = rename_files(file_name, prefix, suffix, find_text, replace_text, self.selected_wildcards_order)
            self.audio_file_list.insert(tk.END, file_name + "\n")
            self.audio_file_list.insert(tk.END, new_name + "\n\n")


















# # By Row, Column
# #Row1
# # prefix_frame = ttk.Frame(frame)
# # prefix_frame.grid(row=0, column=0, sticky="nsew")

# prefix_label = ttk.Label(prefix_frame, text="Prefix:")
# prefix_label.pack(side="left")
# prefix_entry = ttk.Entry(prefix_frame)
# prefix_entry.pack(side="right", fill="x", expand=True)
# prefix_entry.bind("<KeyRelease>", update_audio_file_list) # Bind the event to update when the user types

# find_frame = ttk.Frame(frame)
# find_frame.grid(row=0, column=2, sticky="nsew")

# find_label = ttk.Label(find_frame, text="Find:")
# find_label.pack(side="left")
# find_entry = ttk.Entry(find_frame)
# find_entry.pack(side="right", fill="x", expand=True)
# find_entry.bind("<KeyRelease>", update_audio_file_list)

# #Row2
# suffix_frame = ttk.Frame(frame)
# suffix_frame.grid(row=1, column=0, sticky="nsew")

# suffix_label = ttk.Label(suffix_frame, text="Suffix:")
# suffix_label.pack(side="left")
# suffix_entry = ttk.Entry(suffix_frame)
# suffix_entry.pack(side="right", fill="x", expand=True)
# suffix_entry.bind("<KeyRelease>", update_audio_file_list)  # Bind the event to update when the user types

# replace_frame = ttk.Frame(frame)
# replace_frame.grid(row=1, column=2, sticky="nsew")

# replace_label = ttk.Label(replace_frame, text="Replace:")
# replace_label.pack(side="left")
# replace_entry = ttk.Entry(replace_frame)
# replace_entry.pack(side="right", fill="x", expand=True)
# replace_entry.bind("<KeyRelease>", update_audio_file_list)

# #Row3
# browse = tk.Button(frame, text="Browse", command=select_files)
# browse.grid(row=2, column=0, sticky="w")

# #Delimiter and Filename in a Frame
# filename_frame = ttk.Frame(frame)
# filename_frame.grid(row=2, column=2, sticky="nsew")
# delimiter = ttk.Combobox(filename_frame, width=3)
# delimiter.pack(side="left")
# filename = ttk.Entry(filename_frame)
# filename.pack(side="right", fill="x", expand=True)
# filename.bind("<KeyRelease>", update_audio_file_list) # Bind the event to update when the user types

# wildcards_btn = ttk.Button(frame, text="Wildcards", command=toggle_wildcards_list)
# wildcards_btn.grid(row=2, column=3)
# wildcards = ["$SampleRate", "$Bitrate", "$Length", "$Channels", "$BitsperSample", "$Codec"]
# wildcards_list = tk.Listbox(frame, selectmode=tk.MULTIPLE, height=len(wildcards))
# for wildcard in wildcards:
#     wildcards_list.insert(tk.END, wildcard)
# wildcards_list.bind("<<ListboxSelect>>", update_filename_with_wildcards)

# #Row4
# audio_file_list = tk.Text(frame, wrap="none")
# audio_file_list.grid(row=3, columnspan=3, sticky="nsew")


# selected_files = []

# def select_files():
#     global selected_files
#     selected_files = filedialog.askopenfilenames(filetypes=[ ("Audio Files", "*.mp3"),
#                                                     ("Audio Files", "*.wav"),
#                                                     ("Audio Files", "*.flac"),
#                                                     ("Audio Files", "*.aiff")])
#     update_audio_file_list()

# def update_audio_file_list(*args):
#     audio_file_list.delete("1.0", tk.END)
    
#     for file in selected_files:
#         file_name = os.path.basename(file)
#         file_name_without_ext, file_ext = os.path.splitext(file_name)

#         # Get modified filename (prefix, suffix, wildcards)
#         modified_name = get_modified_filename(file_name_without_ext)

#         final_name = apply_find_replace(modified_name)

#         #Display original and modified filenames
#         audio_file_list.insert(tk.END, file_name + "\n")
#         audio_file_list.insert(tk.END, final_name + file_ext + "\n\n")

# def get_modified_filename(file_name_without_ext):
#     prefix_text = prefix_entry.get().strip() or ""
#     filename_text = filename.get().strip() or file_name_without_ext
#     suffix_text = suffix_entry.get().strip() or ""

#     new_filename = f"{prefix_text}{filename_text}{suffix_text}"

#     #Append wildcards if any are selected
#     if selected_wildcards_order:
#         new_filename += f"_{'_'.join(selected_wildcards_order)}"

#     return new_filename

# def apply_find_replace(base_name):
#     find_text = find_entry.get().strip()
#     replace_text = replace_entry.get().strip()

#     if find_text and find_text in base_name:
#         return base_name.replace(find_text, replace_text)
    
#     return base_name


# Store selected wildcards in order
# selected_wildcards_order = []

# def update_filename_with_wildcards(event=None):
#     # Updates the filename by adding/removing wildcards in the order they were selected.
#     global selected_wildcards_order

#     selected_indices = wildcards_list.curselection()  # Get selected wildcard indices
#     current_selected = [wildcards_list.get(i) for i in selected_indices]  # Get wildcard text

#     # Add newly selected wildcards in the order they were clicked
#     for wildcard in current_selected:
#         if wildcard not in selected_wildcards_order:
#             selected_wildcards_order.append(wildcard)  # Maintain order

#     # Remove wildcards that have been deselected
#     selected_wildcards_order = [w for w in selected_wildcards_order if w in current_selected]

#     # Extract base filename (remove any existing wildcards)
#     base_filename = filename.get().split("_")[0].strip()

#     if selected_wildcards_order:
#         new_filename = f"{base_filename}_{'_'.join(selected_wildcards_order)}"
#     else:
#         new_filename = base_filename  # No wildcards, keep original

#     filename.delete(0, tk.END)  # Clear current text
#     filename.insert(0, new_filename)  # Update filename entry
#     update_audio_file_list()  # Refresh displayed filenames in text box


# def toggle_wildcards_list():
#     if wildcards_list.winfo_ismapped():
#         wildcards_list.grid_remove() #Hides List
#     else:
#         wildcards_list.grid(row=3, column=3, columnspan=2)