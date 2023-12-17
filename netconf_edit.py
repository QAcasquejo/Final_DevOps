from ncclient import manager
import xml.dom.minidom

# Connect to the device
m = manager.connect(
    host="192.168.231.128",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

#1. Hostname
#2. Interface Description
#3. Credential (username and password)
# Define the NETCONF filter with the configuration changesS
netconf_filter = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>Router8</hostname>
        <interface>
            <GigabitEthernet>
                <name>1</name>
                <description>IsysAD Project</description>
                <ip>
                    <address>
                        <dhcp/>
                    </address>
                </ip>
            </GigabitEthernet>
        </interface>
        <username>
            <name>cisco-IsysAD</name>
            <password>
                <password>ciscol23-IsysAD</password>
            </password>
        </username>
    </native>
</config>
"""

# Use the edit_config operation to apply the configuration changes to the running configuration
netconf_reply = m.edit_config(target="running", config=netconf_filter)

# Print the NETCONF reply
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())