import urllib
from urllib.request import Request, urlopen


def main():
    # store unique hosts
    hosts = []

    # read sources
    with open('sources.txt', 'r') as f:
        for source in f:
            if source and source.find('#') == -1:
                get_source(source, hosts)

    # write hosts
    with open('hosts', 'w') as f:
        for line in hosts:
            f.write(line + '\n')


def get_source(source, hosts):
    '''
    Get data from source
    :param source: url
    :param hosts: list to store hosts
    '''
    data = parse_source(source).splitlines()
    for line in data:
        if line and line.find('#') == -1 and line not in hosts:
            line = line.replace('\t', ' ')
            hosts.append(line)


def parse_source(url) -> str:
    """
    HTTP GET source
    :param url: url of source
    :return: string of source contents
    """
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        return urlopen(req).read().decode('utf-8')
    except urllib.error.HTTPError:
        return urlopen(url).read().decode('utf-8')


if __name__ == '__main__':
    main()
