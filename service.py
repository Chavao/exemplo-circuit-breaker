import requests

from circuit import CircuitBreakerConfig


@CircuitBreakerConfig()
def first_method():
    response = requests.get("http://0.0.0.0:8631/index.html")

    return response.content


@CircuitBreakerConfig()
def second_method():
    response = requests.get("http://0.0.0.0:8632/index.html")

    return response.content
