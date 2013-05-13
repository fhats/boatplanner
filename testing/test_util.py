# -*- coding: utf-8 -*-
import datetime
import random
import time

from boatplanner.models.rower import PORT


def make_rower(**kwargs):
	rower = {}
	defaults = {
		'name': random_name(),
		'height': None,
		'weight': None,
		'sweep_side': PORT,
		'sweep_ambi': False,
		'can_scull': False,
		'started_rowing': time.mktime(datetime.datetime.now().timetuple())
	}
	for k, v in defaults.iteritems():
		rower.setdefault(k, v)

	rower.update(kwargs)

	return rower


def random_name():
	first = ''.join([random_char() for _ in xrange(random.randint(5, 13))])
	last = ''.join([random_char() for _ in xrange(random.randint(7, 20))])

	return ' '.join((first, last))


def random_char():
	return chr(random.randint(ord('a'), ord('z')))
