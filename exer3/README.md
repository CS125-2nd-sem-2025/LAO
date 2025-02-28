#  How to Run the OS Info API

Follow these steps to set up and run your **FastAPI** server that provides OS, version, and IP information.

## Prerequisites
Check if you have the following:
- **Python 3.7+** → Check if you have it by typing in your terminal `python --version`
- **pip** → Check if you have it by typing in your terminal `pip --version`

## Step 1: Install Dependencies
Open your terminal (Command Prompt, PowerShell, or VS Code Terminal) and run:
```sh
pip install fastapi uvicorn
```
This installs **FastAPI** (for the API) and **Uvicorn** (to run the server).

## Step 2: Save the Python Script
Clone the code in the repository as `main.py` in your project folder.

## Step 3: Run the API Server
Navigate to the project folder and run:
```sh
uvicorn main:app --reload
```
**Note**: If your file is named differently, replace `main` with your filename.

After running the command, you should see:
```
Uvicorn running on http://127.0.0.1:8000
```

## Step 4: Access the API
Open your browser and type "http://127.0.0.1:8000/"

## Step 6: Stop the Server
To stop the API, **press `CTRL + C`** in the terminal.

