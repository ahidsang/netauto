#!/bin/env python3
#-*- coding: utf-8 -*-

import mylog
import os

logfile = "/var/log/boot.log.1"
file_length = os.path.getsize(logfile)

mylog.printlog(logfile, "OK", int(file_length/2), 3, 5)
