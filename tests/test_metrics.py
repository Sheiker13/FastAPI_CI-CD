from app.metrics import REQUEST_COUNT, REQUEST_LATENCY

def test_metrics_labels():
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()
    REQUEST_LATENCY.labels(endpoint="/").observe(1.23)

    assert REQUEST_COUNT._metrics[("GET", "/")]._value.get() > 0
    assert REQUEST_LATENCY._metrics[("/",)]._sum.get() > 0