import asyncio
import logging
from pprint import pprint as print

from savant.switch import Switch, AudioSwitch, VideoSwitch

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger("savant").setLevel(logging.DEBUG)
switches = [AudioSwitch("192.168.1.19"), VideoSwitch("192.168.1.23")]

async def main():
    for s in switches:
        print(await s.get_switch_state())

if __name__ == "__main__":
    asyncio.run(main())
