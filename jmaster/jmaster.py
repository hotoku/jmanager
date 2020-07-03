"""Main module."""

import os
import subprocess as sp
from time import sleep
import re
import json

_PID = "jupyter.pid"
_LOG = "jupyter.log"


def launch(pid=_PID):
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
    with open(pid, "w") as f:
        dat = dict(
            pid=po.pid,
            port=port,
            token=token
        )
        json.dump(dat, f)


def run():
    if not os.path.exists("jupyter.pid"):
        launch()
    else:
        print("already existing")
        # dat = read_pid()
        # open_browser()
        pass
