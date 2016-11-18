"""
Hosts Concat
Concatenate multiple host files.

author: Patrick Kubiak
"""

import urllib
from urllib.request import Request, urlopen
from sys import stdout
from pathlib import Path
from datetime import datetime
from argparse import ArgumentParser


def main():
    # store data
    hosts, sources, ignore_list = set(), set(), set()
    existing_hosts_count = 0

    # command-line arguments
    parser = ArgumentParser()
    parser.add_argument('source', type=str, help='file containing list of sources to parse')
    parser.add_argument('-o', '--output', type=str, nargs='?', default="hosts", help='write output hosts to file')
    parser.add_argument('-i', '--ignore', type=str, nargs='?', default="ignore.txt",
                        help='file containing list of hosts to ignore')
    parser.add_argument('-e', '--existing', type=str, nargs='?', default="hosts", help='existing hosts file')
    args = parser.parse_args()

    # read ignore file
    stdout.write("Reading " + args.ignore + "...\n")
    if Path(args.ignore).is_file():
        with open(args.ignore, 'r') as f:
            for source in f:
                if source:
                    stdout.write("  Ignoring " + source + "...\n")
                    ignore_list.add(source)
    else:
        stdout.write("  No ignore list found.\n")

    # read existing hosts file
    stdout.write("Reading " + args.existing + "...\n")
    if Path(args.existing).is_file():
        with open(args.existing, 'r') as f:
            for line in f:
                line = line.rstrip().strip()
                if is_valid_host(line, ignore_list):
                    hosts.add(format_host(line))
        existing_hosts_count = len(hosts)
        stdout.write("  Found " + format(existing_hosts_count, ',d') + " existing hosts.\n")
    else:
        stdout.write("  No existing hosts file found.\n")

    # read sources
    stdout.write("Reading " + args.source + "...\n")
    stdout.write("Parsing:\n")
    with open(args.source, 'r') as f:
        for source in f:
            source = source.rstrip().strip()
            if source[:1] != '#':
                if get_hosts(source, hosts, ignore_list):
                    sources.add(source)

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
        curr_date = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        print("# HostsConcat blocked " + format(len(hosts), ',d') + " hosts.\n" +
              "# Generated on " + curr_date + " using the following sources:", file=f)

        # sources info
        for source in sources:
            print("# " + source, file=f)
        print("\n127.0.0.1 localhost\n" + "::1 ip6-localhost", file=f)

        # write hosts
        for line in hosts:
            print(line, file=f)

    # report output
    report_hosts = " host" if len(hosts) - existing_hosts_count == 1 else " hosts"
    print("Found " + format(len(hosts) - existing_hosts_count, ',d') + " new" + report_hosts + "!")

    report_hosts = " host" if len(hosts) == 1 else " hosts"
    report_sources = " source!" if len(sources) == 1 else " sources!"
    print("Blocked " + format(len(hosts), ',d') + report_hosts + " from " + str(len(sources)) + report_sources)


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


def get_hosts(source, hosts, ignore_list) -> bool:
    """
    Get hosts from source
    :param source: url
    :param hosts: list to store hosts
    :param ignore_list: list of hosts to ignore
    :return: True if parsed source, False otherwise
    """

    data = parse_source(source.rstrip())
    if data:
        data = data.splitlines()
        for line in data:
            if line:
                line = format_host(line)
                if is_valid_host(line, ignore_list):
                    hosts.add(line)
        return True
    return False


def parse_source(url) -> str:
    """
    HTTP GET source
    :param url: url of source
    :return: string of source contents
    """

    output = None
    stdout.write("  " + url)

    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        output = urlopen(req).read().decode('utf-8')
    except urllib.error.HTTPError:
        stdout.write(" ...Header Failed!\n")
        try:
            stdout.write("\tAttempting without header")
            output = urlopen(url).read().decode('utf-8')
        except urllib.error.HTTPError:
            stdout.write(" ...HTTP Failed!\n")
        except urllib.error.URLError:
            stdout.write(" ...Connection Failed!\n")
        else:
            stdout.write(" ...OK!\n")
    except urllib.error.URLError:
        stdout.write(" ...Connection Failed!\n")
    else:
        stdout.write(" ...OK!\n")

    return output


def format_host(host) -> str:
    """
    Format host
    :param host: host to format.
    :return: formatted host.
    """

    host = host.replace('\t', ' ')
    host = host.partition('#')[0]
    host = host.strip()

    # 0.0.0.0 does not wait for a timeout
    return host.replace('127.0.0.1', '0.0.0.0')


def is_valid_host(host, ignore_list) -> bool:
    """
    Check if host is valid.
    :param host: host to validate
    :param hosts: list of hosts
    :param ignore_list: list of ignored hosts
    :return: True if host is valid, False otherwise.
    """

    return host and host[:1] != '#' and not ignored_host(host, ignore_list)


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