# -*- coding: utf-8 -*-
"""Contains a public interface to interact with rowers in a data store, as well
as a implementations of a rower in each data store.

Each public function returns a rower as a dictionary or rowers as a list of
dictionaries.
"""

PORT = 0
STARBOARD = 1


def list_rowers():
	"""Get a list of rowers that are available."""
	pass


def get_rower_info(id):
	"""Get a information for a rower with specific ID."""
	pass


def set_rower_info(id, **info):
	"""Set information for a rower with the given ID."""
	pass


def add_rower(**info):
	"""Add a rower to the data store."""
	pass


def remove_rower(id):
	"""Remove rower with the given ID."""
	pass
