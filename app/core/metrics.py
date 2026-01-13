from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "inference_requests_total",
    "Total number of inference requests",
)

REQUEST_LATENCY = Histogram(
    "inference_request_latency_seconds",
    "Inference request latency",
)
