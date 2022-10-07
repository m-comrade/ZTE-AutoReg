import telnetlib as tl
import ip
telnet=tl.Telnet('')
class ZTE:
    def connect(self):
        tn=telnet(ip.stuff.ip)
        telnet.write_until(ip.stuff.user)
        return(tn)
    def gpon_onu_info(self):
        telnet.write_until(b'show gpon onu state')
        telnet.write(b'show gpon onu uncfg')
        sn_onu=telnet.read_until(b'gpon')
        if telnet.read_until(b'No related information to show'):
            print('все онушки регнуты')
        else:
            onu_num=telnet.read_very_eager().decode('utf-8')
            onu_num=onu_num.format(i)
            while onu_num<129:
                onu_num=onu_num[::1]
                i=0
                i=+1
                if i != onu_num:
                    onu_num=i
                    break                   
        return(onu_num,sn_onu)
    print(gpon_onu_info)   
    def gpon_onu_reg (self):
        telnet.write(b'conf t')
        telnet.write(b'int gpon-olt_1/2'+ip.stuff.interface)
        telnet.write(b'onu'+ ZTE.gpon_onu_info.onu_num +'type ZTE660 sn ZTE'+ZTE.gpon_onu_info.sn_onu )
        telnet.write(b'onu'+ ZTE.gpon_onu_info.onu_num + 'profile line 1000mb remote bridge110' )
        telnet.write(b'exit')
        telnet.write(b'interface gpon-onu_1/2'+ip.stuff.interface+':'+ZTE.gpon_onu_info.onu_num)
        telnet.write(b'service-port 1 vport 1 user-vlan'+ip.vlan_id+'vlan' + ip.vlan_id )
        telnet.write(b'description'+ip.stuff.description)
        telnet.write(b'ip access-group 300 in vport 1')
        