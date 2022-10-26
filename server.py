from flask import Flask, Request
from joblib import load

server = Flask(__name__)


# def loading_model():
#     model = load('model_random_forest_v100.pkl')



model = load('model_random_forest_v100.pkl')

@server.route('/api/predictor/<area>;<rooms>;<bathroom>;<parking_space>;<floor>;<animal>;<furniture>;<hoa>;<property_tax>', methods=['GET'])
def predictor(area, rooms, bathroom, parking_space, floor, animal, furniture, hoa, property_tax):

    hyperparameters = [
        float(area), float(rooms), float(bathroom), float(parking_space), 
        float(floor), float(animal), float(furniture), float(hoa), float(property_tax)
    ]


    print(f'\n\nHyperparameters: {hyperparameters}\n\n')

    try:
        predictor_model =  model.predict( [hyperparameters] )    
        return {'rent': f'{predictor_model}'}
    except:
        return {'Error 500': 'Predictor not working'}

if (__name__ == "__main__"):
    server.run(debug=True)


