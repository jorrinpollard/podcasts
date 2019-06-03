from __future__ import division, absolute_import, print_function
from collections import OrderedDict
from xml.etree.ElementTree import fromstring
from xmljson import badgerfish as bf
import os
import xml.etree.ElementTree as ET

from podcasts.log import logger

class Podcast:
    def __init__(self, source):
        """Initializes a Podcast instance based on XML data from a string or file path"""

        logger.debug("Initializing podcast from source: " + source)

        if os.path.isfile(source):
            tree = ET.parse(source)
            root = tree.getroot()
            data = bf.data(root)
        else:
            data = bf.data(fromstring(source))

        channel = data.get("rss").get("channel")

        self.source = source
        self.channel = channel
        self.author = channel.get("author", {}).get("$")
        self.copyright = channel.get("copyright", {}).get("$")
        self.description = channel.get("description", {}).get("$")
        self.explicit = channel.get("explicit", {}).get("$")
        self.generator = channel.get("generator", {}).get("$")
        self.language = channel.get("language", {}).get("$")
        self.link = channel.get("link")
        self.managing_editor = channel.get("managingEditor", {}).get("$")
        self.new_feed_url = channel.get("new-feed-url", {}).get("$")
        self.pub_date = channel.get("pubDate", {}).get("$")
        self.subtitle = channel.get("subtitle", {}).get("$")
        self.summary = channel.get("summary", {}).get("$")
        self.title = channel.get("title", {}).get("$")
        self.type = channel.get("type", {}).get("$")
        self.web_master = channel.get("webMaster", {}).get("$")

    def __str__(self):
        return self.source

    @property
    def owner(self):
        channel = self.channel
        owner = channel.get("owner")
        if not owner:
            return

        if owner.get("$"):
            return owner.get("$")

        if owner.get("name"):
            return owner.get("name").get("$")

        return owner

    @property
    def image_url(self):
        """Finds and return the feed's image URL"""

        channel = self.channel
        
        channel_images = channel.get("image")

        # get itunes image if it exists
        itunes_image = "{http://www.itunes.com/dtds/podcast-1.0.dtd}image"
        if channel.get(itunes_image):
            logger.debug("Using feed's iTunes image for image_url")

            return channel.get(itunes_image).get("@href")

        # put channel_images into a list if there's only one
        if channel_images and type(channel_images) is OrderedDict:
            channel_images = [channel_images]

        # get channel image if they exists
        for channel_image in channel_images:
            if channel_image.get("url"):
                return channel_image.get("url").get("$")

            if channel_image.get("@href"):
                return channel_image.get("@href")

    @property
    def last_build_date(self):
        """Returns the feed's lastBuildDate if it exists, otherwise return the first episode's pubDate"""

        channel = self.channel

        if channel.get("lastBuildDate"):
            logger.debug("Using feed's lastBuildDate for last_build_date")

            return channel.get("lastBuildDate", {}).get("$")

        items = channel.get("item")
        latest_item = items[0]
        if latest_item and latest_item.get("pubDate"):
            logger.debug("Using latest episode's pubDate for last_build_date")

            return latest_item.get("pubDate", {}).get("$")

    @property
    def categories(self):
        """Returns a list of the feed's categories"""

        channel = self.channel

        categories = []

        categories = channel.get("category")
        if not categories:
            logger.warning("Channel has no categories")
            return

        if categories and isinstance(categories, OrderedDict):
            categories = [categories]

        for category in categories:
            logger.debug("Parsing category: " + str(category))

            if isinstance(category, str):
                categories = categories + [category]

            if isinstance(category, OrderedDict):
                categories = categories + [category.get("@text"), category.get("$")]

                if category.get("category"):
                    for inner_category in category.get("category"):
                        if isinstance(inner_category, str):
                            categories = categories + [inner_category]

                        if isinstance(inner_category, OrderedDict):
                            categories = categories + [inner_category.get("@text"), inner_category.get("$")]
        
        categories[:] = [category for category in categories if isinstance(category, str) and category != "@text"]
        categories = list(set(categories))
        categories.sort()

        logger.debug("Categories found: " + str(categories))

        return categories
