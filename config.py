import os

API_ID = API_ID = 29540156

API_HASH = os.environ.get("API_HASH", "775d47859519f34f01549344a392280b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6692879342:AAGxaRJhlHIn_A5Iw-rcdOYPC1fyJF7z8iM")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6629411642))

LOG = -1002029805707

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6629411642").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


