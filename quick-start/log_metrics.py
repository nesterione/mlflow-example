import os
from mlflow import log_metric, log_param, log_artifact, set_tracking_uri, set_experiment


if __name__ == "__main__":
    set_tracking_uri(os.environ["MLFLOW_HOST"])
    set_experiment("my-experiment2")

    # Log a parameter (key-value pair)
    log_param("param1", 5)

    # Log a metric; metrics can be updated throughout the run
    log_metric("foo", 1)
    log_metric("foo", 2)

    # Log an artifact (output file)
    with open("output.txt", "w") as f:
        f.write("Hello world!")
    log_artifact("output.txt")
