import numpy as np
import pandas as pd

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from settings.constants import quests_table_name, users_table_name, json_route, scope

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_route, scope)
client = gspread.authorize(credentials)

quests_table = client.open(quests_table_name)
users_table = client.open(users_table_name)


def get_quest_df(quest_name):
    return __get_df(quests_table, quest_name)


def get_users_df(quest_name):
    return __get_df(users_table, quest_name)


def __get_df(table, sheet_name):
    sheet = table.worksheet(sheet_name)

    data = np.array(sheet.get_all_values())
    records = data[1:]
    columns = data[0]

    df = pd.DataFrame(records, columns=columns)

    return df
