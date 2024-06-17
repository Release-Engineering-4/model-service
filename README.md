# model-service
The model-service represents a wrapper service for the URL phishing model. It offers a REST API to expose the model to other components and make it scalable.

# Usage

**Prerequisites**: Make sure [Docker](https://www.docker.com/) is installed on your device.

To pull the latest docker image use:

```bash
docker pull ghcr.io/release-engineering-4/model-service:v0.0.3
```

To run the docker container use: 

```bash
docker run --name container_name -d -p 5000:8080 ghcr.io/release-engineering-4/model-service:v0.0.3
```

Example of how to get a prediction using a POST HTTP request with a given URL input:

```bash 
POST http://localhost:5000/predict HTTP/1.1
Content-Type: application/json

{
    "url": "https://sample_url.com"
}
```

# Testing 

To run the tests for the pre-processing library use:

```bash
pytest
```

To run the tests with coverage for the pre-processing library use:

```bash
coverage run -m pytest
```

To generate the coverage report use:

```bash
coverage report -m -i
```

To generate the html of the coverage report use:

```bash
coverage html -i
```



# Support 

If you encounter any problems or bugs with `model-service`, feel free to open an issue on the project repository.
