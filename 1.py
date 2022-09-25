import getpass as pwd
import telnetlib
import ip
telnet=telnetlib.Telnet('')
class ZTE:
    ip_proletars_111= (a)
    def connect(self):
        telnet(a)
        telnet.write_until(login)
        telnet.write_until(password)
        return(self)
    def gpon_onu_reg(self):
        telnet.write_until(b'show gpon onu state')
        onu_num=telnet.read_very_eager().decode('utf-8')
        while onu_num<65:
            onu_num=onu_num[::1]
            i=0
            i=+1
            if i != onu_num:
                onu_num=i
                break        
        telnet.write_until(b'show gpon onu uncfg')        
        