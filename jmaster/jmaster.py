"""Main module."""

import os
import subprocess as sp
from time import sleep
import re
import json
import sys

_PID_FILE = "jupyter.pid"
_LOG = "jupyter.log"


def launch():
    with open(_LOG, "w") as f:
        po = sp.Popen(["jupyter", "lab"],
                      stdout=f,
                      stderr=sp.STDOUT,
                      text=True)
    sleep(5)
    with open(_LOG) as f:
        for l in f:
            r = re.match(r"^ +http://localhost:([0-9]+)/\?token=([0-9a-z]+)$", l)
            if r:
                port, token = r.expand(r"\1"), r.expand(r"\2")
    with open(_PID_FILE, "w") as f:
        dat = dict(
            pid=po.pid,
            port=int(port),
            token=token
        )
        json.dump(dat, f)


def open_browser():
    with open(_PID_FILE) as f:
        dat = json.load(f)
    sp.Popen(["open", f"http://localhost:{dat['port']}/?token={dat['token']}"])


def run():
    if not os.path.exists("jupyter.pid"):
        sys.stderr.write("launching new jupyter process\n")
        launch()
    else:
        sys.stderr.write("jupyter process already run\n")
        open_browser()
