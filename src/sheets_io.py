import os
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

load_dotenv()

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def open_sheet():
    creds = Credentials.from_service_account_file(
        os.getenv("GOOGLE_CREDENTIALS_FILE"),
        scopes=SCOPES
    )
    client = gspread.authorize(creds)
    return client.open_by_key(os.getenv("GOOGLE_SHEET_ID"))

def read_df(tab_name):
    sheet = open_sheet().worksheet(tab_name)
    data = sheet.get_all_records()
    return pd.DataFrame(data)

def write_df(tab_name, df):
    sheet = open_sheet().worksheet(tab_name)

    sheet.clear

    sheet.append_row(df.columns.tolist())

    for _, row in df.iterrows():
        sheet.append_row(row.tolist())
