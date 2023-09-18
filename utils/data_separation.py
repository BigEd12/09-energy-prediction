import pandas as pd

def prepare_input_data(file_path):
    df = pd.read_csv('output.txt')
    
    index_of_pred = (df == 'predicciones').idxmax().observaciones
    
    df_in = df.iloc[:index_of_pred].copy()
    df_in[['observacion', 'U', 'V', 'T']] = df_in['observaciones'].str.split(expand=True)
    df_in.drop(columns=['observaciones', 'T'], inplace=True)
    df_in = df_in.astype(int)
    
    df_out = df.iloc[index_of_pred + 1:].copy()
    df_out.rename({'observaciones': 'predicciones'}, axis=1, inplace=True)
    df_out[['fecha', 'hora', 'U', 'V', 'T']] = df_out['predicciones'].str.split(expand=True)
    df_out['date_time'] = pd.to_datetime(df_out['fecha'] + ' ' + df_out['hora'], format='%Y-%m-%d %H:%M')
    df_out.drop(columns=['predicciones', 'T', 'fecha', 'hora'], inplace=True)
    df_out = df_out[['date_time', 'U', 'V']] 
    df_out = df_out.astype({'U': 'int', 'V': 'int64'})
    df_out = df_out.sort_values(by='date_time')
    df_out.reset_index(inplace=True)
    
    return df_in, df_out

