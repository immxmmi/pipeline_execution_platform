from engine_reader.pipeline_reader import PipelineReader
from engine.pipeline_validator import PipelineValidator
from engine.pipeline_executor import PipelineExecutor
import sys


class PipelineEngine:

    def __init__(self, config):
        self.reader = PipelineReader()
        self.validator = PipelineValidator()
        self.executor = PipelineExecutor()
        self.config = config

    def load_pipeline(self, pipeline_file: str):
        try:
            pipeline = self.reader.load_pipeline(pipeline_file)
            inputs = self.reader.load_inputs(self.config.inputs_file)
            pipeline = self.reader.resolve_templates(pipeline, inputs)

            self.validator.validate_jobs(pipeline)
            return pipeline

        except Exception as e:
            print(f"❌ Pipeline validation failed: {e}")
            sys.exit(1)

    def debug_print(self, pipeline):
        print("📌 Loaded Pipeline:")
        for step in pipeline.pipeline:
            print(f"Step: {step.name}")
            print(f"  job: {step.job}")
            print(f"  enabled: {step.enabled}")
            print(f"  params: {step.params}")
            print(f"  params_list: {step.params_list}")
            print()

    def run(self, pipeline):
        try:
            self.executor.run_pipeline(pipeline, self.config.inputs_file)
        except Exception as e:
            print(f"❌ Pipeline execution failed: {e}")
            sys.exit(1)