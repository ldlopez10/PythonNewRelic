# PythonNewRelic

Basic Python serverless function with New Relic Monitoring

## Development Environment Set Up

1. Install Python on your machine [Install Python Docs](https://www.python.org/downloads/)

   - verify install
   - `python3 --version` or `python --version`

2. Install **[Azure function Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cstorageexplorer%2Cv2%2Cbash&pivots=programming-language-python)**

   **MAC installation:**

   - `brew install azure-functions-core-tools@4`

   - verify install
   - `func --version`

3. [Create New Relic account](https://newrelic.com/signup)
   - Free account per single email

## How to Run this function

1. Create a virtual environment by running
   - `python -m venv .venv`
2. Activate your virtual environment by running
   - `source .venv/Scripts/activate`
   - If this does not work try: `source .venv/bin/activate`
3. Install requirements.txt
   - `pip install -r requirements.txt`
4. Run the function
   - `func start`

If you have a New Relic account created add your New Relic licence Key to the local.setting.json file and run the function

`NEW_RELIC_LICENSE_KEY": "123456789NRAL`

## Endpoints

http://localhost:7071/api/HttpTriggerFunc

http://localhost:7071/api/HttpTriggerFunc?name=johndoe

## New Relic

Navigate to https://one.newrelic.com/ then click APM & Services tab to see your data

- [NewRelic University](https://learn.newrelic.com/page/courses) (New Relic training courses)

- **[Python NewRelic Agent Docs](https://newrelic.com/signup)**
  - see new relic python agent methods that you can use to track your data
-

## External API Cat-Facts

https://alexwohlbruck.github.io/cat-facts/docs/
