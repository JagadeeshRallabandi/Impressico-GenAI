from typing import Dict, Union, Any, List

from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentAction
from uuid import UUID
from langchain.schema.output import LLMResult


# First, define custom callback handler implementations
class CustomOpenAICallback(BaseCallbackHandler):
    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        self.print_message(
            f"on_llm_start and following are the prompts: {prompts}",
        )

    # def on_llm_new_token(self, token: str, **kwargs: Any) -> Any:
    #     pprint(f"on_new_token {token}")

    def on_llm_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        self.print_message(f"on_llm_error {error}")

    def on_llm_end(
        self,
        response: LLMResult,
        *,
        run_id: UUID,
        **kwargs: Any,
    ) -> Any:
        self.print_message(f"on_llm_end {response}")

    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        self.print_message(f"on_chain_start and inputs are: {inputs}")

    def on_chain_end(
        self,
        outputs: Dict[str, Any],
        *,
        run_id: UUID,
        **kwargs: Any,
    ) -> None:
        self.print_message(f"on_chain_end and inputs are: {outputs}")

    def on_tool_start(
        self, serialized: Dict[str, Any], input_str: str, **kwargs: Any
    ) -> Any:
        self.print_message(f"on_tool_start and inputs are: {input_str}")

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        self.print_message(f"on_agent_action {action}")

    def print_message(self, message):
        print("DEBUGDEMO: " + message)
