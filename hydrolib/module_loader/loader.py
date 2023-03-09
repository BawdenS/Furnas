# import pandas as pd


def limpa_linhas(df):
    data = pd.DataFrame(df.loc[0])
    data = data.transpose()
    # data[0] = df.loc[0]
    print((data))
    myString = ""
    j = 0
    # for i in range(1,len(df)):
    for i in range(0,len(df)):
        myString = df.loc[i][1]; 
        if  not(pd.isna(myString) or myString == "" or myString.isspace()):
           data.loc[j] = df.loc[i]
           j=j+1
    data = data.reset_index()
    data = data.drop(columns=['index'])
    return data

def load(file_import):
    df = pd.read_excel(file_import);
    # df.dropna(inplace = True)
    # df.drop(df[df['Nome da usina'].empty].index, inplace=True)
    # df.dropna(subset=['Nome da usina'])
    # file_imported = df.dropna()
    # # new_df = df.dropna()
    file_imported = limpa_linhas(df)
    return file_imported

def somador(a,b):
    return a+b

