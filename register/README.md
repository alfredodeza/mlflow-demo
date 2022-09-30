## Register Models and retrieve them

Registering models is a big step towards reproducibility in ML. Until recently, there was no versioning for datasets or models. MLflow has the ability to register, track, and retrieve models. This aligns MLflow very well with cloud providers like Azure that offers the ability to track models in similar ways.


The basis of model versioning is a [Model Registry](https://mlflow.org/docs/latest/model-registry.html). Model versions are tracked automatically and sequentially. You don't need to specify what the version of a model _is_ in order to save it.

You *must* use `log_model` to register a new model. It isn't possible to add a model without having that done.


### Use an existing model to register it

In this example, we use an [ONNX T5 model](https://github.com/onnx/models/tree/main/text/machine_comprehension/t5) to register it. You can use the `MlflowClient` to create it with the API:

```python
from mlflow import MlflowClient

client = MlflowClient()
client.create_registered_model("onnx-t5")
```

You can fetch this model with

```
model_name = "onnx-t5"
model_version = 1

model = mlflow.pyfunc.load_model(
    model_uri=f"models:/{model_name}/{model_version}"
)

```
