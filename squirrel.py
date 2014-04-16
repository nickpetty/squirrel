#!/usr/bin/env python
import markdown2
import os
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("-m", dest='markdown', help="Markdown file to be converted to html.")
parser.add_argument("-t", dest='template', help="Template to be used for formatting of markdown file.")
#parser.add_argument("-u", required=False, action='store_true')
args = parser.parse_args()

def convert():
	markdownInput = open(args.markdown).read() # Read markdown file into markdownInput
	title = markdownInput.split('\n')[:1] # Take the first line and make it the <title>
	block = markdownInput.split('\n')[2:] # Strip the title out of the entry
	block = '\n'.join(block)

	markdownHTML = markdown2.markdown(block) # Convert markdown to HTML
	template = open('templates/' + args.template).read() # Load template specified by -t flag

	htmlOutput = ''
	for line in template:
		htmlOutput += line # Turns converted read template html to a multi line string, helps for regex subs

	htmlOutput = re.sub("{{title}}", str(title[0]), htmlOutput) # Sets <title> if not index

	htmlOutput = re.sub("{{block}}", markdownHTML, htmlOutput) # Insert converted markdown to location of {{block}} in template
	try:
		open('webserver/' + args.markdown.strip(".md") + ".html", "w").write(htmlOutput) # Create html and write it
		print "Generated %s" % (args.markdown.strip('.md') + '.html')
	except IOError:
		print """Path could not be found.  Please make sure the folder hierarchy matches in 
the local 'webserver' folder, and that the 'webserver' folder exists."""
	

if args.markdown:
	if os.path.isfile(str(args.markdown)):
		convert()
	else:
		print "File " + args.markdown + " could not be found."