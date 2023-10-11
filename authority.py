import os
import pathlib
import subprocess
from datetime import datetime, timedelta

import sudo


class Authority(sudo.Plugin):
    def open(self, submit_optind: int, submit_argv: tuple) -> int:
        # check if we've played the sound recently
        last_play_path = os.path.expanduser("~/.authority-last-play")
        if os.path.exists(last_play_path):
            last_play = datetime.fromtimestamp(os.path.getmtime(last_play_path))
            if last_play > datetime.now() - timedelta(minutes=5):
                # already played recently, exit without playing
                pathlib.Path(last_play_path).touch(0o660, exist_ok=True)
                return
        pathlib.Path(last_play_path).touch(0o660, exist_ok=True)

        if not os.path.exists("/usr/bin/ffplay"):
            # because someone is inevitably going to install this without
            # installing ffmpeg first
            sudo.log_info(
                'ffmpeg needs to be installed for the "authority" sudo plugin to work!'
            )
            return

        # We use ffplay via subprocess instead of playing the sound with python
        # because it prevents the plugin from "freezing" sudo while the sound
        # plays (without prematurely cancelling playback when this plugin exits).
        with open(os.devnull, "w") as dev_null:
            subprocess.Popen(
                [
                    "/usr/bin/ffplay",
                    "-nodisp",
                    "-autoexit",
                    "/usr/local/share/sudo-authority/authority.mp3",
                ],
                # prevent ffmpeg's noisy output from messing with the terminal
                stdout=dev_null,
                stderr=dev_null,
            )
