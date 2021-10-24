import os
import dotenv

dotenv.load_dotenv()


def get_env(name: str) -> str:
    e = os.environ.get(name)
    if not e:
        print(f"Please set the environment variable {name}")
        exit(1)
    return e


REVOLT_TOKEN = get_env("REVOLT_TOKEN")
REVOLT_CHANNEL = get_env("REVOLT_CHANNEL")
DISCORD_TOKEN = get_env("DISCORD_TOKEN")
DISCORD_CHANNEL = get_env("DISCORD_CHANNEL")
DISCORD_WEBHOOK = get_env("DISCORD_WEBHOOK")
