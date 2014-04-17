#!/usr/bin/env python
import os
import argparse
import re
import datetime
import gfm

parser = argparse.ArgumentParser()
parser.add_argument("-m", dest='markdown', help="Markdown file to be converted to html.")
parser.add_argument("-t", dest='template', required=False, help="Template to be used for formatting of markdown file.")
#parser.add_argument("-d", required=False, action='store_true')
args = parser.parse_args()

def convert():
	markdownInput = open(args.markdown).read() # Read markdown file into markdownInput

	title = markdownInput.split('\n')[:2] # Take the first line and make it the <title>
	block = markdownInput.split('\n')[2:] # Strip the title out of the entry
	block = '\n'.join(block)

	markdownHTML = gfm.markdown(block.decode('utf8')) # Convert markdown to HTML

	if args.template:
		title = str(title[0]) 
		template = open('templates/' + args.template).read() # Load template specified by -t flag
	else:
		title = str(title[0]) + '\n' + str(title[1])
		title = gfm.markdown(title)
		template = "{{title}}\n{{block}}"

	htmlOutput = ''
	for line in template:
		htmlOutput += line # Turns converted read template html to a multi line string, helps for regex subs

	htmlOutput = re.sub("{{title}}", title, htmlOutput) # Sets <title> if not index
	htmlOutput = re.sub("{{datetime}}", datetime.datetime.now().ctime(), htmlOutput) # Insert date and time i.e., Wed Apr 16 17:18:56 2014	
	htmlOutput = re.sub("{{block}}", markdownHTML, htmlOutput) # Insert converted markdown to location of {{block}} in template

	try:
		if not os.path.exists('webserver'): # Check foe existence of webserver folder
			os.mkdir('webserver')

		htmlPath = args.markdown.strip(".md").replace(' ', '-') + '/'
		if not os.path.exists('webserver/' + htmlPath): # Check for existence of child folder
			os.mkdir('webserver/' + htmlPath)

		open('webserver/' + htmlPath + "/index.html", "w").write(htmlOutput.encode('ascii', 'ignore')) # Create html and write it
		print "Generated %s" % (args.markdown.strip('.md'))
	except IOError:
		print """Path could not be found.  Please make sure the folder hierarchy matches in 
the local 'webserver' folder, and that the 'webserver' folder exists."""
	
if args.markdown:
	if os.path.isfile(str(args.markdown)):
		convert()
	else:
		print "File " + args.markdown + " could not be found."
else:
	print parser.parse_args(['-h'])