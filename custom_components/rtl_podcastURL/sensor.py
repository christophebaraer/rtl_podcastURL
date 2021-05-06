"""This component provides sensors for RTL Podcast URL."""
import requests
from bs4 import BeautifulSoup

from homeassistant.helpers.entity import Entity

from .const import (
    PODCAST_URL,
)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    add_entities([rtl_PodcastSensor()])


class rtl_PodcastSensor(Entity):
    """Representation of a RTL Podcast URL sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'RTL podcast URL'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor."""
        url=PODCAST_URL
        soup = BeautifulSoup(requests.get(url).content, 'xml')

        items = soup.find_all('item')
        podcastURL = ""
        i = 0

        while i < len(items):
            # Only takes into account the very long episodes (which are the full
            # shows) amoung the last 20 episodes. This should filter out all 
            # the short one such as Fake News, Pepites, Le Livre du Jour, Invité
            # Mystère, etc and break the loop after the first long episode
            # has been found
            if int(items[i].enclosure['length']) > 100000000 : 
                podcastURL = items[i].enclosure['url']
                break

            i += 1

        self._state = podcastURL
