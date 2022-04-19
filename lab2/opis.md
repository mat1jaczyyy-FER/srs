# Druga laboratorijska vježba: Autentifikacija upotrebom lozinki

Sustav autentifikacije u njegovom nekodiranom stanju je običan Dictionary u Pythonu 3. Ključ predstavlja korisničko ime pojedinog korisnika, a vrijednost je uređeni par (salt, ključ, forcepass flag). Salt i ključ predstavljaju dovoljne informacije kako bi se provjerila točnost lozinke pojedinog korisnika (ali ne i sama lozinka), dok forcepass flag služi kako bi se signalizirala prisiljena promjena lozinke od strane poslužitelja.

Kako bi se napadaču onemogućilo dobivanje ikakvih informacija u slučaju da se nekako domogne datoteke s korisničkim podatcima, postavljena lozinka ne snima se u obliku čistog teksta već se kodira pomoću pouzdane scrypt funkcije derivacije ključa uz pomoć slučajno izabranog salta. Time se osigurava da dvije iste lozinke neće imati isti ključ (**rainbow-tables**). U datoteku se spremaju i salt i ključ.

Točnost lozinke pri uobičajenoj prijavi korisnika provjerava se ponovnim kodiranjem unosa te usporedbom s zapisanim ključem u datoteci. Time je očuvana tajnost lozinki korisnika.

Zahvaljujući takvom sustavu, napadač ne može direktno dobiti informacije o lozinki, već bi trebao utrošiti jako puno računalnih resursa u brute-forceanje lozinke kako bi ju pogodio. Napadač ne može započeti s tim procesom prije dobivanja datoteke radi nepoznatog salta, tako da u slučaju procurene datoteke imamo više nego dovoljno vremena za zatražiti promjenu lozinke od korisnika. U slučaju zatražene promjene, nova lozinka korisnika ne može odgovarati staroj lozinki. Također, uvjetom o duljini lozinke `len(password) >= 10` i povećanjem broja iteracija kod kodiranja scryptom osiguravamo da takav napad ne može u razumnoj količini vremena pogoditi lozinku.

Korisničke lozinke se tijekom unosa ne prikazuju kako bi se zaštitile ikakve informacije o lozinki (**shoulder-surfing**). U `demo.sh` datoteci se prikazuju radi `--test` flaga koji je dodan kako bi se olakšala automatska demonstracija (unos lozinki sa standardnog ulaza) i nije reprezentativno stvarnom korištenju rješenja laboratorijske vježbe. Slijepi napadi na alate također su usporeni time što alat ne daje informaciju što je točno problem prilikom prijave, nepostojeće korisničko ime ili kriva lozinka.

*Dominik Matijaca 0036524568*
