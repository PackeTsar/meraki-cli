---
title: How Pipelining Works
---

The pipelining feature of Meraki-CLI works by writing standard JSON data out to STDIN; the same data you see if you use the `-j` switch.

All log messages are written to STDERR to prevent interference.

When the program starts, it checks for a leading pipe (ie: `| meraki ...`): the existence of which would indicate that it needs to process STDIN data, which it then does.

When the program processes results to be printed to the screen, it checks for a trailing pipe (ie: `meraki ... |`): the existence of which would indicate that its output will feed another program instance. When this trailing pipe is detected it automatically switches to JSON output and writes it to STDOUT.
