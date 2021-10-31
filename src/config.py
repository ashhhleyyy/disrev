import os
import sys
import re
from typing import Dict, List
import dotenv
from dataclasses import dataclass
from dataclasses_json import dataclass_json

dotenv.load_dotenv()


def get_env(name: str) -> str:
    e = os.environ.get(name)
    if not e:
        print(f"Please set the environment variable {name}")
        exit(1)
    return e


WEBHOOK_ID_FROM_URL_REGEX = re.compile(r"^https:\/\/(ptb\.|canary\.)?discord\.com\/api\/webhooks/([0-9]*)/.*$")


def get_webhook_id_from_url(url: str) -> str:
    return WEBHOOK_ID_FROM_URL_REGEX.fullmatch(url).group(2)


@dataclass_json
@dataclass
class DisrevConfig:
    revolt_to_webhook: Dict[str, str]
    discord_to_revolt: Dict[str, str]

    @property
    def discord_webhook_ids(self) -> List[str]:
        return list(map(get_webhook_id_from_url, self.revolt_to_webhook.values()))


def load_config() -> DisrevConfig:
    if len(sys.argv) >= 2:
        print(f"Loading config from {sys.argv[1]}...")
        with open(sys.argv[1]) as f:
            return DisrevConfig.from_json(f.read())
    else:
        print(f"Loading config from environment variables...")
        revolt_channel = get_env("REVOLT_CHANNEL")
        discord_channel = get_env("DISCORD_CHANNEL")
        discord_webhook = get_env("DISCORD_WEBHOOK")

        return DisrevConfig(
            revolt_to_webhook={ revolt_channel: discord_webhook },
            discord_to_revolt={ discord_channel: revolt_channel },
        )


REVOLT_TOKEN = get_env("REVOLT_TOKEN")
DISCORD_TOKEN = get_env("DISCORD_TOKEN")
