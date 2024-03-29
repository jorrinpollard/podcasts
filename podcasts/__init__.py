from __future__ import division, absolute_import, print_function
from collections import OrderedDict
from xml.etree.ElementTree import fromstring
from xmljson import badgerfish as bf
import os
import xml.etree.ElementTree as ET

from podcasts.log import logger
from podcasts.lib import get_clean_podcast_attr

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
        self.author =  get_clean_podcast_attr(channel.get("author", {}).get("$"))
        self.copyright =  get_clean_podcast_attr(channel.get("copyright", {}).get("$"))
        self.description =  get_clean_podcast_attr(channel.get("description", {}).get("$"))
        self.explicit =  get_clean_podcast_attr(channel.get("explicit", {}).get("$"))
        self.generator =  get_clean_podcast_attr(channel.get("generator", {}).get("$"))
        self.language =  get_clean_podcast_attr(channel.get("language", {}).get("$"))
        self.managing_editor =  get_clean_podcast_attr(channel.get("managingEditor", {}).get("$"))
        self.new_feed_url =  get_clean_podcast_attr(channel.get("new-feed-url", {}).get("$"))
        self.pub_date =  get_clean_podcast_attr(channel.get("pubDate", {}).get("$"))
        self.subtitle =  get_clean_podcast_attr(channel.get("subtitle", {}).get("$"))
        self.summary =  get_clean_podcast_attr(channel.get("summary", {}).get("$"))
        self.title =  get_clean_podcast_attr(channel.get("title", {}).get("$"))
        self.type =  get_clean_podcast_attr(channel.get("type", {}).get("$"))
        self.web_master =  get_clean_podcast_attr(channel.get("webMaster", {}).get("$"))

    def __str__(self):
        return self.source

    @property
    def link(self):
        channel = self.channel
        channel_links = channel.get("link")

        link = None

        if channel_links and isinstance(channel_links, OrderedDict):
            channel_links = [channel_links]

        for channel_link in channel_links:
            if channel_link.get("$"):
                link = channel_link.get("$")
                break

        link = get_clean_podcast_attr(link)
        logger.debug("Link: " + link)
        return link

    @property
    def owner(self):
        channel = self.channel
        channel_owner = channel.get("owner")

        owner = None

        if channel_owner and isinstance(channel_owner, OrderedDict):
            owner_value = channel_owner.get("$")

            if owner_value and isinstance(owner_value, str):
                owner = owner_value

        if not owner and channel_owner.get("name"):
            owner = channel_owner.get("name", {}).get("$")

        if not owner and channel_owner.get("email"):
            owner = channel_owner.get("email", {}).get("$")

        owner = get_clean_podcast_attr(owner)

        logger.debug("Onwer: " + owner)
        return owner

    @property
    def image_url(self):
        """Finds and return the feed's image URL"""

        channel = self.channel
        
        channel_images = channel.get("image")

        image_url = None

        # get itunes image if it exists
        itunes_image = "{http://www.itunes.com/dtds/podcast-1.0.dtd}image"
        if channel.get(itunes_image):
            logger.debug("Using feed's iTunes image for image_url")
            image_url = channel.get(itunes_image).get("@href")

        # put channel_images into a list if there's only one
        if channel_images and isinstance(channel_images, OrderedDict):
            channel_images = [channel_images]

        # get channel image if they exists
        for channel_image in channel_images:
            if not image_url and channel_image.get("url"):
                image_url = channel_image.get("url").get("$")

            if not image_url and channel_image.get("@href"):
                image_url = channel_image.get("@href")

        image_url = get_clean_podcast_attr(image_url)
        logger.debug("Image URL: " + image_url)
        return image_url

    @property
    def last_build_date(self):
        """Returns the feed's lastBuildDate if it exists, otherwise return the first episode's pubDate"""

        channel = self.channel
        last_build_date = None

        if channel.get("lastBuildDate"):
            logger.debug("Using feed's lastBuildDate")
            last_build_date = get_clean_podcast_attr(channel.get("lastBuildDate", {}).get("$"))

            

        items = channel.get("item")
        latest_item = items[0]
        if not last_build_date and latest_item and latest_item.get("pubDate"):
            logger.debug("Using latest episode's pubDate")
            last_build_date =  get_clean_podcast_attr(latest_item.get("pubDate", {}).get("$"))

        last_build_date = get_clean_podcast_attr(last_build_date)
        logger.debug("Last build date: " + last_build_date)
        return last_build_date

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
        categories = list(map(get_clean_podcast_attr, categories))
        categories.sort()

        logger.debug("Categories found: " + str(categories))

        return categories
