# Četvrta laboratorijska vježba: Sigurnost mrežnih protokola i vatrozid

Za potrebe ove laboratorijske vježbe, koristi se isti virtualni stroj za proučavanje ranjivosti iz treće laboratorijske vježbe. Za nesmetan rad, na virtualnom stroju nalazi se IMUNES simulacija male mreže s demilitariziranom zonom čija je svrha pomoći nam bolje razumjeti procese osiguranja mreže.

---

## Pokretanje eksperimenta

Nakon dohvaćanja sadržaja vježbe iz git repozitorija, pokrećemo IMUNES eksperiment.

Sa računala `PC1` uspostavljamo vezu na `server` pomoću telnet i ssh alata. U oba slučaja veza je uspješno uspostavljena i `server` nas pita podatke za prijavu. Na sučelju `eth0` čvora `firewall` pomoću Wireshark-a možemo prisluškivati obje TCP veze jer su one u potpunosti nezaštićene i vidljive.

---

## Konfiguracija vatrozida

Vatrozid konfiguriramo pomoću alata iptables. On nam omogućava postavljanje pravila eksplicitnog prihvaćanja ili odbijanja paketa prema određenim kriterijima (ulazni/proslijeđeni/izlazni paket, ulazni/izlazni interface ili IP adresa, vrsta protokola, status konekcije, izvorišni i odredišni port). Zahtjevana pravila iz teksta laboratorijske vježbe s tim alatom su implementirana u datoteci `FW.sh` koja se pokreće na `firewall`-u i automatski konfigurira vatrozid.

----

*Dominik Matijaca 0036524568*
