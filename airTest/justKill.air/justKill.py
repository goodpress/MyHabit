# -*- encoding=utf8 -*-
__author__ = "wyk"

from airtest.core.api import *

auto_setup(__file__)


stop_app("com.tencent.mm")
sleep(2)
touch(Template(r"tpl1525452724649.png", record_pos=(0.422, 0.756), resolution=(1080.0, 1920.0)))
sleep(6)

