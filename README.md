# Baby Rijndael
Implementation of the Baby Rijndael AES Cipher in Python

## Requirements
- python 3.10+

## Installation
1. Create new virtual environment
    `python3 -m venv .venv`
2. Initialize virtual environment
    `source .venv/bin/activate` (unix)
    `.venv\Scripts\activate` (windows)
3. Install packages from requirements.txt
    `pip install -r requirements. txt`
4. Run python script to encrypt/decrypt with Baby Rijndael
    `python3 main.py`

## Important
- encryption/decryption is done on a file provided by the user. 
    - the file should be in the same root directory as 'main.py'
- tests are written via pytest