import pandas as pd 


def ekstrak_csv(path):
    """

    Meng-extract file csv sesuai path yang dituju

    path = lokasi file csv
    return = hasil extract 

    """
    return pd.read_csv(path)

def ekstrak_json(path):
    """

    Meng-extract file json sesuai path yang dituju

    path = lokasi file json
    return = hasil extract 

    """
    return pd.read_json(path)

