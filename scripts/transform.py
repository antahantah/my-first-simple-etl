# ambil nilai price tanpa currency sehingga bisa jadi integer dan lebih mudah diproses
# products_df['price'].str[3:].astype(int) 

# ambil currency sehingga tahu currency nya apa yaitu Rp.
# products_df['price'].str[:2] 

def transform_data(products_df):
    products_df['mata_uang'] = products_df['price'].str[:2]
    products_df['price'] = products_df['price'].str[3:].astype(int) 

    return products_df.info()