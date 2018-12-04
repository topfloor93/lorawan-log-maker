class Feature:
    def __init__(self):
        self.header_len = ""
        self.arrival_time = ""
        self.dev_eui = ""
        self.app_eui = ""
        self.direction = ""
        self.proto = ""
        self.action = ""
        self.lorawan_mac_hdr = ""
        self.lorawan_frm_hdr = ""
        self.payload = ""
        self.payload_len = ""
        self.pktlen = ""
        self.fport = ""
        self.mtype = ""
        self.dev_addr = ""
        self.fctrl = ""
        self.fcnt = ""
        self.fopts = ""
        self.gwsnr = ""
        self.gwrssi = ""
        self.gweui = ""
        self.gwlati = ""
        self.gwlong = ""
        self.gwalti = ""

    def update_feature(self, _dict):
        self.pktlen = len(_dict.get('PHYPayload'))/2
        phypayload = self.decode_lorawan(_dict.get('PHYPayload'))
        self.arrival_time = _dict.get('createdTime')
        self.dev_eui = _dict.get('DevEUI')
        self.app_eui = _dict.get('AppEUI')
        self.fport = _dict.get('FPort')
        self.dev_addr = _dict.get('DevAddr')
        self.payload = _dict.get('content')
        self.payload_len = _dict.get('contentSize')
        self.gweui = parse_gwinfo(_dict.get('gwInfo')).get('gwEUI')
        self.gwlati = parse_gwinfo(_dict.get('gwInfo')).get('Lati')
        self.gwlong = parse_gwinfo(_dict.get('gwInfo')).get('Long')
        self.gwalti = parse_gwinfo(_dict.get('gwInfo')).get('Alti')
        self.gwrssi = parse_gwinfo(_dict.get('gwInfo')).get('Rssi')
        self.gwsnr = parse_gwinfo(_dict.get('gwInfo')).get('Snr')
        self.header_len = self.pktlen - self.payload_len
        self.proto = 'lorawan'
        self.lorawan_frm_hdr = phypayload['FHDR']
        self.lorawan_mac_hdr = phypayload['MHDR']
        self.mtype = phypayload['MType']

        if self.mtype == '010' or self.mtype == '100':
            self.direction = 'up'
        else:
            self.direction = 'down'

        self.fctrl = phypayload['Fctrl']
        self.fcnt = phypayload['FCnt']
        self.fopts = phypayload['FOpts']

        if int(self.payload, 16) > 14602888812300048:
            self.action = 'Drop'
        else:
            self.action = 'Accept'

    def decode_lorawan(self, phypayload):
        macphyload = phypayload[2:int(self.pktlen)*2-8]
        foptslen = get_foptslen(macphyload[8:10])
        lorawan_dict = {'MHDR': phypayload[:2],
                        'MACPayload': macphyload,
                        'MIC': phypayload[int(self.pktlen)*2-8:int(self.pktlen)*2],
                        'FHDR': macphyload[:14+foptslen],
                        'Fport': macphyload[14+foptslen:16+foptslen],
                        'FRMPayload': macphyload[16+foptslen],
                        'DevAddr': self.dev_addr,
                        'Fctrl': macphyload[8:10],
                        'FCnt': macphyload[10:14],
                        'FOpts': macphyload[14:14+foptslen],
                        'MType': hex2bin(phypayload[:2])[:3]}

        return lorawan_dict


def get_foptslen(fctrl):
    return int(fctrl[1:], 16)


def dec2bin(n):
    bStr = ''
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    bStr = str(n % 2) + bStr
    return bStr


def hex2bin(hex):
    return dec2bin(int(hex, 16))


def parse_gwinfo(gwinfo):
    res = {}
    gwinfo = gwinfo[:len(gwinfo)-1]
    gwinfo = gwinfo.replace(":", " ")
    gwinfo = gwinfo.replace("  ", " ")
    temp = gwinfo.split(" ")

    for i in range(0, 12, 2):
        res[temp[i]] = temp[i+1]

    return res

