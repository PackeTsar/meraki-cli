---
title: Debugging and Logging
---

If you are having trouble figuring out why something is not working, you can set the debugging level to one of four levels:

- **Level 0** (default): Only warnings and errors will be displayed or logged
- **Level 1** (`-d`): General status and program progress will be reported
- **Level 2** (`-dd`): General program progress as well as Meraki API library debugging will be reported
- **Level 3** (`-ddd`): Program progress, Meraki API library debugging, and full data dumps will be reported

If you want to stow those logs away, you can define a log file using something like `-l logs.txt`.

Only logs printed to the screen will be written to the file, so you also need to set a debugging level if you want to see anything other than just warnings and errors.
