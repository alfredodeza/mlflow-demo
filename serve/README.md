# Local Model serving with MLflow

By serving a model you have the ability to interact with the model over an HTTP API. MLflow can serve models locally with a single command but there are some constraints you need to be aware of. In this example you'll serve a previously registered model.


## Serving a model by run

See the `log_model.py` file to programmatically retrieve a T5 model with HuggingFace Transformers and then register it into the UI. Then run inferece using the `curl` command on the `/invocations` API endpoint:

```
curl -X POST -H "Content-Type:application/json; format=pandas-split" --data '{"columns":["text"],"data":[["Today is a perfect day to practice automation skills"]]}' http://127.0.0.1:5000/invocations
```

