# CorruptPDFGenerator
This program creates a PDF that cannot be opened.

## How it works

These program creates a new pdf file (in the same directory as the code) that cannot be opened. The pdf created has no attributes, so it cannot be opened. If you want to corrupt a pdf manually, you can change the extension of that pdf into a txt, then delete the first line:
```
%PDF-1.4
```
or something similar. This is the version of the PDF file and/or the PDF version of your computer. When deleted, change an other time the .txt extension to .pdf and try to open it.
### Requisites:

This program does not require any library. It has been tested on Python 3.9, but it works with every version of python that supports the OS library.

### Installing

- Download or clone the repository.
- Execute the Python file (with launcher.bat or witht any other prefered method)
- A command prompt window should appear.

### How to use:
- Execute the script (a command prompt window should appear)
- Introduce the name of the file (it can contain spaces, numbers...)
- Press enter
- A new file will be crated in the same directory as the code, this will be the corrupted pdf. This pdf cannot be opened 

### Works for sure on:

- Windows 10 with Python 3.9
