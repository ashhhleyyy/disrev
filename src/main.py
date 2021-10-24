#!/usr/bin/env python3
import asyncio
import logging
from controller import DisrevController
import revolt_bridge
import discord_bridge


def main():
    # Make revolt.py shut up. It logs an info level message every time it sends a heartbeat
    logging.getLogger('revolt').setLevel(logging.ERROR)

    controller = DisrevController()
    asyncio.get_event_loop().run_until_complete(asyncio.gather(
        revolt_bridge.run_revolt(controller),
        discord_bridge.run_discord(controller),
    ))


if __name__ == '__main__':
    main()
