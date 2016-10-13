"""
Hosts Concat
Concatenate multiple host files.

author: Patrick Kubiak
"""

from sys import stdout
import datetime
import argparse
import urllib
from urllib.request import Request, urlopen


def main():
    # store data
    hosts, sources, ignore_list = [], [], []

    # command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=str, help='file containing list of sources to parse')
    parser.add_argument('-o', '--output', type=str, nargs='?', default="hosts", help='write output hosts to file')
    parser.add_argument('-i', '--ignore', type=str, nargs='?', default="ignore.txt",
                        help='file containing list of hosts to ignore')
    args = parser.parse_args()

    # read ignore file
    stdout.write("Reading " + args.ignore + "...\n")
    with open(args.ignore, 'r') as f:
        for source in f:
            stdout.write("  Ignoring " + source + "...\n")
            ignore_list.append(source)

    # read sources
    stdout.write("Reading " + args.source + "...\n")
    stdout.write("Parsing:\n")
    with open(args.source, 'r') as f:
        for source in f:
            if len(source) >= 1 and source[:1] != '#':
                get_hosts(source, hosts, ignore_list)
                sources.append(source)

    # sort hosts
    stdout.write("Sorting hosts...\n")
    hosts = sorted(hosts, key=get_hosts_key)

    # set output string
    if isinstance(args.output, list):
        args.output = args.output[0]

    # write hosts
    stdout.write("Writing hosts to: " + args.output + "\n")
    with open(args.output, 'w') as f:
        # header info
        curr_date = datetime.datetime.now().strftime("%B %d, %Y at %I:%M %p")
        f.write("# HostsConcat blocked " + format(len(hosts), ',d') + " hosts.\n" +
                "# Generated on " + curr_date + " using the following sources: \n")

        # sources info
        for source in sources:
            f.write("# " + source)
        f.write("\n\n")

        # write hosts
        for line in hosts:
            f.write(line + '\n')

    # report output
    report_hosts = " host" if len(hosts) == 1 else " hosts"
    report_sources = " source!" if len(sources) == 1 else " sources!"
    print("Blocked " + format(len(hosts), ',d') + report_hosts + " from "
          + str(len(sources)) + report_sources)


def get_hosts_key(host):
    """
    Get key to sort hosts
    :param host: host
    :return: host name
    """
    host_key = host.split()
    if len(host_key) >= 2:
        return host_key[1]
    return host


def get_hosts(source, hosts, ignore_list):
    """
    Get hosts from source
    :param source: url
    :param hosts: list to store hosts
    :param ignore_list: list of hosts to ignore
    """
    data = parse_source(source.rstrip()).splitlines()
    for line in data:
        if line and line[:1] != '#' and line not in hosts and not ignored_host(line, ignore_list):
            line = line.replace('\t', ' ')
            hosts.append(line)


def parse_source(url) -> str:
    """
    HTTP GET source
    :param url: url of source
    :return: string of source contents
    """
    stdout.write("  " + url)
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        return urlopen(req).read().decode('utf-8')
    except urllib.error.HTTPError:
        stdout.write(" ...Header Failed!\n")
        try:
            stdout.write("\tAttempting without header")
            return urlopen(url).read().decode('utf-8')
        except urllib.error.HTTPError:
            stdout.write(" ...HTTP Failed!\n")
    finally:
        stdout.write(" ...OK!\n")


def ignored_host(source, ignore_list) -> bool:
    """
    Determine if source is to be ignored
    :param source: url of source
    :param ignore_list: list of hosts to ignore
    :return: True to ignore host, false otherwise
    """
    for ignore in ignore_list:
        if ignore in source:
            return True
    return False

if __name__ == '__main__':
    main()
