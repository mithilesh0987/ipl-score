import pickle
import pandas as pd

# Load the trained model
with open('model/score_predictor.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_score(input_data):
    # Convert input data into DataFrame for model prediction
    input_df = pd.DataFrame([input_data])
    input_df = pd.get_dummies(input_df)

    # Ensure all columns match the training data
    required_columns = model.feature_names_in_
    for col in required_columns:
        if col not in input_df:
            input_df[col] = 0

    # Predict score using the trained model
    predicted_score = model.predict(input_df)
    return predicted_score[0]
