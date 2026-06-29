from backend.agents.state import Source
from backend.llm.ollama_client import OllamaClient
from backend.prompts.research_prompt import RESEARCH_PROMPT


class ResearchClient:
    def __init__(self, llm_client: OllamaClient):
        self.llm_client = llm_client

    def summarize(self, topic: str, sources: list[Source]) -> str:
        formatted_sources = ""
        parts = []

        for source in sources:
            parts.append(f"""
            Title: 
            {source.title}

            URL:
            {source.url}

            Content: 
            {source.content[:500]}
            ----------------------------------
            """)

        formatted_sources = "\n".join(parts)
        # print(len(source.content))

        prompt = RESEARCH_PROMPT.format(topic=topic, sources=formatted_sources)

        try:
            return self.llm_client.generate(prompt)
        except Exception as e:
            raise RuntimeError(f"Research summarization failed: {e}")
