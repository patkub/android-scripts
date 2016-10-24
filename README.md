AdBlock
=======
Concatenates hosts from list of sources.  
Generate hosts file:
```
usage: hosts_concat.py [-h] [-o [OUTPUT]] source
```
Mount system partition in recovery and run:
```
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

Parse list of sources from sources.txt, ignore ones listed in ignore.txt, and write to "hosts" file
```
python hosts_concat.py source.txt -i ignore.txt
```

Parse list of sources from sources.txt, and list of hosts from "hosts" file
```
python hosts_concat.py source.txt -e hosts
```
