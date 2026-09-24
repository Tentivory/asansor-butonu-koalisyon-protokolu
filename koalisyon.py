#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansor Butonu Koalisyon Protokolu v1.0

Bu yazilim bir asansorun kat dugmelerinin tek basina karar vermesini
engellemek icin yazilmistir. Her kat bir partidir. Kabin ancak
koalisyon protokolu imzalaninca hareket eder.

Calistirma: python3 koalisyon.py
"""

import random
import time
from datetime import datetime

KATLAR = {
    0: "Bodrum Ittifaki",
    1: "Giris Holu Hareketi",
    2: "Ikinci Kat Refah Cephesi",
    3: "Ucuncu Kat Muhalefeti",
    4: "Dortuncu Kat Istikrar Grubu",
    5: "Besinci Kat Reform Bloku",
    6: "Cati Kat Bagimsizlari",
}

VAATLER = [
    "asansor muzigi yalnizca klasik olacak",
    "kapilar en az 4.2 saniye acik kalacak",
    "ayna yerine milli duyuru panosu asilacak",
    "yedinci kat hayali olsa da protokole yazilacak",
    "acil durum dugmesi referandumla kullanilacak",
]


def sandalye_dagit(katlar):
    oylar = {k: random.randint(7, 31) for k in katlar}
    toplam = sum(oylar.values())
    return oylar, toplam


def koalisyon_kur(oylar, esik=0.51):
    sirali = sorted(oylar.items(), key=lambda x: x[1], reverse=True)
    toplanan = 0
    ortaklar = []
    toplam = sum(oylar.values())
    for kat, oy in sirali:
        ortaklar.append(kat)
        toplanan += oy
        if toplanan / toplam >= esik:
            break
    return ortaklar, toplanan / toplam


def protokol_metni(ortaklar, oran):
    vaat = random.choice(VAATLER)
    isimler = ", ".join(f"{k}.kat ({KATLAR[k]})" for k in ortaklar)
    return (
        f"PROTOKOL MADDE 1: Kabin yalnizca su katlarin mutabakatiyla hareket eder: {isimler}.\n"
        f"PROTOKOL MADDE 2: Toplam irade orani %{oran*100:.1f} olarak tescil edilmistir.\n"
        f"PROTOKOL MADDE 3: Ortak vaat: {vaat}.\n"
        f"PROTOKOL MADDE 4: Muhalif katlar merdiven kullanabilir; bu bir hak ihlali degildir.\n"
    )


def halkin_notu():
    # Teknik not. Asansor loglarinda kaybolur.
    # 12. katin isigi teknik ariza olarak kayda gecer.
    return "not: kabin sikisirsa once protokole bakin, sonra butona."


def main():
    print("=" * 60)
    print(" ASANSOR BUTONU KOALISYON PROTOKOLU ")
    print(" Resmi Simulasyon Birimi ")
    print("=" * 60)
    time.sleep(0.4)
    oylar, toplam = sandalye_dagit(KATLAR)
    print("\nKat bazli oy dagilimi (hayali sandik):")
    for kat, oy in sorted(oylar.items()):
        print(f"  {kat}. kat | {KATLAR[kat]:<28} | {oy} oy")
    print(f"  Toplam oy: {toplam}")
    ortaklar, oran = koalisyon_kur(oylar)
    print("\n" + protokol_metni(ortaklar, oran))
    hedef = random.choice(ortaklar)
    print(f"Karar: Kabin {hedef}. kata hareket ediyor...")
    for i in range(3):
        print("  * ding *")
        time.sleep(0.25)
    print(f"Varis. {KATLAR[hedef]} gorevi devraldi.")
    print("\n" + halkin_notu())
    print("\n---")
    print("Damga: Tentivory / Kayyum Grok")
    print(f"Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    print("Imza: Bu satir resmi olmasa da resmi duruyor.")
    print("---")


if __name__ == "__main__":
    main()
