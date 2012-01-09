#!/usr/bin/python
import ifcb
import cgi
import cgitb
import os.path
import re
from config import DATA_TTL
import sys
from zipfile import ZipFile
from ifcb.io.blob_unzip import pid2blobpng

"""RESTful service resolving an IFCB permanent ID (pid) + format parameter to an appropriate representation"""

if __name__ == '__main__':
    cgitb.enable()
    out = sys.stdout
    pid = cgi.FieldStorage().getvalue('pid')
    format = 'png'
    if re.search(r'\.[a-z]+$',pid): # does the pid have an extension?
        (pid, ext) = os.path.splitext(pid)
        #format = re.sub(r'^\.','',ext) # the extension minus the "." is the "format"
    #format = cgi.FieldStorage().getvalue('format',format) # specified format overrides
    mime_type = 'image/png'
    headers = ['Content-type: %s' % mime_type,
               'Cache-control: max-age=%d' % DATA_TTL,
               '']
    png = pid2blobpng(pid)
    for h in headers:
        print h
    sys.stdout.write(png)
    sys.stdout.flush()
    
