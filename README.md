AdBlock
=======
Concatenates hosts from list of sources. 
Generate hosts file:
```bash
usage: hosts_concat.py [-h] [-o [OUTPUT]] source
```
Mount system partition in recovery and run:
```bash
flash_hosts
```

Examples
========
Parse list of sources from sources.txt and write to "hosts" file
```
python hosts_concat.py sources.txt
```

Parse list of sources from sources.txt and write to "myhosts.txt" file
```
python hosts_concat.py source.txt -o myhosts.txt
```
