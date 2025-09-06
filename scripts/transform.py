# ambil nilai price tanpa currency sehingga bisa jadi integer dan lebih mudah diproses
# products_df['price'].str[3:].astype(int) 

# ambil currency sehingga tahu currency nya apa yaitu Rp.
# products_df['price'].str[:2] 

# ubah tanggal pada product agar menjadi datetime YYYY-MM-DD
# pd.to_datetime(transactions_df['transaction_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
# format='%d/%m/%Y' untuk mengetahui input nya adalah tanggal-bulan-tahun
# dt.strftime('%Y-%m-%d') untuk outputnya bisa diatur yaitu adalah tahun-bulan-tanggal dengan output berbentuk string

import pandas as pd 

def transform_data(products_df, transactions_df):
    """
    Transform data products, memisahkan currency dengan price
    """
    products_df['mata_uang'] = products_df['price'].str[:2]
    products_df['price'] = products_df['price'].str[3:].astype(int) 

    """
    Transform data transaction, merapikan format tanggal
    """
    transactions_df['transaction_date'] = pd.to_datetime(transactions_df['transaction_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

    # return products_df.info()
    return transactions_df