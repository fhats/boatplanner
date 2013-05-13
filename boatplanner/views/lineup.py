# -*- coding: utf-8 -*-
from flask import render_template

from boatplanner import app


@app.route("/lineup", methods=["GET"])
def lineup():
    """Shows the page that does the heavy lifting of lineup creation."""
    return render_template("lineup.html")


@app.route("/lineup/generate", methods=["POST"])
def generate_lineups():
    """Given a set of rowers, generate a set of proposed lineups."""
    pass
