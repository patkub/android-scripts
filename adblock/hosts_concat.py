from sys import stdout
import datetime
import argparse
import urllib
from urllib.request import Request, urlopen


def main():
    # store unique hosts
    hosts = []
    sources = []

    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=str, help='sources to read hosts from')
    parser.add_argument('-o', '--output', type=str, nargs='*', default="hosts", help='file to write hosts output to')
    args = parser.parse_args()

    # read sources
    stdout.write("Reading " + args.source + "...\n")
    stdout.write("Parsing:\n")
    with open(args.source, 'r') as f:
        for source in f:
            if len(source) >= 1 and source[:1] != '#':
                get_hosts(source, hosts)
                sources.append(source)

    # sort hosts
    stdout.write("Sorting hosts...\n")
    hosts = sorted(hosts, key=get_hosts_key)

    if isinstance(args.output, list):
        args.output = args.output[0]

    # write hosts
    stdout.write("Writing hosts to: " + args.output + "\n")

    with open(args.output, 'w') as f:
        curr_date = datetime.datetime.now().strftime("%B %d, %Y at %I:%M %p")
        f.write("# HostsConcat blocked " + format(len(hosts), ',d') + " hosts.\n" +
                "# Generated on " + curr_date + " using the following sources: \n")
        for source in sources:
            f.write("# " + source)
        f.write("\n\n")

        for line in hosts:
            f.write(line + '\n')

    report_hosts = " host" if len(hosts) == 1 else " hosts"
    report_sources = " source!" if len(sources) == 1 else " sources!"

    print("Blocked " + format(len(hosts), ',d') + report_hosts + " from "
          + str(len(sources)) + report_sources)


def get_hosts_key(s):
    """
    Get key to sort hosts
    :param s: host
    :return: host name
    """
    new_s = s.split()
    if len(new_s) >= 2:
        return new_s[1]
    return s


def get_hosts(source, hosts):
    """
    Get hosts from source
    :param source: url
    :param hosts: list to store hosts
    """
    data = parse_source(source.rstrip()).splitlines()
    for line in data:
        if line and line[:1] != '#' and line not in hosts:
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
            stdout.write("HTTP Failed!\n")
    finally:
        stdout.write(" ...OK!\n")


if __name__ == '__main__':
    main()
