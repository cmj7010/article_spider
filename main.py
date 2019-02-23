# !usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:Charlie

from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scarpy","crawl","jobbole"])
#execute(["scarpy","crawl","zhihu"])