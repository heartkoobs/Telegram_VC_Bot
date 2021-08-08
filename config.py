HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["3888634"])
    API_HASH = environ["77168685ab2dbd9ab1f7cf1ca9ebd044"]
    SESSION_STRING = environ[
        "AQCtTJpcTWFybT-VnFFn4SYwCTqegeH2JQDnWeSJEZZtB-_L5TGpJKwOKn7dYEeUfFR71O5gfCV4hKEaQdTTebATinSNS3ji7UCEi5TIz0IQkN7If6odOVtSNu0hMqgtjPXJZqOWjGy8FA3BGcG67fgAxkpPzt9HvLUfPpIHGPZtoCzMw6WhsNk1wiiDudSdaoxee-JG9OZRfG0MAO51pw_cbhtuSjZpyJ_76ezsiwm--4bGMlu2z8beozSioM-5fYeOhHaKxOh2h9DSpKc-MDGN-Rb7oP1O2wdBLwU8FgnMdVo_9J4ARaxmKeoJWYGaoOF58Fm-uE1pZaiSGf_FCZUHYZebZQA"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["LHDTAS-HVWPGP-GCVXZJ-PGUXNH-ARQ"]
    CHAT_ID = int(environ["CHAT_ID"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"
    BITRATE = int(environ["BITRATE"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    ARQ_API_KEY = "Get this from @ARQRobot"
    CHAT_ID = -100546355432
    DEFAULT_SERVICE = "saavn"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320

# don't make changes below this line
ARQ_API = "https://thearq.tech"
