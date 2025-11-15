# Program se provadi pouze pri spusteni JMRI
# Definuji se vsechny promenne a provadi se nastaveni "Stuj" na navestidlech 

import jmri
import jarray

cekani_stanice = 10000
cekani_vyhybka = 2000
zpozdeni = 5000
zpozdeni_while = 1000
zpozdeni_signal = 5000

z5_petrov = memories.provideMemory("z5_petrov")
z3_petrov = memories.provideMemory("z3_petrov")
dir_sobotin = memories.provideMemory("dir_sobotin")
dir_zabreh = memories.provideMemory("dir_zabreh")

z5_petrov.value = False
z3_petrov.value = False
dir_sobotin.value = 0
dir_zabreh.value = 0

default_enable = sensors.provideSensor("IS8")
zabreh_kriz = sensors.provideSensor("IS9")

# Deklarace snimacu obsazeni do pole

LS = [ sensors.provideSensor("LS1"),
        sensors.provideSensor("LS1"),
        sensors.provideSensor("LS2"),
        sensors.provideSensor("LS3"),
        sensors.provideSensor("LS4"),
        sensors.provideSensor("LS5"),
        sensors.provideSensor("LS6"),
        sensors.provideSensor("LS7"),
        sensors.provideSensor("LS8"),
        sensors.provideSensor("LS9"),
        sensors.provideSensor("LS10"),
        sensors.provideSensor("LS11"),
        sensors.provideSensor("LS12"),
        sensors.provideSensor("LS13"),
        sensors.provideSensor("LS14"),
        sensors.provideSensor("LS15"),
        sensors.provideSensor("LS16"),
        sensors.provideSensor("LS17"),
        sensors.provideSensor("LS18"),
        sensors.provideSensor("LS19"),
        sensors.provideSensor("LS20"),
        sensors.provideSensor("LS21"),
        sensors.provideSensor("LS22"),
        sensors.provideSensor("LS23"),
        sensors.provideSensor("LS24"),
        sensors.provideSensor("LS25"),
        sensors.provideSensor("LS26"),
        sensors.provideSensor("LS27"),
        sensors.provideSensor("LS28"),
        sensors.provideSensor("LS29"),
        sensors.provideSensor("LS30"),
        sensors.provideSensor("LS31"),
        sensors.provideSensor("LS32"),
        sensors.provideSensor("LS33"),
        sensors.provideSensor("LS34"),
        sensors.provideSensor("LS35"),
        sensors.provideSensor("LS36"),
        sensors.provideSensor("LS37"),
        sensors.provideSensor("LS38"),
        sensors.provideSensor("LS39"),
        sensors.provideSensor("LS40")]    


# Deklarace alokacnich bloku do pole 

IS = [sensors.provideSensor("IS10"),
      sensors.provideSensor("IS10"),
      sensors.provideSensor("IS11"),
      sensors.provideSensor("IS12"),
      sensors.provideSensor("IS13"),
      sensors.provideSensor("IS14"),
      sensors.provideSensor("IS15"),
      sensors.provideSensor("IS16"),
      sensors.provideSensor("IS17"),
      sensors.provideSensor("IS18"),
      sensors.provideSensor("IS19"),
      sensors.provideSensor("IS20"),
      sensors.provideSensor("IS21"),
      sensors.provideSensor("IS22"),
      sensors.provideSensor("IS23"),
      sensors.provideSensor("IS24"),
      sensors.provideSensor("IS25"),
      sensors.provideSensor("IS26"),
      sensors.provideSensor("IS27"),
      sensors.provideSensor("IS28"),
      sensors.provideSensor("IS29"),
      sensors.provideSensor("IS30"),
      sensors.provideSensor("IS31"),
      sensors.provideSensor("IS32"),
      sensors.provideSensor("IS33"),
      sensors.provideSensor("IS34"),
      sensors.provideSensor("IS35"),
      sensors.provideSensor("IS36"),
      sensors.provideSensor("IS37"),
      sensors.provideSensor("IS38"),
      sensors.provideSensor("IS39"),
      sensors.provideSensor("IS40"),
      sensors.provideSensor("IS41"),
      sensors.provideSensor("IS42"),
      sensors.provideSensor("IS43"),
      sensors.provideSensor("IS44"),
      sensors.provideSensor("IS45"),
      sensors.provideSensor("IS46"),
      sensors.provideSensor("IS47"),
      sensors.provideSensor("IS48"),
      sensors.provideSensor("IS49")]     


# Deklarace vyhybek do pole

LT = [ turnouts.provideTurnout("LT200"),
       turnouts.provideTurnout("LT200"),
       turnouts.provideTurnout("LT201"),
       turnouts.provideTurnout("LT202"),
       turnouts.provideTurnout("LT203"),
       turnouts.provideTurnout("LT204"),
       turnouts.provideTurnout("LT205"),
       turnouts.provideTurnout("LT206"),
       turnouts.provideTurnout("LT207"),
       turnouts.provideTurnout("LT208"),
       turnouts.provideTurnout("LT209"),
       turnouts.provideTurnout("LT210"),
       turnouts.provideTurnout("LT211"),
       turnouts.provideTurnout("LT212"),
       turnouts.provideTurnout("LT213"),
       turnouts.provideTurnout("LT214"),
       turnouts.provideTurnout("LT215"),
       turnouts.provideTurnout("LT216"),
       turnouts.provideTurnout("LT217"),
       turnouts.provideTurnout("LT218"),
       turnouts.provideTurnout("LT219"),
       turnouts.provideTurnout("LT220")]    


# Deklarace navestidel do pole

NAV = [masts.getSignalMast("Nav-1-A"),
       masts.getSignalMast("Nav-1-A"),
       masts.getSignalMast("Nav-1-B"),
       masts.getSignalMast("Nav-1-C"),
       masts.getSignalMast("Nav-1-D"),
       masts.getSignalMast("Nav-1-E"),
       masts.getSignalMast("Nav-1-F"),
       masts.getSignalMast("Nav-1-G"),
       masts.getSignalMast("Nav-1-H"),
       masts.getSignalMast("Nav-1-I"),
       masts.getSignalMast("Nav-1-J"),
       masts.getSignalMast("Nav-1-K"),
       masts.getSignalMast("Nav-1-L"),
       masts.getSignalMast("Nav-1-M"),
       masts.getSignalMast("Nav-1-N"),
       masts.getSignalMast("Nav-1-O"),
       masts.getSignalMast("Nav-1-P"),
       masts.getSignalMast("Nav-2-A"),
       masts.getSignalMast("Nav-2-B"),
       masts.getSignalMast("Nav-2-C"),
       masts.getSignalMast("Nav-2-D"),
       masts.getSignalMast("Nav-2-E"),
       masts.getSignalMast("Nav-2-F"),
       masts.getSignalMast("Nav-2-G"),
       masts.getSignalMast("Nav-2-H"),
       masts.getSignalMast("Nav-2-I"),
       masts.getSignalMast("Nav-2-J"),
       masts.getSignalMast("Nav-2-K"),
       masts.getSignalMast("Nav-2-L"),
       masts.getSignalMast("Nav-2-M"),
       masts.getSignalMast("Nav-2-N"),
       masts.getSignalMast("Nav-2-O"),
       masts.getSignalMast("Nav-2-P"),
       masts.getSignalMast("Nav-3-A"),
       masts.getSignalMast("Nav-3-B"),
       masts.getSignalMast("Nav-3-C"),
       masts.getSignalMast("Nav-3-D"),
       masts.getSignalMast("Nav-3-E"),
       masts.getSignalMast("Nav-3-F"),
       masts.getSignalMast("Nav-3-G"),
       masts.getSignalMast("Nav-3-H"),
       masts.getSignalMast("Nav-3-I"),
       masts.getSignalMast("Nav-3-J"),
       masts.getSignalMast("Nav-3-K"),
       masts.getSignalMast("Nav-3-L")]   


# Deklarace ABS navestidel do pole

ABS = [masts.getSignalMast("Nav-AB-A"),
       masts.getSignalMast("Nav-AB-A"),
       masts.getSignalMast("Nav-AB-B"),
       masts.getSignalMast("Nav-AB-C"),
       masts.getSignalMast("Nav-AB-D"),
       masts.getSignalMast("Nav-AB-E"),
       masts.getSignalMast("Nav-AB-F"),
       masts.getSignalMast("Nav-AB-G"),
       masts.getSignalMast("Nav-AB-H")]   


# Deklarace osvetleni do pole 

#OSV = [turnouts.provideTurnout("LT221"),
#       turnouts.provideTurnout("LT221"),
#       turnouts.provideTurnout("LT222"),
#       turnouts.provideTurnout("LT223"),
#       turnouts.provideTurnout("LT224"),
#       turnouts.provideTurnout("LT225"),
#       turnouts.provideTurnout("LT226")]    


# Deklarace radicu smeru

DIR_OUT =  [  sensors.provideSensor("IS100"),
              sensors.provideSensor("IS100"),
              sensors.provideSensor("IS103"),
              sensors.provideSensor("IS106"),
              sensors.provideSensor("IS109"),
              sensors.provideSensor("IS112"),
              sensors.provideSensor("IS115"),
              sensors.provideSensor("IS118"),
              sensors.provideSensor("IS121"),
              sensors.provideSensor("IS124"),
              sensors.provideSensor("IS127"),
              sensors.provideSensor("IS130"),
              sensors.provideSensor("IS133"),
              sensors.provideSensor("IS136")]

DIR_IN =   [  sensors.provideSensor("IS101"),
              sensors.provideSensor("IS101"),
              sensors.provideSensor("IS104"),
              sensors.provideSensor("IS107"),
              sensors.provideSensor("IS110"),
              sensors.provideSensor("IS113"),
              sensors.provideSensor("IS116"),
              sensors.provideSensor("IS119"),
              sensors.provideSensor("IS122"),
              sensors.provideSensor("IS125"),
              sensors.provideSensor("IS128"),
              sensors.provideSensor("IS131"),
              sensors.provideSensor("IS134"),
              sensors.provideSensor("IS137")]

DIR_STOP = [  sensors.provideSensor("IS102"),
              sensors.provideSensor("IS102"),
              sensors.provideSensor("IS105"),
              sensors.provideSensor("IS108"),
              sensors.provideSensor("IS111"),
              sensors.provideSensor("IS114"),
              sensors.provideSensor("IS117"),
              sensors.provideSensor("IS120"),
              sensors.provideSensor("IS123"),
              sensors.provideSensor("IS126"),
              sensors.provideSensor("IS129"),
              sensors.provideSensor("IS132"),
              sensors.provideSensor("IS135"),
              sensors.provideSensor("IS138")]


# Vychozi stavy

for i in range(len(DIR_STOP)):
       DIR_STOP[i].setKnownState(ACTIVE)       
