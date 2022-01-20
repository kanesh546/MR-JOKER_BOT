# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/mrjoker/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID =  13303918 # integer value, dont use ""
    API_HASH = "24f473f4478796b9a416e4e68b49ab25"
    BOT_ID = "5063706531"
    TOKEN = "5063706531:AAFeR7pzJronQkpyuYxHxCDhcGYurnQxy8c"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 916028993 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Singleboy546"
    SUDO_USERS = "916028993"
    SUPPORT_USERS = "916028993"
    SUPPORT_CHAT = "bbYiw"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001776212077
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001776212077
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = " postgresql://postgres:eP1tQFTZj5s57Z7RbfYU@containers-us-west-22.railway.app:7214/railway"  # needed for any database modules
    REDIS_URI = " "
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    INFOPIC = True
    URL = None
    HEROKU_API_KEY = ""
    HEROKU_APP_NAME = ""
    BOT_USERNAME = "@gm_newbot"
    SPAMWATCH_API = "uyMrTbnUfQcraw5B7Pgn3JHZLPBt_dijS5ZhbIK3rKWFkcfZTjmateY4nSgx9Ofo"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    ARQ_API_KEY = "GBVANC-POIBJH-XAYVHT-XZBPTG-ARQ"
    ARQ_API_URL = "https://thearq.tech/"
    TEMP_DOWNLOAD_DIRECTORY = "./"
    OPENWEATHERMAP_ID = ""
    VIRUS_API_KEY = ""
    REDIS_URL = ""
    LASTFM_API_KEY = ""
    

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    ALLOW_CHATS = ""
    DRAGONS = "916028993"
    WHITELIST_USERS = "916028993"
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = "916028993"
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = "916028993"
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = "916028993"
    WOLVES = "916028993"
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = "CAACAgEAAxkBAAEBmkphzeVQlkYV9Xft7SNoXNDLXB2U2AACLwADnjOcH-wxu-ehy6NRHgQ"  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "O6FGAQ3BYSIPE48P"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "Y3JQK0TJ6NVF"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "xyz"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "d50ac1930db5722c348d36ed5eac5e2020a6fe1ab07eb3f39658e2c44350d9c4d7f389097b92b80b28137a678159ab36fd9b944621e7e7bfaf4b68d2df508144"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    REM_BG_API_KEY = "THcRAj2BVa8E8urCgEFoNwz4"
    GENIUS_API_TOKEN = ""
    MONGO_DB = "mongodb+srv://Friday546:friday546@cluster5.opdei.mongodb.net/friday546?retryWrites=true&w=majority"
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
