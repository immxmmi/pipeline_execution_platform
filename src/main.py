from engine.pipeline_engine import PipelineEngine

if __name__ == "__main__":
    engine = PipelineEngine()
    pipeline = engine.load_pipeline("pipelines/pipeline2.yaml")
    engine.debug_print(pipeline)
    engine.run_pipeline(pipeline)