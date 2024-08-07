This is a flask web-app that takes x-ray pictures as input and predicts if it has tuberculosis or not.
The model used is a CNN model.

##Create a virtual environment
    $ python3 -m venv <enviroment_name>

##Activate a virtual environment
    #On_Linux:
        $ source <enviroment_name>/bin/activate
    #On_Windows:
        $ <enviroment_name>/Scripts/activate

##Install libraries
    $ pip install -r requirements.txt

##Run the preprocessing script:
    $ python3 ./model/preprocessing.py

##Train & Save Model:
    $ python3 ./model/tb_cnn_model.py

##Run Flask App:
    $ python3 app.py