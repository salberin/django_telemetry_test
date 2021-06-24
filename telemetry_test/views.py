from django.http import HttpResponse
from opentelemetry import trace


def index(request):
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("foo"):
        return HttpResponse("Hello, world...")
