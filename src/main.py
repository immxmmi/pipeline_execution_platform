from engine.pipeline_engine import PipelineEngine
from config.loader import Config

config = Config()
if config.debug:
    print("[DEBUG]: Loaded configuration:", config.__dict__)
engine = PipelineEngine(config)

pipeline = engine.load_pipeline(config.pipeline_file)
if config.debug:
    engine.debug_print(pipeline)
engine.run(pipeline)