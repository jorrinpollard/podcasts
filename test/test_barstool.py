#!/usr/bin/env python
from __future__ import division, absolute_import, print_function

import os
import sys
import unittest


cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, cwd)

from podcasts import Podcast

source = os.path.join(cwd, "test", "fixtures", "barstool.xml")

_copyright = "2019 Barstool Sports"
_type = None
author = "Barstool Sports"
categories = ['Comedy', 'Talk Radio']
description = "Follow along vlogger Alexandra Cooper and best friend Sofia Franklyn as the duo dives into the explicit details of their life in NYC. In their 20s, the two exploit the f*ck out of their lives, making you feel a hell of a lot better about yours. Relationships, sex, the NY social scene, embarrassing moments, and more are all addressed here on CALL HER DADDY."
explicit = "yes"
generator = "McSorleys by Barstool Sports"
image_url = "https://podcasts.barstoolsports.com/_images/call_her_daddy_itunes.e5b5d9abdc67.jpg"
language = "en-us"
last_build_date = "Sat, 11 May 2019 20:27:55 GMT"
link = "https://www.barstoolsports.com/shows/call-her-daddy"
managing_editor = "podcasting@barstoolsports.com (Barstool Podcasting)"
new_feed_url = "https://mcsorleys.barstoolsports.com/feed/call-her-daddy"
owner = "Barstool Sports"
pub_date = "Sun, 20 May 2012 04:00:00 GMT"
subtitle = "Follow along vlogger Alexandra Cooper and best friend Sofia Franklyn as the duo dives into the explicit details of their life in NYC. In their 20s, the two exploit the f*ck out of their lives, making you feel a hell of a lot better about yours. Relationsh"
summary = "Follow along vlogger Alexandra Cooper and best friend Sofia Franklyn as the duo dives into the explicit details of their life in NYC. In their 20s, the two exploit the f*ck out of their lives, making you feel a hell of a lot better about yours. Relationships, sex, the NY social scene, embarrassing moments, and more are all addressed here on CALL HER DADDY."
title = "Call Her Daddy"
web_master = "engineering@barstoolsports.com (Barstool Engineering)"

class TestBarstool(unittest.TestCase):
    def setUp(self):
        self.podcast = Podcast(source)

    def test_attrubites(self):

        self.assertEqual(self.podcast.source, source)
        self.assertEqual(self.podcast.author, author)
        self.assertEqual(self.podcast.categories, categories)
        self.assertEqual(self.podcast.copyright, _copyright)
        self.assertEqual(self.podcast.description, description)
        self.assertEqual(self.podcast.explicit, explicit)
        self.assertEqual(self.podcast.generator, generator)
        self.assertEqual(self.podcast.image_url, image_url)
        self.assertEqual(self.podcast.language, language)
        self.assertEqual(self.podcast.last_build_date, last_build_date)
        self.assertEqual(self.podcast.link, link)
        self.assertEqual(self.podcast.managing_editor, managing_editor)
        self.assertEqual(self.podcast.new_feed_url, new_feed_url)
        self.assertEqual(self.podcast.owner, owner)
        self.assertEqual(self.podcast.pub_date, pub_date)
        self.assertEqual(self.podcast.subtitle, subtitle)
        self.assertEqual(self.podcast.summary, summary)
        self.assertEqual(self.podcast.title, title)
        self.assertEqual(self.podcast.type, _type)
        self.assertEqual(self.podcast.web_master, web_master)

if __name__ == "__main__":
    unittest.main()
