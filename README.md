# **OT_Game_2024 - Game Design Document - SK**
Na danom repozitáre sa nachádza implementácia prototypu hry v Pygame, na skúšku z predmetu objektové technológie.

**Autor**: Samuel Kiss

**Vybraná téma**: One level but constantly changing 
---
## **1. Úvod**
Navrhnutá hra slúži ako ukážka pre predmet Objektové technológie, s cieľom vytvorenia funkčného prototypu hry ako projektu ku skúške. Vytvorená hra spĺňa požiadavky zadanej témy (One level but constantly changing ).
Cieľom hry je udržať sa na platformách čo najdlhšie.

---
### **1.1 Inšpirácia**
<ins>**Sonic the Hedgehog (1991)**</ins>

Sonic the Hedgehog hra je zameraná na hráča ktorý ovláda Sonica, ktorý sa snaží poraziť zloducha Dr. Robotnika (Dr. Eggmana). Koncept hry Sonic the Hedgehog (1991) je postavený na kombinácii rýchlosti, presnosti a zábavy v prostredí 2D platformovky. Hlavnou myšlienkou je vytvoriť jedinečný herný zážitok, ktorý kladie dôraz na dynamiku a plynulosť pohybu, pričom hráč prekonáva prekážky, ničí nepriateľov a objavuje rôznorodé prostredia.
<p align="center">
  <img src="https://github.com/Samuel-kiss/OT_Game/blob/main/Sonic-the-Hedgehog.jpg" alt="Sonic the Hedgehog">
  <br>
  <em> Sonic the Hedgehog (1991)</em>
</p>

### **1.2 Herný zážitok**
Cieľom hry je, aby hráč prežil ***určitý časový interval v hre***, pričom sa bude musieť udržať na platformách.

### **1.3 Vývojový softvér**
- **Pygame-CE**: zvolený programovací jazyk.
- **PyCharm 2024.3**: vybrané IDE.
- **Itch.io**: zdroj grafických assetov a zvukov do hry.
- **Pixabay.com**: zdroj zvukov do hry.

---
## **2. Koncept**

### **2.1 Prehľad hry**
Hráč ovláda svoju postavu a snaží sa prežiť čo najdlhší čas na platformách, ktoré sa postupom času zužujú a ich generovanie sa zrýchľuje.Hráč môže zbierať bonusy, ktoré mu pomôžu prežiť dlhší čas.Hráč musí dávať pozor na padajúce kvapky, ktoré pri dotyku uberajú život.

### **2.2 Interpretácia témy (One level but constantly changing)**
**"One level but constantly changing"** -  hráč sa nachádza v jedinom hernom prostredí (alebo úrovni), ale toto prostredie sa dynamicky transformuje, mení svoje pravidlá, vzhľad, mechaniky alebo interakcie. Hlavným princípom je udržiavať hráča v napätí a výzve tým, že prostredie nie je nikdy úplne statické.

### **2.3 Základné mechaniky**
- **Prekážky**: v hre sa generujú kvapky, ktoré padajú a pri zásahu hrača odoberú jeden život.
- **Bonusy**: hráč môže v hre zbierať bonusy, ktoré mu pridajú život alebo bonusový skok.


### **2.4 Návrh tried**
- **Game**: trieda, v ktorej sa bude nachádzať hlavná herná logika (úvodná obrazovka, herná slučka, vyhodnotenie hry, ...).
- **Player**: trieda reprezentujúca hráča, ovládanie hráča, vykreslenie postavy .
- **Platforms**: trieda reprezentujúca platformy, ich generovanie a vykreslovanie.

---
## **3. Grafika**

### **3.1 Interpretácia témy (One level but constantly changing)**
Hra chce byť vizuálne príťažlivá, kde pomocou assetov z itch.io boli vybrané assety hráča, bonusov, prekážky a platformy. Zameranie je na 2D kreslené objekty, ktoré budú mať minimalistické animácie pohybu.


### **3.2 Dizajn**
V hre boli použité assety z itch.io.Cieľom bolo dosiahnuť na pohľad príjemný animovaný dizajn v kontexte arkádovej skákačky.

<p align="center">
  <img src="https://github.com/Samuel-kiss/OT_Game/blob/main/nahlad_hry.png" alt="Dizajn hry">
  <br>
  <em>Ukážka dizajnu hry</em>
</p>

---
## **4. Zvuk**

### **4.1 Hudba**
Výber hudby do pozadia bol zameraný na 8-bit žánrovo orientovanú hudbu, ktorá bola vybraná zo stránky (https://pixabay.com/music/) a bude poskytovať vhodný nádych arkádovej tématiky, ktorý vhodne dopĺňa grafický dizajn hry.

### **4.2 Zvuky**
Zvuky v hre boli podobne orientované na 8-bit zvuky, pričom boli opätovne použité voľne dostupné assety (https://pixabay.com/sound-effects/), z ktorých boli vybrané zvuky na skákanie, pohyb, minutie života.

---
## **5. Herný zážitok**

### **5.1 Používateľské rozhranie**
Používateľské rozhranie bude orientované do ostatného grafického štýlu a úvodná obrazovka bude obsahovať možnosť spustiť a ukončiť hru.

### **5.2 Ovládanie**
<ins>**Klávesnica**</ins>
- **Klávesy šípok <- a ->**: pohyb hráča do strán.
- **Space bar**: skočenie alebo použitie bonusového skoku vo vzduchu.
