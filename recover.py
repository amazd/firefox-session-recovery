#!/usr/bin/env python
import lz4.block as lz4
import json
import sys

def extract_urls(last_tab):
    print(f"<ul>")
    if('entries' in last_tab and len(last_tab['entries']) >= 1):
        if (last_tab['entries'][0]['url'] == 'about:sessionrestore'):
            older_session_data = last_tab['formdata']['id']['sessionData']
            extract_windows(older_session_data)
        else:
            for i in range(len(last_tab['entries'])):
                url = last_tab['entries'][i]['url']
                print(f"<li><a href='" + url + "'>" + url + "</a></li>")
    print("</ul>")

def extract_windows(session):
    for i in range(len(session['windows'])):
        windows = session['windows'][i]
        print("<h2>tabs in windows</h2> </br>")
        for j in range(len(windows['tabs'])):
            tab = windows['tabs'][j]
            extract_urls(tab)

    for k in range(len(session['_closedWindows'])):
        close_windows = session['_closedWindows'][k]
        print("<h2>tabs in closed windows</h2><BR>")
        for q in range(len(close_windows['tabs'])):
            tab = close_windows['tabs'][q]
            extract_urls(tab)

path = sys.argv[1]
with open(path, 'rb') as f:
    assert f.read(8) == b'mozLz40\0'
    recovery_session_data=json.loads(lz4.decompress(f.read()))

extract_windows(recovery_session_data)
