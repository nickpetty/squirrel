Squirrel
========
[![Creative Commons License][1]][2]

Requirements
------------

- python **2.7**
- ~~markdown2 *pip install markdown2*~~
- gfm ([GitHub Flavored Markdown][3]) *pip install gfm*

About
-----

+ Everything written in markdown.  Including index.
+ Hierarchy matches that of webserver, but in MD instead of html 
+ HTML styling can still be applied in MD through use of CSS or div tags (note that MD syntax is not interpreted in html blocks)
+ First two lines of Markdown file is reserved for title and will be stripped from the block.  This is to make the MD readable, and to populate the {{title}} variable in the template if included.

All converted MD to HTML files will be placed in the same hierarchy in a folder named '*webserver*'(generated automatically) for simple deployment.

**NOTE**: Any dependencies will need to be manually copied to their respected folders in the 'webserver' folder. i.e., pictures/videos

**ANOTHER NOTE**: All necessary folders must be created before running Squirrel. 

Folder Hierarchy
----------------

**Example:**

	+ blog
	|
	|-+ templates
	|  |
	|  |- index.html
	|  |- post.html
	|
	|-+ posts
	|  |
	|  |- How I Learned RegEx In One Week.md
	|
	|-+ webserver
	|  |
	|  |- index.html
	|  |- style.css
	|  |- posts
	|    |
	|    + How-I-Learned-RegEx-In-One-Week
	|       |
	|       |-index.html
	|
	|-- index.md

As you see here, the converted post is placed into a folder of the name of the MD file.  This helps keep clean URLs.  This folder is genereated automatically.  However, the 'posts' folder it is in, is not.  If it could not find the 'posts' folder, an error would be returned.  You must duplicate the folder hierarchy in the 'webserver' folder.

Also, be sure to correctly address your style.css in the templates to reflect the root of what would be your webserver.

Templates
---------

Templates are optional.  If no template is specified, the MD is simply converted to html and saved.

Templates can include the following variables. 

Where the main entry (everything but the first two lines of the MD file) will go:

	{{block}}

Pulled from the first two lines of the MD file to populate the 'title' tag or any area you only want the title of the entry to be (i.e., top of page):

	{{title}}

Insert date and time:

	{{datetime}}

*Two example templates are included.  If you do not have a title for the Markdown file, two blank lines will suffice.*

Usage
-----

Use of flags for specifications.

	squirrel -t <template> -m <markdown file>
	squirrel -t index.html -m README.md

*Run in root of working dir* - Doing so will pass in the directory of the file and will save in the same location in the *webserver* folder.

Optional usage flags (In Development)
-------------------------------------

	squirrel ... -d 

This will deploy to a git repo specified in a config file.

[1]: http://i.creativecommons.org/l/by-sa/4.0/80x15.png
[2]: http://creativecommons.org/licenses/by-sa/4.0/
[3]: https://help.github.com/articles/github-flavored-markdown