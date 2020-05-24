import logging
logger = logging.getLogger(__name__)

def gen_json(data):
    d = '['
    nd = 0
    for item in data:
        s = '{'
        nitem = 0
        for k in item.keys():
            if nitem == 0:
              s += '"%s":"%s"'%(k, item[k])
              nitem = 1
            else:
                s += ',"%s":"%s"'%(k, item[k])
        s += '}'
        if nd == 0:
            d += s
            nd = 1;
        else:
            d += ',' + s
    d += ']'
    #print(d)
    return d