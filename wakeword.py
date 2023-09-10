from elib.ai.precise import PreciseRunner, PreciseEngine
import os
from pathlib import Path

MODEL_DIR = Path(os.path.expanduser("~/ai/models"))
engine = PreciseEngine('precise-engine/precise-engine', MODEL_DIR / 'stop.tflite')
runner = PreciseRunner(engine, on_activation=lambda: print('hello'))
runner.start()

from time import sleep
while True:
    sleep(10)
