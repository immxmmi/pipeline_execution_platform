import sys
from engine.action_registry import ACTION_REGISTRY
from config.loader import Config

class PipelineValidator:

    def validate_jobs(self, pipeline):
        cfg = Config()
        if cfg.debug:
            print("[DEBUG] Validating jobs in pipeline")
        for step in pipeline.pipeline:
            if cfg.debug:
                print(f"[DEBUG] Checking job '{step.job}' for step '{step.name}'")
            if step.job not in ACTION_REGISTRY:
                allowed = ", ".join(ACTION_REGISTRY.keys())

                print(f"❌ Invalid job '{step.job}' in step '{step.name}'.")
                print(f"   Allowed jobs: {allowed}")
                if cfg.debug:
                    print(f"[DEBUG] Validation failed for step '{step.name}' with job '{step.job}'")

                sys.exit(1)