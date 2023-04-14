import netifaces

# Získání seznamu síťových rozhraní
interfaces = netifaces.interfaces()

# Pro každé síťové rozhraní získáme IP adresy
for iface in interfaces:
    addresses = netifaces.ifaddresses(iface)
    ip_addresses = addresses.get(netifaces.AF_INET)
    
    # Pokud jsou k dispozici nějaké IP adresy, vypište je
    if ip_addresses:
        print(f"Síťové rozhraní {iface}:")
        for ip in ip_addresses:
            print(f"- IP adresa: {ip['addr']}")
   
    