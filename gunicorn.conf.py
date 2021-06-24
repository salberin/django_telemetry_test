import multiprocessing

from opentelemetry import trace
from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

worker_class = "gevent"
timeout = 120
workers = 3
max_requests = 500
max_requests_jitter = 50
worker_tmp_dir = '/dev/shm'


def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)

    resource = Resource.create(attributes={"service.name": "telemtry-test"})

    trace.set_tracer_provider(TracerProvider(resource=resource))
    span_processor = BatchSpanProcessor(
        CloudTraceSpanExporter()
    )
    trace.get_tracer_provider().add_span_processor(span_processor)
