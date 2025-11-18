from pydantic import BaseModel
from typing import Any, Dict, List, Optional


class PipelineStep(BaseModel):
    name: str
    job: str
    enabled: bool = True
    params: Optional[Dict[str, Any]] = None


class PipelineDefinition(BaseModel):
    input_file: str
    pipeline: List[PipelineStep]