#!/bin/sh

logparser -ss http://127.0.0.1:6800 -dir /etc/scrapyd/logs > logparser.log 2>&1 &
scrapyd --pidfile= > scrapyd.log 2>&1