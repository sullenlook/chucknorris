#!/usr/bin/python
# -*- coding: utf-8 -*-
#by SullenLook <sullenlook@sullenlook.eu>

import re
import urllib2, urllib, uuid
import json
from urllib2 import urlopen
from xml.dom import minidom

from plugin import *

#Insert your API key from http://chuck-norris-witze.de in the URL below
APPID = 85031401("chucknorris")

class cnjoke(Plugin):

        @register("de-DE", ".*Chuck Norris*.")
        def cn_joke(self, speech, language):
                chuckurl = 'http://chuck-norris-witze.de/api.php?key=%s&o=1' % (APPID)
                joke = urllib.urlopen(chuckurl)
                store = joke.read()
                query = store.replace('Chuck','tschack').replace('&quot;','').replace('roundhouse','raundhaus')
                store = store.replace('&quot;','\"')
                self.say(store,query)
                self.complete_request()
# EOF