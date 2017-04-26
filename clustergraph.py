import csv
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages as pdf


def netdict(infile, delim=','):
    netd={}
    f = csv.reader(open(infile))
    for row in f:
        key=row[0]
        if key in netd:
            pass
        netd[key]=row[1].split(',')
    return netd

def attdict(infile, delim=','):
    atd={}
    f = csv.reader(open(infile))
    for row in f:
        key=row[0]
        if key in atd:
            pass
        atd[key]=[float(x) for x in row[2].split(',')]
    return atd

def getnodecol(atd):
    col={}
    for k in atd:
        col[k]='%.1f' % round(sum(atd[k])/len(atd[k]),1)
    return col

def makenet(netd,atd,col):
    G=nx.from_dict_of_lists(netd)
    nx.set_node_attributes(G,'tpm',atd)
    nx.set_node_attributes(G,'color',col)
    return G

def gengraph(G):
    gr=nx.draw_networkx(G,with_labels=True,node_color=list(dict.values(nx.get_node_attributes(testnet,'color'))))
    return gr

def exgraph(gr,outpath):
    pdf.savefig(outpath)
