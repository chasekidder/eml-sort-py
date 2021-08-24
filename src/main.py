#!/usr/bin/env python3


# Copyright 2021 Chase Kidder

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Sorts .eml files into subdirectories based on date.

import os
import email
import shutil
from pathlib import Path

def main():
    src_directory = """\\EMAILS\\TO\\SORT\\"""
    dst_directory = """\\SORTED\\EMAILS\\DEST\\"""

    for filename in os.listdir(src_directory):
        # Do not sort non-emails
        if not ".eml" in filename:
            continue

        path = os.path.join(src_directory, filename)

        # Do not sort subdirectories
        if not os.path.isfile(path):
            continue

        with open(path) as f:
            # Get date and time from email headers
            headers = email.message_from_file(f)
            date = email.utils.parsedate_to_datetime(headers.get('date'))

            # Create target directory path from date
            new_path = f"{dst_directory}{str(date.year).zfill(2)}\\{str(date.month).zfill(2)}\\{str(date.day).zfill(2)}\\"
            Path(new_path).mkdir(parents=True, exist_ok=True)

            # Do not replace existing files
            if os.path.isfile(new_path + filename):
                print(f"'Duplicate File: {path}' vs '{new_path + filename}'")
                continue

            # Copy the file
            shutil.copy2(src=path, dst=new_path)


if __name__ == "__main__":
    main()




