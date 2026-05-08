#rosie/distro.py
import os
from dataclasses import dataclass

def get_distro():
    return os.environ.get("ROS_DISTRO", None)

@dataclass
class Distro:
    name: str                                               # "humble" | "iron" | "jazzy"
    eol: bool                                               # is this distro end of life
    middleware: str                                         # default middleware (fastdds, cyclonedds)
    supported_commands: dict[str,dict[str,list[str]]]       # which ros2 CLI commands are supported
    quirks: list[str]                                       # known bugs/issues to inject into prompt
    python_version: str                                     # python version for different distros

HUMBLE = Distro(
    name="humble",
    eol=False,
    middleware="fastdds",
    supported_commands={
        "ros2":{
            "action":['info','list','send_goal','show'],
            "bag":['info','play','record'],
            "component":['list','load','standalone','types','unload'],
            "daemon":['start','status','stop'],
            "doctor":[],
            "extension_points":[],
            "extensions":[],
            "interface":['list','package','packages','proto','show'],
            "launch":[]
        }

    },
    quirks=[],
    python_version="3.11"

)