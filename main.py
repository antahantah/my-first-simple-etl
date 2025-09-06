from config.setting import PRODUCTS_PATH, USERS_PATH, TRANSACTIONS_PATH, OUTPUT_PATH
from scripts.extract import ekstrak_csv, ekstrak_json

# Command Extract CSV dan JSON
products_df = ekstrak_csv(PRODUCTS_PATH)
transactions_df = ekstrak_csv(TRANSACTIONS_PATH)
users_df = ekstrak_json(USERS_PATH)


