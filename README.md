# Project
02268 – Process-oriented and Event-driven Software Systems - Group 7

# Placing Siddhi files in your workspace
You can import the `.siddhi` files under `/siddhi/` into your WSO2 directory. It should be located under `<SIDDHI ROOT>/wso2/tooling/deployment/workspace/`

# Run Camunda Platform using Docker

```
docker pull camunda/camunda-bpm-platform:run-latest
docker run -d --name camunda -p 8080:8080 camunda/camunda-bpm-platform:run-latest
```

# Run External Event source script with Python
Requires Python >3.7

1. Create a virtual environment for python
2. Install dependencies needed to run the script: `pip install -r requirements.txt` (from the directory)
3. Run the corresponding `.py` script for the BPMN diagram. E.g. `predictive-maintenance.bpmn` with `machine_learning_model.py`

# Customer Issue Resolution (How-To)
the choices for the "selection" that camunda model will accept as the 'SelectSupportOption' and 'Choice' variables in the Customer and Webpage processes respectively are the Strings: "new","transfer" and "cancel".
The diagram flows well but some user tasks and other tasks have been implemented just for the show-case and testing of the model :)
