import sys
from engine.action_registry import ACTION_REGISTRY

class PipelineValidator:

    def validate_jobs(self, pipeline):
        for step in pipeline.pipeline:
            if step.job not in ACTION_REGISTRY:
                allowed = ", ".join(ACTION_REGISTRY.keys())

                print(f"❌ Invalid job '{step.job}' in step '{step.name}'.")
                print(f"   Allowed jobs: {allowed}")

                sys.exit(1)