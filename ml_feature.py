class Feature:
    def __init__(self):
        self.duration = ""
        self.header_len = ""
        self.arrival_time = ""
        self.total_packet = ""
        self.variance_data_byte = ""
        self.dev_eui = ""
        self.app_eui = ""
        self.direction = ""
        self.proto = ""
        self.flags = ""
        self.ts = ""
        self.nfq_v = ""
        self.action = ""
        self.lorawan_mac_hdr = ""
        self.lorawan_mac_var = ""
        self.lorawan_frm_hdr = ""
        self.lorawan_frm_var = ""
        self.payload = ""
        self.payload_len = ""
        self.pktlen = ""
        self.alert = ""
        self.fport = ""
        self.mtype = ""
        self.dev_addr = ""
        self.fcnt = ""
        self.fopts = ""
        self.gwsnr = ""
        self.gwrssi = ""
        self.gweui = ""
        self.gwlati = ""
        self.gwlong = ""
        self.gwalti = ""

    def update_feature(self, _dict):
        list = _dict.values()
        phypayload = list[4]
        self.decode_lorawan(phypayload)
        self.dev_eui = list[0]
        self.app_eui = list[1]
        self.fport = list[2]
        self.dev_addr = list[3]
        self.payload = list[5]
        self.payload_len = list[7]
        self.gweui = list[8].get('gwEUI')
        self.gwlati = list[8].get('Lati')
        self.gwlong = list[8].get('Long')
        self.gwalti = list[8].get('Alti')
        self.gwrssi = list[8].get('Rssi')
        self.gwsnr = list[8].get('Snr')
        self.pktlen = len(list[4])*2
        self.header_len = self.pktlen - self.payload_len

    def decode_lorawan(self, phypayload):
        lorawan_dict = {}

        return lorawan_dict