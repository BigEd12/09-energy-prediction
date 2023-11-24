

def output_to_txt(err_df, pred_df):
    file_path = 'output.txt'

    with open(file_path, 'a') as file:
        header = 'Regresiones'
        file.write(header + '\n')
        rows_as_strings = err_df.apply(lambda row: f"{row['DataFrame']} {row['Coefficient']} {row['Y-Intercept']}", axis=1)
        for row_string in rows_as_strings:
            file.write(row_string + '\n')

        header = 'Errores'
        file.write(header + '\n')
        rows_as_strings = err_df.apply(lambda row: f"{row['DataFrame']} {row['MAE as %']} {row['MSE as %']}", axis=1)
        for row_string in rows_as_strings:
            file.write(row_string + '\n')

        header = 'Predicciones'
        file.write(header + '\n')
        rows_as_strings = pred_df.apply(lambda row: f"{str(row['date_time'])[:-3]} {row['pred']}", axis=1)
        for row_string in rows_as_strings:
            file.write(row_string + '\n')
            
    print(f'File has been successfully saved as {file_path}')