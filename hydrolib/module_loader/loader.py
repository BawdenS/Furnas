import pandas as pd


def load(file_import):
    df = pd.read_excel(file_import);
    # df.dropna(inplace = True)
    # df.drop(df[df['Nome da usina'].empty].index, inplace=True)
    # df.dropna(subset=['Nome da usina'])
    # file_imported = df.dropna()
    # # new_df = df.dropna()
    return df

def somador(a,b):
    return a+b

