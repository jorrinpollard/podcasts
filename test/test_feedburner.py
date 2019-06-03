#!/usr/bin/env python
from __future__ import division, absolute_import, print_function

import os
import sys
import unittest


cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, cwd)

from podcasts import Podcast

source = os.path.join(cwd, "test", "fixtures", "feedburner.xml")

_copyright = "Copyright 2019 Serial Podcast"
_type = "serial"
author = "This American Life"
categories = ["News & Politics"]
description = "Serial is a podcast from the creators of This American Life, hosted by Sarah Koenig. Serial unfolds one story - a true story - over the course of a whole season. The show follows the plot and characters wherever they lead, through many surprising twists and turns. Sarah won't know what happens at the end of the story until she gets there, not long before you get there with her. Each week she'll bring you the latest chapter, so it's important to listen in, starting with Episode 1. New episodes are released on Thursday mornings."
explicit = None
generator = None
image_url = "https://serialpodcast.org/sites/all/modules/custom/serial/img/serial-itunes-logo.png"
language = "en"
last_build_date = "Thu, 15 Nov 2018 10:30:00 +0000"
managing_editor = None
new_feed_url = None
owner = "rich@thislife.org"
pub_date = None
subtitle = "A podcast from the creators of This American Life"
summary = None
title = "Serial"
web_master = None

class TestFeedburner(unittest.TestCase):
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
