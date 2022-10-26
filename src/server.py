from flask import Flask, Request
from joblib import load
from sqlite3 import connect
from datetime import datetime

server = Flask(__name__)

model_file = '../model/model_random_forest_v100.pkl'
model = load(model_file)


@server.route('/api/predictor/<area>;<rooms>;<bathroom>;<parking_space>;<floor>;<animal>;<furniture>;<hoa>;<property_tax>', methods=['GET'])
def predictor(area, rooms, bathroom, parking_space, floor, animal, furniture, hoa, property_tax):

    date_started = datetime.now()
        
    hyperparameters = [
        float(area), float(rooms), float(bathroom), float(parking_space), 
        float(floor), float(animal), float(furniture), float(hoa), float(property_tax)
    ]


    print(f'\n\n[DEBUG] --- Hyperparameters: {hyperparameters}\n\n')

    try:
        predictioned_rent =  model.predict( [hyperparameters] )    
        print(f'\n\n[DEBUG] --- predictioned_rent: {predictioned_rent}\n\n')

        date_finished = datetime.now()
        processing_time = date_finished - date_started

        print(f'\n\n[DEBUG] --- processing_time: {processing_time}\n\n')

        applicationModelList = hyperparameters
        applicationModelList.append(str(predictioned_rent))

        print(f'\n\n[DEBUG] --- applicationModelList: {applicationModelList}\n\n')

        input=''
        for value in applicationModelList:
            input += ';' + str(value)

        query_insert = f'''
            INSERT INTO log_api (inputs, date_started, date_finished, processing_time )
            values ( '{input}', '{date_started}', '{date_finished}', '{processing_time}' )
        '''

        db = '../database/bd_api.db'
        conn_db = connect(db)
        cursor_db = conn_db.cursor()
        
        cursor_db.execute(query_insert)
        conn_db.commit()
        cursor_db.close()

        return {'Expected Rent': f'{predictioned_rent}'}

    except:
        return {'Error 500': 'Problem during prediction'}

if (__name__ == "__main__"):
    server.run(debug=True)


