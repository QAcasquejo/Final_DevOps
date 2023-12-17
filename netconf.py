from ncclient import manager

m = manager.connect(
    host="192.168.231.128",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
    )

result = m.get_config(source='running')
print(result.xml)