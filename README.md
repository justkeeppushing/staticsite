# My site generator

### This is a mockup readme with a few ideas on how i can proliferate this. it's not necessarily accurate.

## Usage
Plug in your sites to items.json using schema example. The URLS must contain protocol. Any followable URL.

Title will be the label so name it how you want to see it. what goes in, comes out.

Gif backgrounds will be selected from gif/title.gif using title value. You must name them as such otherwise default style will be used. Gif backgrounds are only going to show on desktop on Hover, or for a short time on click for mobile.

You will need to provide your own favicon.ico in includes directory. Otherwise, none will be used.

You will need to provide your own style.css in the includes directory. Otherwise, none will be used.

In the future i may make a prompt that allows for custom title element, as a higher level json object in the same items.json file.
for now it's just mine so it doesn't really matter.

no extra error checking right now either. 
Running generate-site.py on its own just goes to STOUT. 

## Running
Have your script runner deploy run.sh, which is a one liner (tees to a file from generate-site.py)

It generates index.html which you need to choose as your output (default for github pages i believe).
For github pages, that should be all it needs, this is using python 3 list comprehension so it may need 3 or higher.

Ideally, you could make a branch per website and if i implement the changes above, you'd only need to provide the items.json file (maybe i could add additional meta/env vars/etc, but it's ok for now).
