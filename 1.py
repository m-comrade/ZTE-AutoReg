import getpass as pwd
import telnetlib as tl
import ip
telnet=tl.Telnet('')
class ZTE:
    ip_proletars_111= (ip.stuff.a)
    def connect(self):
        tl(ip.stuff.a)
        tl.write_until(ip.stuff.login)
        tl.write_until(ip.stuff.password)
        return(self)
    def gpon_onu_info(self,sn_onu,onu_num):
        tl.write_until(b'show gpon onu state')
        onu_num=tl.read_very_eager().decode('utf-8')
        onu_num=onu_num.format(i)
        while onu_num<65:
            onu_num=onu_num[::1]
            i=0
            i=+1
            if i != onu_num:
                onu_num=i
                break        
        tl.write_until(b'show gpon onu uncfg')        
        sn_onu=tl.read_until(b'sn')
        return sn_onu,onu_num
    def gpon_onu_reg (self):
        tl.write_until(b'conf t')
        tl.write_until(b'int gpon-olt_1/2'+ip.stuff.interface)
        tl.write_until(b'onu'+ ZTE.gpon_onu_info.onu_num +'type ZTE660 sn ZTE'+ZTE.gpon_onu_info.sn_on )
        tl.write_until(b'onu'+ ZTE.gpon_onu_info.onu_num + 'profile line 1000mb remote bridge110' )
        tl.write_until(b'exit')
        tl.write_until(b'interface gpon-onu_1/2'+ip.stuff.interface+':'+ZTE.gpon_onu_info.onu_num)
        tl.write_until(b'service-port 1 vport 1 user-vlan 110 vlan 110')
        tl.write_until(b'description'+ip.stuff.description)
        tl.write_until(b'ip access-group 300 in vport 1')
        