## Machine Learning project with Flask API

It contains my ML project involving rental price recommendation based on `area`, `rooms`, `bathroom`, `parking_space`, `floor`, `animal`, `furniture`, `hoa`, and `property tax`. This project was accomplished during [Machine Learning | Solução completa end-to-end (Python)](https://www.udemy.com/course/machine-learning-solucao-completa-end-to-end-api/), an Udemy course. I


The command below clone this repository.

```
$ git clone https://github.com/Samuellucas97/ML-E2E-Course.git
$ cd ML-E2E-Course
```

### Requirements


- Python ( version _3.8.10_ )

- Numpy ( version _1.23.4_ )
    - Use the following command to install: `pip install numpy`

- Pandas ( version _1.5.1_ )
    - Use the following command to install: `pip install pandas`

- Seaborn ( version _0.12.1_ )
    - Use the following command to install: `pip install seaborn`

- Sckit-learn ( version _1.1.3_ )
    - Use the following command to install: `pip install sklearn`

- Yellowbrick (version _1.5_ )
    - Use the following command to install: `pip install yellowbrick`

- Joblib ( version _1.2.0_ )
    - Use the following command to install: `pip install joblib`


- Flask ( version _2.2.2_ )
    - Use the following command to install: `pip install flask`


You could check your Sckit-learn lib version, for example, using the following commands on Python interpreter:

```
>>> import sklearn
>>> print('The scikit-learn version is {}.'.format(sklearn.__version__))
```

### How to run

Since you have installed software requirements, you need to execute on the terminal the following command:

```
$ python server.py
```

A Flask server will be running on [http://127.0.0.1:5000](http://127.0.0.1:5000).