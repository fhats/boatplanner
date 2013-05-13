from flask import Flask
app = Flask(__name__)

import boatplanner.views.lineup
import boatplanner.views.management
