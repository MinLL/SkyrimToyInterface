from constants import *
## Edit the following variables to configure this script

# Important variables to configure for all users:
LOG_PATH = '../Documents/My Games/Skyrim VR/Logs/Script/Papyrus.0.log' # Full path to the Papyrus log that the script should parse
CHARACTER_NAME = "Min"  # The name of your character. 

# Toy configuration
TOY_TYPE = [TOY_COYOTE, TOY_LOVENSE]
DD_VIB_MULT = 2  # Duration of vibration event is multiplied by this value. 
WARN_ON_STACK_DUMP = True  # Loop short vibrations to notify user of Stack Dumps. Set to False to disable.

# Configuration if using Chaster:
CHASTER_TOKEN = ""

LOCK_NAME = "Self-lock"  # The name of the lock to manipulate. Must be unique.
# LOCK_NAME = "Keyholder lock"  # The name of the lock to manipulate. Must be unique.
# Chaster + Sexlab Defeat Configuration
CHASTER_DEFEAT_MIN = 60 * 60 * 4  # Minimum number of hours to add on party defeat
CHASTER_DEFEAT_MAX = CHASTER_DEFEAT_MIN * 2  # Maximum number of hours to add on party defeat

