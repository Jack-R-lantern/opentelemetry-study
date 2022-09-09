# to start tracing, you'll need to initialize a TraceProvider
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
        BatchSpanProcessor,
        ConsoleSpanExporter,
)

# to start collecting metrics, you'll need to initialize a MeterProvidr
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
        ConsoleMetricExporter,
        PeriodicExportingMetricReader,
)

# FastAPI
from fastapi import FastAPI

# random
from random import randint

# tracer
trace_provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
trace_provider.add_span_processor(processor)

# meter
metric_reader = PeriodicExportingMetricReader(ConsoleMetricExporter())
meter_provider = MeterProvider(metric_readers=[metric_reader])

# Sets the global default tracer provider
trace.set_tracer_provider(trace_provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer("tutorial_trace")

# Sets the global default meter provider
metrics.set_meter_provider(meter_provider)

# Create a meter from the global meter provider
meter = metrics.get_meter("tutorial_meter")

# Application create
app = FastAPI()

@app.get("/")
@tracer.start_as_current_span("roll_dice")
def roll_dice():
    print("doing roll...")
    return str(do_roll())

@tracer.start_as_current_span("do_roll")
def do_roll():
    return randint(1, 6)




