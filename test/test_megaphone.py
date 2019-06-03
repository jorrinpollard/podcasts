#!/usr/bin/env python
from __future__ import division, absolute_import, print_function

import os
import sys
import unittest


cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, cwd)

from podcasts import Podcast

source = os.path.join(cwd, "test", "fixtures", "megaphone.xml")

author = "iHeartRadio & HowStuffWorks"
_copyright = "Copyright 2015 HowStuffWorks"
description = "If you've ever wanted to know about champagne, satanism, the Stonewall Uprising, chaos theory, LSD, El Nino, true crime and Rosa Parks then look no further. Josh and Chuck have you covered."
explicit = "no"
generator = None
language = "en"
link = "[OrderedDict([('@href', 'https://feeds.megaphone.fm/stuffyoushouldknow'), ('@rel', 'self'), ('@type', 'application/rss+xml')]), OrderedDict([('$', 'https://www.howstuffworks.com')])]"
managing_editor = None
new_feed_url = "https://feeds.megaphone.fm/stuffyoushouldknow"
pub_date = None
subtitle = "Stuff You Should Know"
summary = "If you've ever wanted to know about champagne, satanism, the Stonewall Uprising, chaos theory, LSD, El Nino, true crime and Rosa Parks then look no further. Josh and Chuck have you covered."
title = "Stuff You Should Know"
_type = "episodic"
web_master = None
categories = ['Society & Culture']
image_url = "https://static.megaphone.fm/podcasts/1e705dd4-2de6-11e8-b55d-9ba6ddb3f75e/image/uploads_2F1546996139536-0o3pw93d8mk-d5f1143c14a746754c55efb478c66988_2FSKSKLogo-FINAL-iHR-3000x3000.png"
last_build_date = "Sat, 11 May 2019 09:00:00 -0000"
owner = "iHeartRadio & HowStuffWorks"

class TestMegaphone(unittest.TestCase):
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
        self.assertFalse(self.podcast.link == [])
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
