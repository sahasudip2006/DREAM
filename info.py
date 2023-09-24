import re
import os
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/94c74580a918cb9e6b18e.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/94c74580a918cb9e6b18e.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/94c74580a918cb9e6b18e.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/229b746a9efacb4245b53.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '794968418').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001514388938').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1270873344 5232414179 794968418 5290038359 885767886').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', "")
reqst_channel = environ.get('REQST_CHANNEL_ID', "")
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others

VERIFY = bool(environ.get('VERIFY', True))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'TinyFy.in')
SHORTLINK_API = environ.get('SHORTLINK_API', 'f999bc3f142a37b8db08754279b7be7a81ef8604')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False)
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1001818118297').split()]
PORT = environ.get("PORT", "8080")
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/Ott_Movie_Request_Group')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/S_Hindi_Movie')
MSG_ALRT = environ.get('MSG_ALRT', 'Thanks To Using Me 😇')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001565949579'))
REQUEST_LOGS = int(environ.get('REQUEST_LOGS', '-1001565949579'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'filmymenchat')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

BLACKLIST_WORDS = (
    list(os.environ.get("BLACKLIST_WORDS").split(","))
    if os.environ.get("BLACKLIST_WORDS")
    else []
)

BLACKLIST_WORDS = ["@MoviesHouse8", "@Eliteflix_Official", "@TrollerMawa_Ofcl", "[D&O]", "[MM]", "[]", "[FC]", "[CF]", "LinkZz", "[DFBC]", "@New_Movie", "@Infinite_Movies2", "MM", "@R A R B G", "[F&T]", "[KMH]", "[DnO]", "[F&T]", "MLM", "@TM_LMO", "@x265_E4E", "@HEVC_MoviesZ", "SSDMovies", "@MM_Linkz", "[CC]", "@Mallu_Movies", "@DK Drama", "@luxmv_Linkz", "@Akw_links", "CK_HEVC", "@Team_HDT", "[CP]", "www 1TamilMV men", "@TamilMob_LinkZz", "@GreyMatter_Bots", "@Forever_Bros", "@TamilMvmovies2Tunnel", "@TEAM_HD4K", "@MoviezzClub", "PFM", "[GorGom]", "4U", "www", "1TamilMV", "[FHM]", "@CC", "[CF]", "MLM", "themoviesboss", "@AM_linkzz", "[MF]", "[CVM]", "[PM]", "[MM]", "aFilmywap", "[MSM]", "FG", "@Mj_Linkz", "MCArchives", "[MASHOBUC]", "[MABLG]", "Bros", "[YDF]", "HEBC", "LINKS", "www_1TamilMV_men", "Linkz", "HEVC", "[MoviesNowTamil]", "7HitMovies", "linkzz", "[JP]", "[CD]", "HD4K", "[CD]", "@MM", "[DC]", "DC", "[AnimeRG]", "[CNT]", "Moviez", "TheMoviesBoss", "bros", "Movies", "1stOnNet", "[TIF]", "()", "[MF]", "[WC]", "ғαιвεяsgαтє", "TF", "E4E", "X265", "autos", "[HCN]", "KC", "[KC]", "[Movieshd121]", "[CNT]", "Download", "[MS]", "[WMJ]", "links", "[Movie_Bazar]", "S_1", "[MF]", "[MJ]", "Filmy4cab", "24X7", "[MJ]", "M_D_B", "[Nep_Blanc]", "HDT", "tv", "M_D_B_", "wdll", "[FN]", "[mwkOTT]", "LinkZ", "MABLG_", "[MW]", "[MH]", "[Movie_Bazar]", "Links", "media", "TamilHDRip", "[MwK]", "{KMH}", "[M5]", "[A2MOVIES]", "@Movierockerzs"]
