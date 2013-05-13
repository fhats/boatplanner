# -*- coding: utf-8 -*-

# TODO: Fix this and the below inversion to deal with the fact that 2x has
# the same number of rowers as a 2+. This is a convenient way to get
# len(SIZES_TO_BOAT) == len(BOAT_SIZES), but is not an accurate representation
# of the world.
BOAT_SIZES = {
	'8+': 9,
	'4+': 5,
	'4x': 4,
	'2x': 2,
	'1x': 1,
}

SIZES_TO_BOAT = dict((v, k) for k, v in BOAT_SIZES.iteritems())
