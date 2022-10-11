from asyncore import write
from gettext import find
import telnetlib as tl
import ip
#global argument
telnet=tl.Telnet('')
class ZTE:
    
#define of connection to switch
    def connect(self):
        tn=telnet(ip.stuff.ip)
        telnet.write_until(ip.stuff.user)
        return(tn)
          #pars interface
    def onu_state(self):      
        string_onu_state=telnet.write(b'show gpon onu state')
        return string_onu_state
    def onu_uncfg(self):    
        string_onu_=telnet.write(b'show gpon onu uncfg')
        return string_onu_      
    def interface(self):
        interface=ZTE.onu_uncfg
        interface=interface.split(' ')   
        interface_index_start = find(interface,b'gpon-onu_1/')
        interface_index_end=find(interface,'ZTE')
        interface_index=interface.index(interface_index_start,interface_index_end)
        interface=interface[interface_index]
        return interface
        #define of reading information from commandlets    
    def gpon_onu_sn(self):
        sn_onu=telnet.read_until(b'gpon')
        #check  onu registration 
        if telnet.read_until(b'No related information to show'):
            print('все онушки регнуты')                
        return(sn_onu)
    def gpon_onu_num(self):
        onu_num=ZTE.onu_state
        onu_num=onu_num.format(i)
            #find of non reg number of onu
        while onu_num<129:
            onu_num=onu_num[::1]
            i=0
            i=+1 
            if i != onu_num:
                onu_num=i
                break
            return onu_num   
    #reg commandlets  
    def gpon_onu_reg (self):
        telnet.write(b'conf t')
        telnet.write(b'int gpon-olt_1/2'+ZTE.interface)
        telnet.write(b'onu'+ ZTE.gpon_onu_num +'type ZTE660 sn ZTE'+ZTE.gpon_onu_sn )
        telnet.write(b'onu'+ ZTE.gpon_onu_num + 'profile line 1000mb remote bridge110' )
        telnet.write(b'exit')
        telnet.write(b'interface gpon-onu_1/2'+ZTE.interface + ':'+ ZTE.gpon_onu_num)
        telnet.write(b'service-port 1 vport 1 user-vlan'+ip.vlan_id +'vlan' + ip.vlan_id )
        telnet.write(b'description'+ip.stuff.description)
        telnet.write(b'ip access-group 300 in vport 1')
class ZTE_epon:
    def epon_onu_unauth_interface (self):
        ZTE.connect
        telnet.write(b'whow onu una')
        interface=telnet.read_until(b'Onu Model')
        interface_index_start=find(interface,b'epon-onu_1/1/')
        interface_index_end=find(interface,b'\n')
        interface_index=interface.index(interface_index_start,interface_index_end)
        interface=interface[interface_index]
        return interface
    def  epon_onu_state(self):
        #переписать хуйню сверху и эту в отдельную функцию из предидущего класса
        telnet.write(b'')
    def epon_onu_reg(self):
        telnet.write(b'conf t')
        telnet.write(b'int ' + ZTE_epon.epon_onu_unauth_interface)
        telnet.write(b'onu ' + None)# + та хуйня сверху ,которую надо переписать)    
        telnet.write(b'!')
        telnet.write(b'int ' +ZTE_epon.epon_onu_unauth_interface + 'та хуйня')
        telnet.write(b'admin enable \n sla-profile 1000mbit vport 1')
        telnet.write(b'encrypt direction downstream disable vport 1')
        telnet.write(b'switchport vlan '+ ip.stuff.vlan_id + b' tag vport 1')
        telnet.write(b'ip access-group 300 in vport 1')
        telnet.write(b'Property description '+ ip.stuff.description)
        telnet.write(b'!')    