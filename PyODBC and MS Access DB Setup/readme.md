
# Using PyODBC to connecto to a MS Access Database (on Windows)

## Purpose

Setting up and loading dependencies for Windows drivers, Python environment, and some sample code to interact with a Microsoft Acces .mdb database using Python.

## Either 64 & 64 or 32 & 32

The first thing to note is the Python environment and the database __must__ be the same bitness.
This was a huge hangup for me in the beginning because I didn't realize my Anaconda was running 64 bit but my MS Office was 32. This will likely be the case for many people starting with default installations. For these directions, personally I decided to uninstall my MS Office and reinstall the 64 bit. Handling a lot of large data files, this makes sense since it's one of the benefits of 64 bit MS Office. You can find directions for downloading MS Office [here](https://support.office.com/en-us/article/download-and-install-or-reinstall-office-365-or-office-2019-on-a-pc-or-mac-4414eaaf-0478-48be-9c42-23adc4716658). If you'd rather not change your MS Office installation you can run a specific Python environment just for handling this module.

## Download PYODBC

If you're not using Anaconda (which comes with PYODBC preloaded), download the PYODBC module either from [here](https://pypi.org/project/pyodbc/#description) or by using 'pip install pyodbc'. 

## Windows Drivers

Another big hang up I had was although I had installed the 64 bit version of Microsoft Office, it did not come with the DSN drivers needed to interact with the data base. You can check the drivers that Python recognizes using the code below:

![Python Drivers](C:\Users\MacalusoC\Desktop\Connecting_to_pyodbc\7pyodbcdrivers().png)
