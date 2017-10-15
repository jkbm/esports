import requests
import urllib.request
from datetime import datetime
import time
from bs4 import BeautifulSoup
from .models import Match, Tournament, Player, Game, Group, Deck, Deckset
from django.db.models import Q
from django.core.files import File 
import json
import re
from xml.etree import ElementTree

