from engine.action_registry import ACTION_REGISTRY
from engine_reader.pipeline_reader import PipelineReader

class PipelineExecutor:

    def __init__(self):
        self.reader = PipelineReader()

    def run_pipeline(self, pipeline, inputs_file):
        inputs = self.reader.load_inputs(inputs_file)

        for step in pipeline.pipeline:
            if not step.enabled:
                continue

            action_class = ACTION_REGISTRY.get(step.job)
            action = action_class()

            if step.params_list:
                key = step.params_list.replace("{{ ", "").replace(" }}", "")
                items = inputs.get(key, [])

                for params in items:
                    self._run_action(step, action, params)
                continue

            self._run_action(step, action, step.params or {})

    def _run_action(self, step, action, params):
        print(f"▶ Running step: {step.name} ({step.job})")
        response = action.execute(params)

        print(f"   ✔ Success: {response.success}")
        if response.message:
            print(f"   ✔ Message: {response.message}")
        if response.data:
            print(f"   ✔ Data: {response.data}")

        if not response.success:
            print("❌ Pipeline failed.")
            import sys
            sys.exit(1)