#!/usr/bin/env python
from __future__ import division, absolute_import, print_function

import os
import sys
import unittest


cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, cwd)

from podcasts import Podcast

source = os.path.join(cwd, "test", "fixtures", "art19.xml")

_copyright = None
_type = "episodic"
author = "GaS Digital Network"
categories = ['Sports & Recreation']
description = "<p>For the past two years, UFC middleweight Champion, Michael Bisping, and stand up comedian, Luis J. Gomez, have hosted a show together on satellite radio. Now they bring their brand of brash, comedic MMA commentary to the podcast world! Believe You Me is a weekly show that gives you a behind the scenes look at the career and life of a UFC champion. Bisping along with his co-host, Gomez, break down MMA news, pop culture stories, and talk parenting, philosophy, and life in general. Believe You Me is FOR ADULTS ONLY! Follow us on twitter and Instagram: @BYMPod. The newest 15 episodes are always free, but if you want access to all the archives, listen live, chat live, access to the forums, and get the show before it comes out everywhere else - you can subscribe now at gasdigitalnetwork.com and use the code BYM to save 15% on the entire network.</p>"
explicit = "yes"
generator = "ART19"
image_url = "https://content.production.cdn.art19.com/images/61/e2/04/17/61e20417-ab6f-43c6-a8fb-00d8d845d8e5/d7bea48af84622089cf34d61a6b2bd64691ac4bda05793a4ca463ea0afbb60bc8af9457ea259ebe8d79826bf2e48d510d6fc130edd74e0bb5454fc1ee30baf74.jpeg"
language = "en"
last_build_date = "Tue, 07 May 2019 04:44:41 -0000"
link = "[OrderedDict([('@href', 'https://rss.art19.com/believe-you-me'), ('@rel', 'self'), ('@type', 'application/rss+xml')]), OrderedDict([('$', 'http://GaSDigitalNetwork.com/believe')])]"
managing_editor = "bym@gasdigitalnetwork.com (Michael Bisping, Luis J. Gomez)"
new_feed_url = "https://rss.art19.com/believe-you-me"
owner = "Michael Bisping, Luis J. Gomez"
pub_date = None
subtitle = None
summary = "<p>For the past two years, UFC middleweight Champion, Michael Bisping, and stand up comedian, Luis J. Gomez, have hosted a show together on satellite radio. Now they bring their brand of brash, comedic MMA commentary to the podcast world! Believe You Me is a weekly show that gives you a behind the scenes look at the career and life of a UFC champion. Bisping along with his co-host, Gomez, break down MMA news, pop culture stories, and talk parenting, philosophy, and life in general. Believe You Me is FOR ADULTS ONLY! Follow us on twitter and Instagram: @BYMPod. The newest 15 episodes are always free, but if you want access to all the archives, listen live, chat live, access to the forums, and get the show before it comes out everywhere else - you can subscribe now at gasdigitalnetwork.com and use the code BYM to save 15% on the entire network.</p>"
title = "Believe You Me with Michael Bisping"
web_master = None

class TestArt19(unittest.TestCase):
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
