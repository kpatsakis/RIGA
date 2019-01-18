#!/usr/bin/python
import requests
from time import time, sleep
import json

# get working gateways
gateways_URL = "https://ipfs.github.io/public-gateway-checker/gateways.json"
r = requests.get(gateways_URL)
gateways = json.loads(r.text)
h = "Qmaisz6NMhDB51cCvNWa1GMS7LU1pAxdF4Ld6Ft9kZEP2a"
gw = []
for g in gateways:
    url = g.replace(":hash", h)
    try:
        r = requests.get(url, timeout=5)
        if "Hello from IPFS Gateway Checker" in r.text:
            gw.append(g.replace(":hash", ""))
    except:
        pass
print "There are %d IPFS gateways working now." % len(gw)


# add some content from wikipedia to query the gateways
content = ["QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Domain_generation_algorithm.html", "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Malware.html",
           "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Public-key_cryptography.html",
           "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Digital_signature.html",
           "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Botnet.html",
           "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Command_and_control_(malware).html",
           "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Conficker.html",
           "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Zeus_(Trojan_horse).html",
           "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Srizbi_botnet.html",
           "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/CryptoLocker.html",
           "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Domain_Name_System.html", "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Computer_worm.html",
           "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Welchia.html",
           "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Administrative_share.html",
           "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Push_technology.html",
           "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Pull_technology.html",
           "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Pseudorandom_number_generator.html",
           "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/SHA-1.html",
           "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/RSA_(algorithm).html",
           "QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/MD6.html"]

print "Checking for availability..."
loops = 50
time_outs = [5]
for t in time_outs:
    print "Timeout set to %d seconds." % t
    for g in gw:
        ts = time()
        errs = 0
        cnt = 0
        dropped = 0
        for i in range(loops):
            for c in content:
                try:
                    r = requests.get(g + c, timeout=t)
                    if r.status_code != 200:
                        errs += 1
                except:
                    dropped += 1
                cnt += 1
        te = time()
        print g, te - ts, errs, dropped
