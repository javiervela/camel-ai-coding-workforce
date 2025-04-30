from camel.societies.workforce import Workforce
from camel.agents import ChatAgent
from camel.messages import BaseMessage

from camel_ai_coding_workforce.model import create_openai_model  # , create_ollama_model

WORKFORCE_DESCRIPTION = (
    "Coder Agent Workforce: Coding agents that can write, review, and test code."
)

DEFAULT_TASK = "Write a Python function to calculate the factorial of a number."


def create_workforce(description, agent_configurations):
    # model = create_ollama_model(model_type="llama3.2:3b")
    # model = create_ollama_model(model_type="llama3.1:8b")
    model = create_openai_model()

    workforce = Workforce(
        description=description,
        coordinator_agent_kwargs={"model": model},
        task_agent_kwargs={"model": model},
        new_worker_agent_kwargs={"model": model},
    )

    for _, agent_config in agent_configurations.items():
        agent = ChatAgent(
            system_message=BaseMessage.make_assistant_message(
                role_name=agent_config.get("role_name"),
                content=agent_config.get("system_message"),
            ),
            model=model,
            tools=agent_config.get("tools"),
        )

        workforce.add_single_agent_worker(
            description=agent_config.get("description"),
            worker=agent,
        )

    return workforce
