from engine_reader.pipeline_reader import PipelineReader
from engine.pipeline_validator import PipelineValidator
from engine.pipeline_executor import PipelineExecutor
from config.loader import Config
import sys


class PipelineEngine:

    def __init__(self, config):
        self.reader = PipelineReader()
        self.validator = PipelineValidator()
        self.executor = PipelineExecutor()
        self.config = config

    def load_pipeline(self, pipeline_file: str):
        try:
            cfg = Config()
            if cfg.debug:
                print(f"[DEBUG] Loading pipeline file: {pipeline_file}")

            pipeline = self.reader.load_pipeline(pipeline_file)
            inputs = self.reader.load_inputs(self.config.inputs_file)
            if cfg.debug:
                print(f"[DEBUG] Loaded inputs from: {self.config.inputs_file}")
                print(f"[DEBUG] Inputs content: {inputs}")

            pipeline = self.reader.resolve_templates(pipeline, inputs)
            if cfg.debug:
                print("[DEBUG] Templates resolved")

            self.validator.validate_jobs(pipeline)
            if cfg.debug:
                print("[DEBUG] Pipeline validation completed")
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
            cfg = Config()
            if cfg.debug:
                print("[DEBUG] Starting pipeline execution")

            self.executor.run_pipeline(pipeline, self.config.inputs_file)
        except Exception as e:
            cfg = Config()
            if cfg.debug:
                print(f"[DEBUG] Execution error detail: {e}")
            print(f"❌ Pipeline execution failed: {e}")
            sys.exit(1)