from flask import Flask, render_template, request, jsonify
from model.predictor import predict_score

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print(f"Received data: {data}")  # Debugging line
        team = data['team']
        opponent_team = data['opponent_team']
        venue = data['venue']
        overs = data['overs']
        wickets = data['wickets']

        # Prepare the input for the model prediction
        input_data = {
            'team': team,
            'opponent_team': opponent_team,
            'venue': venue,
            'overs': overs,
            'wickets': wickets
        }

        # Call the model's prediction function
        predicted_score = predict_score(input_data)
        print(f"Predicted Score: {predicted_score}")  # Debugging line
        return jsonify({"predicted_score": predicted_score})

    except Exception as e:
        print(f"Error: {str(e)}")  # Debugging line
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
