from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType


# model_type="llama3.1:8b",
# model_type="llama3.2:3b",
def create_ollama_model(
    model_type="llama3.2:3b",
    url="http://localhost:11434/v1",
    temperature=0.4,
    max_tokens=9999,
):
    return ModelFactory.create(
        model_platform=ModelPlatformType.OLLAMA,
        model_type=model_type,
        url=url,
        model_config_dict={
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": False,
        },
    )


def create_openai_model(temperature=0.4, max_tokens=9999):
    return ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type=ModelType.GPT_4O_MINI,
        model_config_dict=ChatGPTConfig(
            temperature=temperature,
            max_tokens=max_tokens,
            stream=False,
        ).as_dict(),
    )
