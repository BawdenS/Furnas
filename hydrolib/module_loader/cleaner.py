# import pandas as pd
# def limpa_linhas(df): #Old
#     data = pd.DataFrame();
#     myString = ""
#     j = 0;
#     for i in range(0,len(df)):
#         myString = df.loc[i][1]; 
#     if  pd.isna(myString) or myString == "" or myString.isspace():
#         j = j+1; #conta o numeros de coluna em branco, nula ou vázias ou tab/espaço
#     else: data = data.append(df.loc[i]);
#     data = data.reset_index()
#     data = data.drop(columns=['index'])
#     data.shape[0]
#     return data

def clean(df):
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