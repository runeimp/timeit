#!/usr/bin/env python3
"""
TimeIt will run a command with the time utility and for so many loops and give the average with and without the max and min values removed.

@author RuneImp <runeimp@gmail.com>
@licence MIT
@see https://betterexplained.com/articles/how-to-analyze-data-using-the-average/


ChangeLog
---------
2017-01-22  1.0.0      Initial creation

average
average distribution
Central Limit Theorem
mean
standard deviation
Gaussian distribution
outliers
"""

# __all__ = []
__version__ = '1.0.0'
__author__ = 'RuneImp <runeimp@gmail.com>'

import argparse
import os
import re
from subprocess import PIPE, run
import sys


APP_NAME = 'TimeIt'
CLI_NAME = 'timeit'


parser = argparse.ArgumentParser(add_help=False, description='TimeIt: the time looper!', prefix_chars="-/", prog=APP_NAME)
parser.add_argument('commands', nargs='+', help='Commands to run')
# parser.add_argument('-n', '--dry-run', action='store_true', help="Do a dry run. In otherwords don't actually rename files.")
# parser.add_argument('--debug', action='store_true', help='Debug processing and dry run')
parser.add_argument('-h', '--help', '/help', action='help', help='Show this help message and exit')
parser.add_argument('-l', '--loop', '/loop', default=5, help='Number of loops to run')
parser.add_argument('-t', '--trim', '/trim', action='store_true', help='Remove the lowest and highest results before averaging')
parser.add_argument('-v', '--version', '/ver', action='version', help="Show program's version number and exit", version='%(prog)s {}'.format(__version__))
args = parser.parse_args()

results = []
time_re = re.compile('([a-z]+)\s([0-9]+)m([0-9]+\.[0-9]+)s')


if args.loop < 3:
	if args.trim:
		print("ERROR: -l and --loops expect a minimum value of 3 when trim is 'true'.")
	elif args.loop < 1:
		print("ERROR: -l and --loops expect a minimum value of 1 when trim is 'false'.")
	exit(1)

divisor = args.loop
if args.trim == 'true':
	divisor -= 2


def mands(datum):
	"""Combines minutes and seconds into seconds total"""
	result = datum['s']
	if datum['m'] > 0:
		result += datum['m'] * 60

	return result


if args.commands:
	for cmd in args.commands:
		cmd_str = 'time ' + cmd
		i = 0
		while i < args.loop:
			# print(cmd_str)
			result = run(cmd_str, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
			# CompletedProcess .args .returncode .stdout .stderr
			output = result.stderr
			match = time_re.findall(output)
			# print("match: {}".format(match))
			datum = {
				'real': {'m': int(match[0][1]), 's': float(match[0][2])},
				'user': {'m': int(match[1][1]), 's': float(match[1][2])},
				'sys': {'m': int(match[2][1]), 's': float(match[2][2])},
			}
			# print("datum: {}".format(datum))

			exit_code = result.returncode
			if exit_code == 0:
				results.append(datum)
			else:
				print('BREAK: exit_code: {}'.format(exit_code))
				break
			i += 1

		real_max = None
		real_min = None
		real_tmp = 0
		real_total = 0
		syst_max = None
		syst_min = None
		syst_tmp = 0
		syst_total = 0
		user_max = None
		user_min = None
		user_tmp = 0
		user_total = 0
		for datum in results:
			# print("-- {}".format(datum))
			real_tmp = mands(datum['real'])
			if real_max == None:
				real_max = real_tmp
			elif real_max < real_tmp:
				real_max = real_tmp
			if real_min == None:
				real_min = real_tmp
			elif real_min > real_tmp:
				real_min = real_tmp
			real_total += real_tmp

			# print("real_total: {:.5f} | real_max: {:.5f} | real_min: {:.5f} | real_tmp: {:.5f}".format(real_total, real_max, real_min, real_tmp))

			user_tmp = mands(datum['user'])
			if user_max == None:
				user_max = user_tmp
			elif user_max < user_tmp:
				user_max = user_tmp
			if user_min == None:
				user_min = user_tmp
			elif user_min > user_tmp:
				user_min = user_tmp
			user_total += user_tmp

			# print("user_total: {:.5f} | user_max: {:.5f} | user_min: {:.5f} | user_tmp: {:.5f}".format(user_total, user_max, user_min, user_tmp))

			syst_tmp = mands(datum['user'])
			if syst_max == None:
				syst_max = syst_tmp
			elif syst_max < syst_tmp:
				syst_max = syst_tmp
			if syst_min == None:
				syst_min = syst_tmp
			elif syst_min > syst_tmp:
				syst_min = syst_tmp
			syst_total += syst_tmp

			# print("syst_total: {:.5f} | syst_max: {:.5f} | syst_min: {:.5f} | syst_tmp: {:.5f}\n".format(syst_total, syst_max, syst_min, syst_tmp))

		if args.trim:
			real_total -= real_max
			real_total -= real_min
			user_total -= user_max
			user_total -= user_min
			syst_total -= syst_max
			syst_total -= syst_min

		real_total = real_total / divisor
		user_total = user_total / divisor
		syst_total = syst_total / divisor

		print("\n{}".format(cmd_str))
		# print("  real_total: {:.5f} | user_total: {:.5f} | syst_total: {:.5f}".format(real_total, user_total, syst_total))
		print("   real:  |  user:  |  sys:")
		print("  {:.5f} | {:.5f} | {:.5f}".format(real_total, user_total, syst_total))
	print()
