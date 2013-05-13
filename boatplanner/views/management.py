# -*- coding: utf-8 -*-
from flask import render_template

from boatplanner import app


@app.route("/crew")
def crew_management():
    """Displays a management page for viewing and changing stuff about the
    available rowers.
    """
    return render_template("crew_management.html")
