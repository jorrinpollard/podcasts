#!/usr/bin/env python
from __future__ import division, absolute_import, print_function

import os
import sys
import unittest


cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, cwd)

from podcasts import Podcast

source = os.path.join(cwd, "test", "fixtures", "shoutengine.xml")

_copyright = None
_type = None
author = "Matt Farah & Zack Klapman"
categories = ['Automotive', 'Comedy', 'Games & Hobbies', 'Video Games']
description = "Matt Farah and Zack Klapman sit down with automotive icons, pro drivers, comedians and other friends to discuss automotive industry news, racing, projects and whatever else comes to mind.For video test drives and reviews, go toTheSmokingTire.comorwww.youtube.com/thesmokingtireRentour movie, where we find out if some bad CraigsList cars can cross an entire US State, off-road!www.thesmokingtire.com/film"
explicit = "yes"
generator = "ShoutEngine 1.0; http://www.shoutengine.com"
image_url = "http://media.cdn.shoutengine.com/cache/d6/e9/d6e900686dd88c35c643f0a1747f1912.jpg"
language = "en"
last_build_date = "Sat, 11 May 2019 19:21:22"
link = 'http://shoutengine.com/TheSmokingTire/'
managing_editor = "Matt Farah & Zack Klapman"
new_feed_url = None
owner = "Matt Farah & Zack Klapman"
pub_date = "Fri, 01 Mar 2013 22:12:55 +0000"
subtitle = "Matt Farah and Zack Klapman sit down with automotive icons, pro drivers, comedians and other friends to discuss automotive industry news, racing, projects and whatever else comes to mind.For video test drives and reviews, go toTheSmokingTire.comorwww.youtube.com/thesmokingtireRentour movie, where we find out if some bad CraigsList cars can cross an entire US State, off-road!www.thesmokingtire.com/film"
summary = "Matt Farah and Zack Klapman sit down with automotive icons, pro drivers, comedians and other friends to discuss automotive industry news, racing, projects and whatever else comes to mind.For video test drives and reviews, go toTheSmokingTire.comorwww.youtube.com/thesmokingtireRentour movie, where we find out if some bad CraigsList cars can cross an entire US State, off-road!www.thesmokingtire.com/film"
title = "The Smoking Tire"
web_master = "Matt Farah & Zack Klapman"

class TestShoutengine(unittest.TestCase):
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
