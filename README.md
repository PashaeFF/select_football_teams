# Select Football Teams

Kechen oyun oyunchularini <b>"/data/last_teams.py"</b>, kechen oyun nakidka geyinenleri ise <b>"data/last_yellow_dresseds_team.py"</b> faylina elave edin

Proqram oyunchularin bal sistemine uygun <b>Random</b> komandalar bolur, arada ele de ciddi bal ferqi olmur.
Nakidka geyinenleri ise "data/last_yellow_dresseds_team.py" faylinda gorur, yeni bolunmush komandalarin ichinde gezir,
kechen oyun nakidka geyinenlerin arasinda ve yeni random sechilen team'ler arasinda kesishmeli "for" dongusu edir.
Ona uygun count qaytarir ki, meselen: Team 1-e dushenler icinde 2 nefer, Team 2-ye dushenler arasinda 4 nefer kechen oyun nakidka geyinib.
Hansi azdirsa, az olan komandaya nakidka verir, yox eger tesaduf neticesinde 
meselen 3-3 dushse(meselen, kecen oyun nakidka geyinenlerden 3-u bir komandyaa dushub, 3-u ise diger komandaya), bu halda nakidkani da random her hansi bir komandaya verecek.

><u>Example</u>

<i><h6>Kechen oyun Team 1 uzre forma geyinenlerin sayi:  2
Kechen oyun Team 2 uzre forma geyinenlerin sayi:  4

Team 1:
1) Azad => 90
2) Tacir => 70
3) Huseyn => 80
4) Karim => 80
5) Rafiq => 60
6) Shukran => 90

Team Power: 470

Team 1 nakidka geyinmelidir...

Team 2:
1) Hasan => 70
2) Sabuhi => 60
3) Tural => 70
4) Nicat => 80
5) Ahmad => 90
6) Iqbal => 70

Team Power: 440
</h6></i>

Default olaraq <b>"static.py"</b> faylinda oyunchular listde dictionary sheklinde yer alib, meselen:
<i><b>"self.humans = [{'name':'Rafiq','rating':60}]"</b></i>
Lakin proqrami run edib daxilinde oyuna qatilmayacaq oyunchulari sile, evezine oyuna girecek oyunculari elave ede bilersiniz.

#####Reytinq sistemi 40-100 arasi goturulub.


<b>self.level_1 = [ ] >> Rating(80-100)</b>
<b>self.level_2 = [ ] >> Rating(61-80)</b>
<b>self.level_3 = [ ] >> Rating(40-60) </b>

Bu o demekdir ki, siz oyunchu secimi ederken proqram ilk once <i><b>"self.humans = []"</b></i>  listinin daxilinde gezir ve bala uygun oyunchuleri bu 3 liste bolur.
Sonra bu listdekileri ten yaridan 2 komanda listine bolur, eger oyunchu sayinda ferq <i>(meselen level 1de 3 nefer varsa 1-ni bir komandaya, 2-cisini diger komandaya verir, buda <b>'BUG'</b>-a yol acir. Hansi ki, ola biler komandalar arasi oyunchular sayinda ferq olsun)</i> olarsa, diger komandadan reytinqe uygun oyunchu elave edir ki, komandalarda oyunchu sayinda ferq olmasin(yalniz tek sayda oyuncu olarsa ferq ola biler, meselen 13 nefer varsa 1 neferi random bashqa komandaya atacaq).

##### Qeyd:
<b>Team</b>'ler sechilenden sonra <b>"H/Y"</b> chixir, siz <b>"H"</b> sechdikde oyunchulari <b>"/data/last_teams.py"</b> faylina, Nakidka geyinen komandanin oyunchu adlarini ise <b>"data/last_yellow_dresseds_team.py"</b> faylina elave edir.
Eger <b>"Y"</b> sechseniz, hech yere hechne elave etmir, yeniden komanda sechimi edir...

##### Qeyd 2:
Proqrami <b>run</b> etdikden sonra elave etdiyiniz ve sildiyiniz oyunchular proqrami bagladiqdan sonra,
<i><b>"self.humans = [{'name':'Rafiq','rating':60}]"</b></i> listinde qalmir. Eger Team kimi sechiliblerse <b>"/data/last_teams.py"</b> ve <b>"data/last_yellow_dresseds_team.py"</b> fayllarina adlari dushur ki(Kohne komandalar ve nakidka geyinenler siyahisina).