# Prva laboratorijska vježba: Simetrična kriptografija

Sustav upravljanja lozinkama u njegovom nekodiranom stanju je običan Dictionary u Pythonu 3. Ključ predstavlja web-mjesto, a vrijednost lozinku koja se pamti za zadano web-mjesto.

Kako bi se sustav zaštitio od neovlaštenog čitanja i pisanja, kada se čita i sprema na disk uvodi se posebno kodiranje. Prvo se Dictionary presloži u običan niz bajtova u memoriji na način da se svaki par ključa i vrijednosti zapisuje jedan pored drugoga sa `0x00` između unosa. Između ključa i vrijednosti se također nalazi `0x00`.

Takav niz se kodira pomoću AES128 blok ciphera za kojeg se ključ generira iz glavne lozinke koju zadaje korisnik pri inicijalizaciji sustava. Prije kodiranog niza zapisuju se nonce i tag,

*Dominik Matijaca 0036524568*
