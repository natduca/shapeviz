#!/usr/bin/env python2.7
import os
import sys
import argparse

def ReadTemplate():
	template_filename = os.path.join(os.path.dirname(__file__), "shapeviz_template.html")
	with open(template_filename, 'r') as f:
		return f.read()

def Main(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument('files', nargs='+')
	args = parser.parse_args(argv[1:])
	template = ReadTemplate()
	for filename in args.files:
		with open(filename, 'r') as infile:
			data = infile.read()
		out_html = template.replace('%%SHAPEDATA%%', data)
		dstfile = os.path.splitext(filename)[0] + '.html'
		with open(dstfile, 'w') as f:
			f.write(out_html)


if __name__ == "__main__":
	sys.exit(Main(sys.argv))