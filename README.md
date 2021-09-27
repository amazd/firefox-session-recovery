### Background
I’m what's known as a tab hoarder. At any given time I might have 100s of tabs open across multipe Firefox windows. 
I know some folks love to hate on firefox, but as one of the only mainstream browsers that is not controlled by a big (evil) tech corp with various privacy/monopolistic concerns, it's my default browser. It is a tad slower than some of the other browsers overall, but it makes it up with the 
[amazing](https://addons.mozilla.org/en-US/firefox/addon/tree-style-tab/) [extensions](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/) and great developer experince.

I also love Firefox for allowing me to keep all my tabs running and backed-up. Even if Firefox crashes, it always recovers nicely, restoring all the tabs that were open when the browser crashed. And this feature (i.e. managing crashed sessions/tabs) which chrome eventually copied (even though it's still not implmented as well as ff) has been my bread and butter and why I've stuck with Firefox all these years.

### The Problem
Having said all that, once in a while (and I used to really dread those moments when it happened), firefox would not be able to resore my crashed session (which might have involed 1000s of tabs that I kept opened, hoping to bookmark at some point). I could never figure out why and eventually there was nothing firefox could do. This led many online to create their own tools to try and extract all those lost tabs (urls) manually. 

Once such popular tool is the [Session History Scrounger](https://www.jeffersonscher.com/ffu/scrounger.html)
which was written in js and runs in browser. It has a great interface but it is slow and has mostly crashed in my use cases (my compressed session files can sometimes be 100mb). As per the tool: "Firefox creates various session history files as you browse, and then at shutdown creates sessionstore.jsonlz4. In Firefox 56+, the files are compressed using Mozilla's flavor of LZ4 compression (.jsonlz4 or .baklz4 file extension). The JSON data contained in those compressed files contain a rich detail about your session" which can be used to extract the urls. 

### Solution

Given that this js implemntion didn't work in my situtration, I needed to come up with a solution which didn't crash if I needed to extract the urls from massive json file. Enter python and the rest is a simple script (developed through trial and error) which extracts all urls from the open tabs.

#### Usage

You can find the recovery files in the sessionstore-backups folder in the Firefox profile dir:

`$FIREFOX_PROFILE/sessionstore-backups/recovery.jsonlz4`

This script will work with either `recovery.jsonlz4` or `recovery.baklz4`

Then just pass the file path to the python script and it will output a html file with all the tabs urls

`$ ./recover.py recovery.jsonlz4 > done.html`

In case you run into this error: 

`ModuleNotFoundError: No module named 'lz4` 

Just run

`pip install lz4`



