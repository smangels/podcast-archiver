import xml.etree.ElementTree as etree


def add_feeds_from_feedsfile(self, feedsfile):
    return feedsfile.read().strip().splitlines()


def add_feeds_from_opml(self, opml):
    with opml as file:
        tree = etree.fromstringlist(file)

    return [
        node.get("xmlUrl")
        for node in tree.findall("*/outline/[@type='rss']")
        if node.get("xmlUrl") is not None
    ]
