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


def read_assets():
    sheet = open_sheet().worksheet("assets")
    rows = sheet.get_all_values()

    assets = []
    risks = []
    returns_5y = []

    for i in range(1, len(rows)):
        row = rows[i]

        if row[0] == "":
            continue

        assets.append(row[0])
        risks.append(float(row[2]))

        raw = row[5]  

        if "%" in raw:
            raw = raw.replace("%", "")
            raw = float(raw) / 100
        else:
            raw = float(raw)

        returns_5y.append(raw)

    return assets, risks, returns_5y


def read_constraints():
    sheet = open_sheet().worksheet("Constraints")

    capital = float(sheet.cell(1, 2).value)
    max_risk = float(sheet.cell(2, 2).value)

    rows = sheet.get_all_values()

    min_w = []
    max_w = []

    for i in range(4, len(rows)):
        row = rows[i]

        if row[0] == "":
            continue

        min_w.append(float(row[1]))
        max_w.append(float(row[2]))

    return capital, min_w, max_w, max_risk


def write_results(assets, weights, capital, score):
    sheet = open_sheet().worksheet("Results")

    sheet.clear()

    sheet.append_row(["Asset", "Weight (%)", "Dollar Allocation"])

    for i in range(len(assets)):
        weight_percent = round(weights[i] * 100, 2)
        dollars = round(weights[i] * capital, 2)

        sheet.append_row([
            assets[i],
            weight_percent,
            dollars
            ])
    sheet.append_row(["", "", ""])

    sheet.append_row([
        "Worst-case return (%)",])

def write_ai_explanation(explanation_text):
    sheet = open_sheet().worksheet("AI_Explanation")

    sheet.clear()

    lines = explanation_text.split("\n")

    for line in lines:
        sheet.append_row([line])


