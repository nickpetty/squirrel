Squirrel
=====================

Requirements
------------

- python **2.7**
- markdown2 *pip install markdown2*

About
-----

+ Everything written in markdown.  Including index.
+ Hierarchy matches that of webserver, but in MD instead of html 
+ HTML styling can still be applied in MD through use of CSS or div tags (note that MD syntax is not interpreted in html blocks)

All converted MD to HTML files will be placed in the same hierarchy in a folder named '*webserver*' for simple deployment.

**NOTE**: Any dependencies will need to be manually copied to their respected folders in the 'webserver' folder. i.e., pictures/videos

**ANOTHER NOTE**: All necessary folders must be created before running Squirrel.  Including 'webserver'.

Commands
---------

Use of flags for specifications.

	squirrel -t <template> -m <markdown file>

*Run in root of working dir* - Doing so will pass in the directory of the file and will save in the same location in the *webserver* folder.

Optional commands (In Development)
-----------------

	chainsaw ... -d 

This will deploy to a git repo specified in a config file.
