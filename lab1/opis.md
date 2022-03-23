# Prva laboratorijska vježba: Simetrična kriptografija

Sustav upravljanja lozinkama u njegovom nekodiranom stanju je običan Dictionary u Pythonu 3. Ključ predstavlja web-mjesto, a vrijednost lozinku koja se pamti za zadano web-mjesto.

Kako bi se sustav zaštitio od neovlaštenog čitanja i pisanja, kada se čita i sprema na disk uvodi se posebno kodiranje. Prvo se Dictionary presloži u običan niz bajtova u memoriji na način da se svaki par ključa i vrijednosti zapisuje jedan pored drugoga sa `0x00` između unosa. Između ključa i vrijednosti se također nalazi `0x00`.

Takav niz se kodira pomoću AES128 blok ciphera za kojeg se ključ generira iz glavne lozinke koju zadaje korisnik i salta koji je slučajno izabran, oboje su određeni pri inicijalizaciji sustava. Prije kodiranog niza zapisuju se generirani salt, nonce i tag. Nonce (number only used once) se ponovno slučajno generira pri svakom spremanju datoteke, dok tag služi za provjeru vjerodostojnosti podataka nakon što ih korisnik kasnije dekodira.

Pri dekodiranju niza, čitaju se salt, nonce i tag, te se uz pomoć korisnikovog ponovnog unosa glavne lozinke, salta i noncea dekodira niz. Uspješnost dekodiranja provjeru se pomoću taga koji je ustvari hash, pa pomoću njega korisnik zna da u datoteci nije nastala nekakva greška.

*Dominik Matijaca 0036524568*
