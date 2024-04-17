# Baby Rijndael
Implementation of the Baby Rijndael Block Cipher in Python

## Requirements
- python 3.10+

## Installation
1. Create new virtual environment
   
    `python3 -m venv .venv`
3. Initialize virtual environment
   
    `source .venv/bin/activate` (unix)
   
    `.venv\Scripts\activate` (windows)
4. Install packages from requirements.txt
   
    `pip install -r requirements. txt`
6. Run python script to encrypt/decrypt with Baby Rijndael
   
    `python3 main.py`

## Important
- encryption/decryption is done on a file provided by the user. 
    - the file should be in the same root directory as 'main.py'
- tests are written via pytest

## MISC
- get byte value of input file (grouped)
    
    `xxd -g 1 [filename]`
    `od -cx [filename]` (outputs in little-endian)
- get byte value of input file (raw)

    `xxd -p [filename]`
    `od -t x1 [filename]`
- [xxd documentation](https://ss64.com/mac/xxd.html)
