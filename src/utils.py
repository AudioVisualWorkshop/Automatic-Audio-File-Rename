# Helper functions (logging, error handling)

import re

def is_valid_filename(filename):
    return not bool(re.search(r'[\/:*?"<>|]', filename))