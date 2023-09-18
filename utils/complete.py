from utils.data_separation import prepare_input_data
from utils.data_model_preprocessing import preprocessing, add_wind_speed, wind_radians_degrees, direction_sector, prepare_data_for_prediction
from utils.model import errors, make_prediction
from utils.output import output_to_txt

def full_sequence(file_name):
    obs_df, pred_df = prepare_input_data(file_name)

    n_df, e_df, s_df, w_df = preprocessing(obs_df)

    errors_df, models = errors([n_df, e_df, s_df, w_df])

    prepped_df = prepare_data_for_prediction(pred_df)

    prepped_df['pred'] = prepped_df.apply(make_prediction, axis=1, models=models)

    output_to_txt(errors_df, pred_df)