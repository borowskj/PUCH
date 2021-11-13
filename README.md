## Translator App

This will be a translator app using Azure Cognitive Services

## Running App

Install and setup Flask:
https://flask.palletsprojects.com/en/2.0.x/installation/

After completing these steps, the command below should show the flask and python versions:

```
flask --version
```

Install requests:

```
pip install requests
```

Setting up `FLASK_APP` environment variable:

```
set FLASK_APP=app.py
```

To run application use:

```
flask run
```

## Use Cases
![alt text](https://github.com/borowskj/PUCH/blob/master/images/use_cases.png?raw=true)


## Architecture diagram
![alt text](https://github.com/borowskj/PUCH/blob/master/images/architecture.png?raw=true)

## Technology
- Web App - Flask
- Azure Services:
  - Azure Functions:
  - Cognitive Services:
    - Translator
    - Speech Service
    - Computer Vision
    - Language Service


