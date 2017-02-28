'''
some utils for the test
'''

import sys

def get_test_data_path(fname):
    print "The repo is in are in ",sys.argv[0].split('repoNoData')[0]
    path = "/dls/science/users/clb02321/DAWN_stable/GithubLFS/repo4data/test_data/%s"
    return path % fname