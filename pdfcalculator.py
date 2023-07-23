#!/usr/bin/env python
#!interpreter [optional-arg]
"""
__author__ = "Nazrin Nazarudin"
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "nazrinhnazarudin@gmail.com"
__status__ = "Prototype"

This program reads PDF Files and locate the numbers. The numbers will then be added from each PDF file.

Prerequisites:
All PDF files must have the same format.
"""

import os
from pypdf import PdfReader

# CONSTANTS
DIRECTORY_PATH = "C:/Users/NZH/Documents/" # Set to the directory in which the PDF files are located
PAGE_TO_SCAN = 0 # Set this to the page number you want to scan
TEXT_INDEX = 0 # After selecting the page, enter the text index here (will be replaced by the highlight feature)
SET_MODE = 0 # Modes for single or multipage may be included in the future updates
CONTAINS_COMMA = 1 # Set to one if the number contains comma

file_count = 0
sum = 0    

for item in os.listdir(DIRECTORY_PATH):
        item_path = os.path.join(DIRECTORY_PATH, item)
        if os.path.isfile(item_path):
            
            # File counter
            file_count += 1
            print(item_path)
            
            # PDF Reader
            reader = PdfReader(item_path)
            page = reader.pages[PAGE_TO_SCAN-1]
            text = page.extract_text()
            line = text.split() # Splits the text line by line
            theString = line[TEXT_INDEX-1] # Minus one because index starts with 0
            
            if (CONTAINS_COMMA == 1):
                noComma = theString.replace(",","") # Removes the comma within the number string
            floatString = float(noComma) # Converts the string to a float for arithmetic operation
            sum += floatString # Sums the numbers from each PDF file

print('File count:', file_count) # Counts the number of file included with the sum
print('Total:', sum) # Displays the total summation of the files                                                                              