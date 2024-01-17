import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "23849039"))
    API_HASH = os.environ.get("API_HASH", "1673e33ac8001f6c446485b3bfd6cefa")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6965991576:AAGg7COKv_PQ1go2uQ0DMRcE9AzGXDdgMuc")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "snaptdown_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
