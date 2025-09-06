from config.setting import PRODUCTS_PATH, USERS_PATH, TRANSACTIONS_PATH, OUTPUT_PATH
from scripts.extract import ekstrak_csv, ekstrak_json
from scripts.transform import transform_data

# Command Extract CSV dan JSON
products_df = ekstrak_csv(PRODUCTS_PATH)
transactions_df = ekstrak_csv(TRANSACTIONS_PATH)
users_df = ekstrak_json(USERS_PATH)

# Command Transform
afterTransform = transform_data(products_df, transactions_df)
print(afterTransform)

