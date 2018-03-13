import os
import sys
import argparse
import subprocess

def ReadAndVulcanizeTemplate():
  template_filename = os.path.join(os.path.dirname(__file__), "shapeviz_template.html")

  p = subprocess.Popen(['vulcanize', template_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  (stdout, stderr) = p.communicate()
  if p.wait() != 0:
    raise Exception(stderr)
  return stdout


def Main(argv):
  parser = argparse.ArgumentParser()
  parser.add_argument('files', nargs='+')
  args = parser.parse_args(argv[1:])
  template = ReadAndVulcanizeTemplate()
  for filename in args.files:
    with open(filename, 'r') as infile:
      data = infile.read()
    out_html = template.replace('%%SHAPEDATA%%', data)
    dstfile = os.path.splitext(filename)[0] + '.html'
    with open(dstfile, 'w') as f:
      f.write(out_html)
