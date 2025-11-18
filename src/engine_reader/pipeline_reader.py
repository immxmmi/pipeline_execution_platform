import yaml
from pathlib import Path
from model.pipeline_model import PipelineDefinition


class PipelineReader:
    def load_pipeline(self, file_path: str) -> PipelineDefinition:
        data = yaml.safe_load(Path(file_path).read_text())
        return PipelineDefinition(**data)

    def load_inputs(self, file_path: str) -> dict:
        return yaml.safe_load(Path(file_path).read_text())

    def resolve_templates(self, pipeline: PipelineDefinition, inputs: dict):
        for step in pipeline.pipeline:
            if step.params:
                for key, value in step.params.items():
                    if isinstance(value, str) and value.startswith("{{ inputs."):
                        param_key = value.replace("{{ inputs.", "").replace(" }}", "")
                        step.params[key] = inputs.get(param_key)
        return pipeline