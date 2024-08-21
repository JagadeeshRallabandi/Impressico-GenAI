from typing import Any, Dict, List, Optional
from uuid import UUID
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema.output import LLMResult



class CustomOpenAICallback(BaseCallbackHandler):
  
  def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], *, run_id: UUID, parent_run_id: UUID | None = None, tags: List[str] | None = None, metadata: Dict[str, Any] | None = None, **kwargs: Any) -> Any:
    print(f"on_llm_start: {prompts}")

  def on_llm_end(self, response: LLMResult, *, run_id: UUID, parent_run_id: UUID | None = None, **kwargs: Any) -> Any:
    print(f"on_llm_end: {response}")