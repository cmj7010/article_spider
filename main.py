# !usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:Charlie

import sys
import os
from scrapy.cmdline import execute

sys.path.append( os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl"])