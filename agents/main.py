from pydantic_ai import Agent


class GeminiModels:
    flash = "gemini-2.5-flash"
    flash_lite = "gemini-2.5-flash-lite"


agent = Agent(
    GeminiModels.flash_lite,
    instructions="Be concise, answer with one sentence."
)


def main():
    result = agent.run_sync("What's a goroutine?")
    print(result)


if __name__ == "__main__":
    main()
