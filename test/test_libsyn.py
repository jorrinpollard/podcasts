#!/usr/bin/env python
from __future__ import division, absolute_import, print_function

import os
import sys
import unittest


cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, cwd)

from podcasts import Podcast

source = os.path.join(cwd, "test", "fixtures", "libsyn.xml")

_copyright = "Copyright © Talking Monkey Productions"
_type = "episodic"
author = "Joe Rogan"
categories = ['Comedy', 'Society & Culture', 'Technology']
description = "Conduit to the Gaian Mind"
explicit = "yes"
generator = "Libsyn WebEngine 2.0"
image_url = "http://static.libsyn.com/p/assets/7/1/f/3/71f3014e14ef2722/JREiTunesImage2.jpg"
language = "en"
last_build_date = "Fri, 10 May 2019 02:04:10 +0000"
link = "[OrderedDict([('@href', 'http://joeroganexp.joerogan.libsynpro.com/rss'), ('@rel', 'self'), ('@type', 'application/rss+xml')]), OrderedDict([('$', 'https://www.joerogan.com')])]"
managing_editor = "joe@joerogan.net (joe@joerogan.net)"
new_feed_url = "http://joeroganexp.joerogan.libsynpro.com/rss"
owner = "Joe Rogan"
pub_date = "Fri, 10 May 2019 02:00:00 +0000"
subtitle = "Joe Rogan's Weekly Podcast"
summary = "The podcast of Comedian Joe Rogan.."
title = "The Joe Rogan Experience"
web_master = None

class TestLibsyn(unittest.TestCase):
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
