# Project
02268 – Process-oriented and Event-driven Software Systems - Group 7

# Placing Siddhi files in your workspace
You can import the `.siddhi` files under `/siddhi/` into your WSO2 directory. It should be located under `<SIDDHI ROOT>/wso2/tooling/deployment/workspace/`

# Run Camunda Platform using Docker

```
docker pull camunda/camunda-bpm-platform:run-latest
docker run -d --name camunda -p 8080:8080 camunda/camunda-bpm-platform:run-latest
```
