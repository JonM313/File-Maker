#!/usr/bin/python
# -*- coding: utf-8 -*-

from newsdownload import download_zeit_german
from newsmake import download_source

download_source("ZEIT German", "zeit_german", "https://rc24.xyz/images/webhooks/news/afp_german.png", 2, ["065", "066", "067", "074", "076", "077", "078", "079", "082", "083", "088", "094", "095", "096", "098", "105", "107", "108", "110"], download_zeit_german())
