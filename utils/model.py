import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def errors(dfs):
    columns = ['DataFrame', 'Coefficient', 'Y-Intercept', 'MAE as %', 'MSE as %']
    res_df = pd.DataFrame(columns=columns)
    lin_regs = []
    
    for i, df in enumerate(dfs):
        X = df[['Speed (m/ps)']]
        y = df['observacion']

        X_train, X_test, y_train, y_test = train_test_split(X, 
                                                            y, 
                                                            test_size=0.2,
                                                            random_state=42
                                                           )

        lin_reg = LinearRegression()
        lin_reg.fit(X_train, y_train)

        y_intercept = round(lin_reg.intercept_, 2)
        coef = round(lin_reg.coef_[0], 2)
        
        lin_regs.append(lin_reg)

        y_pred = lin_reg.predict(X_test)

        mse = round(mean_squared_error(y_test, y_pred), 2)
        mae = round(np.mean(np.abs(y_test - y_pred)), 2)
        mse_percentage = round((mse / (y_test.mean() ** 2)) * 100, 2)
        mae_percentage = round((mae / y_test.mean()) * 100, 2)

        map_dict = {
            0: 'North',
            1: 'East',
            2: 'South',
            3: 'West'
        }
        
        # Add a new row with an identifier for the DataFrame
        res_df.loc[len(res_df.index)] =[map_dict[i], coef, y_intercept, mae_percentage, mse_percentage]
    
    return res_df, lin_regs


def make_prediction(row, models):
    model_mapping = {
        'North': 0,
        'East': 1,
        'South': 2,
        'West': 3
    }
    direction = row['Direction (sector)']
    model_index = model_mapping.get(direction)
    model = models[model_index]

    speed = float(row['Speed (m/ps)'])

    X = np.array(speed).reshape(-1, 1)

    y_pred = int(round(model.predict(X)[0], 0))
    return y_pred