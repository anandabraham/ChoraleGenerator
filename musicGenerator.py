from music import *
from javax.swing import *
from java.awt import *
import sys
import random
INSTRUMENTS = {'SOPRANO':FLUTE, 'ALTO':TRUMPET, 'TENOR':HORN, 'BASS':CONTRABASS, 'PIANO' : 0,
'BRIGHT_ACOUSTIC' : 1,
'ELECTRIC_GRAND' : 2,
'HONKYTONK' : 3,
'RHODES_PIANO' : 4,
'DX_PIANO' : 5,
'HARPSICHORD' : 6,
'CLAVINET' : 7,
'CELESTA' : 8,
'GLOCKENSPIEL' : 9,
'MUSIC_BOX' : 10,
'VIBRAPHONE: 11,
'MARIMBA' : 12,
'XYLOPHONE' : 13,
'TUBULAR_BELLS' : 14,
'DULCIMER' : 15,
'ORGAN' : 16,
'JAZZ_ORGAN' : 17,
'ROCK_ORGAN' : 18,
'CHURCH_ORGAN' : 19,
'REED_ORGAN' : 20,
'ACCORDION' : 21,
'HARMONICA' : 22,
'TANGO_ACCORDION' : 23,
'GUITAR' : 24,
'STEEL_GUITAR' : 25,
'JAZZ_GUITAR' : 26,
'ELECTRIC_GUITAR' : 27,
'MUTED_GUITAR' : 28,
'OVERDRIVEN_GUITAR' : 29,
'DISTORTION_GUITAR' : 30,
'GUITAR_HARMONICS' : 31,
'ACOUSTIC_BASS' : 32,
'ELECTRIC_BASS' : 33,
'PICKED_BASS' : 34,
'FRETLESS_BASS' : 35,
'SLAP_BASS1' : 36,
'SLAP_BASS2' : 37,
'SYNTH_BASS1' : 38,
'SYNTH_BASS2' : 39,
'VIOLIN' : 40,
'VIOLA' : 41,
'CELLO' : 42,
'CONTRABASS' : 43,
'TREMOLO_STRINGS' : 44,
'PIZZICATO_STRINGS' : 45,
'HARP' : 46,
'TIMPANI' : 47,
'STRING_ENSEMBLE1' : 48,
'STRING_ENSEMBLE2' : 49,
'SYNTH_STRINGS1' : 50,
'SYNTH_STRINGS2' : 51,
'CHOIR' : 52,
'VOICE' : 53,
'VOX' : 54,
'ORCHESTRA_HIT' : 55,
'TRUMPET' : 56,
'TROMBONE' : 57,
'TUBA' : 58,
'MUTED_TRUMPET' : 59,
'FRENCH_HORN' : 60,
'BRASS_SECTION' : 61,
'SYNTH_BRASS1' : 62,
'SYNTH_BRASS2' : 63,
'SOPRANO_SAXOPHONE' : 64,
'ALTO_SAXOPHONE' : 65,
'SAXOPHONE' : 66,
'BARITONE_SAXOPHONE' : 67,
'OBOE' : 68,
'ENGLISH_HORN' : 69,
'BASSOON' : 70,
'CLARINET' : 71,
'PICCOLO' : 72,
'FLUTE' : 73,
'RECORDER' : 74,
'PAN_FLUTE' : 75,
'BOTTLE' : 76,
'SHAKUHACHI' : 77,
'WHISTLE' : 78,
'OCARINA' : 79,
'SQUARE' : 80,
'SAWTOOTH' : 81,
'CALLIOPE' : 82,
'CHIFF' : 83,
'CHARANG' : 84,
'SOLO_VOX' : 85,
'FIFTHS' : 86,
'BASS_LEAD' : 87,
'NEW_AGE' : 88,
'WARM_PAD' : 89,
'POLYSYNTH' : 90,
'SPACE_VOICE' : 91,
'BOWED_GLASS' : 92,
'METALLIC' : 93,
'HALO' : 94,
'SWEEP' : 95,
'ICE_RAIN' : 96,
'SOUNDTRACK' : 97,
'CRYSTAL' : 98,
'ATMOSPHERE' : 99,
'BRIGHTNESS' : 100,
'GOBLINS' : 101,
'ECHO_DROPS' : 102,
'SCI_FI' : 103,
'SITAR' : 104,
'BANJO' : 105,
'SHAMISEN' : 106,
'KOTO' : 107,
'KALIMBA' : 108,
'BAGPIPE' : 109,
'FIDDLE' : 110,
'SHANNAI' : 111,
'BELL' : 112,
'AGOGO' : 113,
'STEEL_DRUMS' : 114,
'WOODBLOCK' : 115,
'TAIKO' : 116,
'TOM_TOM' : 117,
'SYNTH_DRUM' : 118,
'REVERSE_CYMBAL' : 119,
'GUITAR_FRET_NOISE' : 120,
'BREATH' : 121,
'SEA' : 122,
'BIRD' : 123,
'TELEPHONE' : 124,
'HELICOPTER' : 125,
'APPLAUSE' : 126,
'GUNSHOT' : 127}
rewriteRules = {'I': [(.07, ['I','I']), (.3, ['I','V']), (.33, ['I6', 'IV']), (.35, ['V7/IV', 'IV']), (.55, ['I','IV']), (.70, ['I','ii']), (.85, ['I','vi']), (.9, ['I','viio']), (.93, ['I6', 'iii']), (1.0, ['I','iii'])], 'ii': [(.03, ['ii6', 'V']), (.05, ['ii7', 'V']), (.55, ['ii','V']), (.58, ['ii6', 'IV']), (.85, ['ii','IV']), (.95, ['V/V','V']), (1.0, ['ii', 'viio'])], 'iii': [(.5, ['iii', 'vi']), (.9, ['iii', 'IV']), (1.0, ['V/vi', 'vi'])], 'IV': [(.03, ['IV6','V']), (.6, ['IV', 'V']), (.9, ['IV', 'I']), (.91, ['IV6', 'viio']), (.95, ['IV', 'viio']), (1.0, ['IV', 'ii'])], 'V': [(.04, ['V6', 'I']), (.5, ['V', 'I']), (.8, ['V', 'IV']), (.95, ['V', 'vi']), (1.0, ['V7', 'I'])], 'vi': [(.03, ['vi6', 'ii']), (.5, ['vi', 'ii']), (1.0, ['vi', 'IV'])], 'viio': [(.03, ['viio7', 'I']), (.7, ['viio6', 'I']), (1.0, ['viio', 'V'])]}
toOne = {('I','I'): [(.05, ['I64', 'V7', 'I']), (1.0, ['I64', 'V', 'I'])], ('ii', 'I'): [(.1, ['ii6', 'V', 'I']), (.15, ['ii', 'V7', 'I']), (1.0, ['ii', 'V', 'I'])], ('iii', 'I'): [(1.0, ['iii', 'IV', 'I'])], ('IV', 'I'): [(.05, ['IV', 'V7', 'I']), (.15, ['IV6', 'V', 'I']), (1.0, ['IV', 'V', 'I'])], ('V', 'I'): [(.2, ['V6', 'V', 'I']), (1.0, ['V', 'V7', 'I'])], ('vi', 'I'): [(.2, ['vi', 'V', 'I']), (1.0, ['vi', 'IV', 'I'])], ('viio', 'I'): [(1.0, ['viio', 'V7', 'I'])]}
rewriteRules.update(toOne)
toFive = {('I', 'V'): [(.5, ['I', 'IV', 'V']), (.9, ['I', 'ii', 'V']), (.95, ['I', 'ii6', 'V']), (1.0, ['I', 'V/V', 'V'])], ('ii', 'V'): [(.75, ['ii', 'IV', 'V']), (.85, ['ii', 'viio', 'V']), (.90, ['ii6', 'ii', 'V']), (.95, ['ii6', 'IV', 'V']), (1.0, ['ii', 'ii7', 'V'])], ('iii', 'V'): [(1.0, ['iii', 'IV', 'V'])], ('IV', 'V'): [(.65, ['IV', 'I', 'V']), (.90, ['IV', 'viio', 'V']), (1.0, ['IV', 'viio', 'V7'])], ('V', 'V'): [(.5, ['V', 'IV', 'V']), (.95, ['V', 'I', 'V']), (.98, ['V', 'ii', 'V']), (1.0, ['V', 'V/V', 'V'])], ('vi', 'V'): [(.5, ['vi', 'IV', 'V']), (.95, ['vi', 'ii', 'V']), (1.0, ['vi', 'ii6', 'V'])], ('viio', 'V'): [(1.0, ['viio', 'I', 'V'])], }
rewriteRules.update(toFive)
toSix = {('I', 'vi'): [(1.0, ['I', 'V', 'vi'])], ('ii', 'vi'): [(1.0, ['ii', 'V', 'vi'])], ('iii', 'vi'): [(1.0, ['iii', 'V/vi', 'vi'])], ('IV', 'vi'): [(1.0, ['IV', 'V', 'vi'])], ('V', 'vi'):[(1.0, ['V', 'V7', 'vi'])], ('vi', 'vi'):[(1.0, ['vi', 'V', 'vi'])], ('viio', 'vi'):[(1.0, ['viio', 'V7', 'vi'])]}
rewriteRules.update(toSix)
toFour = {('I', 'IV'):[(1.0, ['I', 'V', 'IV'])], ('ii', 'IV'):[(1.0, ['ii', 'V', 'IV'])], ('iii', 'IV'):[(.25, ['iii', 'iii7', 'IV']), (1.0, ['iii', 'vi', 'IV'])], ('IV', 'IV'):[(.3, ['IV', 'I', 'IV']), (1.0, ['IV', 'V', 'IV'])], ('V', 'IV'):[(1.0, ['V', 'I', 'IV'])], ('vi', 'IV'):[(.6, ['vi', 'ii', 'IV']), (1.0, ['vi', 'V', 'IV'])], ('viio', 'IV'):[(1.0, ['viio', 'viio', 'IV'])]}
rewriteRules.update(toFour)
def rewrite(chordList, length, rules, endChord, startChord = 'I'):
   #generates a sequence of chords starting at startChord and ending at endChord, following the prescribed rewrite rules
    chordList[0] = startChord
    if len(chordList) == length:
        return chordList
    if len(chordList) == length - 2:
        cadence = [chordList.pop()]
        cadence += [endChord]
        selection = random.random()
        chances = rewriteRules[tuple(cadence)]
        for c in chances:
            if c[0] > selection:
                cadence = c[1]
                break
        chordList += cadence
        chordList[0] = startChord
        return chordList
    else:
        startChord = chordList[0]
        selection = random.random()
        chances = rules[chordList.pop()]
        for c in chances:
            if c[0] > selection:
                return rewrite(chordList + c[1], length, rules, endChord, startChord)
class abstractNote:
   #an abstract representation of a note
   def __init__(self, number): #C is 0, B is 11
      self.value = number % 12
   def __repr__(self):
      catalogue = {0:'C', 1:'C#/Db', 2:'D', 3:'D#/Eb', 4:'E', 5:'F', 6:'F#/Gb', 7:'G', 8:'G#/Ab', 9:'A', 10:'A#/Bb', 11:'B'}
      return catalogue[self.value]
class Chord:
   #a chord is a combination of abstract notes, with an optional seventh note
    def __init__(self, first, third, fifth, seventh = None):
        self.first = first
        self.third = third
        self.fifth = fifth
        self.seventh = seventh
    def __repr__(self):
        return str([self.first, self.third, self.fifth])
class Key:
   #a key is a collection of chords, bound to a certain tonality
    def __init__(self, key, tonality = 'M'):
        self.key = abstractNote(key)
        if tonality == 'M':
           self.notes = {'one':abstractNote(key), 'two':abstractNote(key + 2), 'three':abstractNote(key + 4), 'four':abstractNote(key + 5), 'five':abstractNote(key + 7), 'six':abstractNote(key + 9), 'seven':abstractNote(key + 11)}
        elif tonality == 'm':
           self.notes = {'one':abstractNote(key), 'two':abstractNote(key + 2), 'three':abstractNote(key + 3), 'four':abstractNote(key + 5), 'five':abstractNote(key + 7), 'six':abstractNote(key + 8), 'seven':abstractNote(key + 10)}
        elif tonality == 'd':
           self.notes = {'one':abstractNote(key), 'two':abstractNote(key + 2), 'three':abstractNote(key + 3), 'four':abstractNote(key + 5), 'five':abstractNote(key + 7), 'six':abstractNote(key + 9), 'seven':abstractNote(key + 10)}
        elif tonality == 'p':
           self.notes = {'one':abstractNote(key), 'two':abstractNote(key + 1), 'three':abstractNote(key + 3), 'four':abstractNote(key + 5), 'five':abstractNote(key + 7), 'six':abstractNote(key + 8), 'seven':abstractNote(key + 10)}
        elif tonality == 'l':
           self.notes = {'one':abstractNote(key), 'two':abstractNote(key + 2), 'three':abstractNote(key + 4), 'four':abstractNote(key + 6), 'five':abstractNote(key + 7), 'six':abstractNote(key + 9), 'seven':abstractNote(key + 11)}
        elif tonality == 'mi':
           self.notes = {'one':abstractNote(key), 'two':abstractNote(key + 2), 'three':abstractNote(key + 4), 'four':abstractNote(key + 5), 'five':abstractNote(key + 7), 'six':abstractNote(key + 9), 'seven':abstractNote(key + 10)}
        elif tonality == 'lo':
           self.notes = {'one':abstractNote(key), 'two':abstractNote(key + 1), 'three':abstractNote(key + 3), 'four':abstractNote(key + 5), 'five':abstractNote(key + 6), 'six':abstractNote(key + 8), 'seven':abstractNote(key + 10)}
        elif tonality == 'ld':
           self.notes = {'one':abstractNote(key), 'two':abstractNote(key + 2), 'three':abstractNote(key + 4), 'four':abstractNote(key + 6), 'five':abstractNote(key + 7), 'six':abstractNote(key + 9), 'seven':abstractNote(key + 10)}
        elif tonality == 'pd':
           self.notes = {'one':abstractNote(key), 'two':abstractNote(key + 1), 'three':abstractNote(key + 4), 'four':abstractNote(key + 5), 'five':abstractNote(key + 7), 'six':abstractNote(key + 8), 'seven':abstractNote(key + 10)}
        elif tonality == 'mlo':
           self.notes = {'one':abstractNote(key), 'two':abstractNote(key + 2), 'three':abstractNote(key + 4), 'four':abstractNote(key + 5), 'five':abstractNote(key + 6), 'six':abstractNote(key + 8), 'seven':abstractNote(key + 10)}
        elif tonality == 'ud':
           self.notes = {'one':abstractNote(key), 'two':abstractNote(key + 2), 'three':abstractNote(key + 3), 'four':abstractNote(key + 6), 'five':abstractNote(key + 7), 'six':abstractNote(key + 9), 'seven':abstractNote(key + 10)}
        elif tonality == 'hm':
           self.notes = {'one':abstractNote(key), 'two':abstractNote(key + 2), 'three':abstractNote(key + 3), 'four':abstractNote(key + 6), 'five':abstractNote(key + 7), 'six':abstractNote(key + 8), 'seven':abstractNote(key + 11)}
        elif tonality == 'n':
           self.notes = {'one':abstractNote(key), 'two':abstractNote(key + 1), 'three':abstractNote(key + 3), 'four':abstractNote(key + 5), 'five':abstractNote(key + 7), 'six':abstractNote(key + 8), 'seven':abstractNote(key + 11)}
        self.chords = {'I':Chord(self.notes['one'], self.notes['three'], self.notes['five']), 'ii':Chord(self.notes['two'], self.notes['four'], self.notes['six']), 'iii':Chord(self.notes['three'], self.notes['five'], self.notes['seven']), 'IV':Chord(self.notes['four'], self.notes['six'], self.notes['one']), 'V':Chord(self.notes['five'], self.notes['seven'], self.notes['two']), 'vi':Chord(self.notes['six'], self.notes['one'], self.notes['three']), 'viio':Chord(self.notes['seven'], self.notes['two'], self.notes['four'])}
        if tonality == 'm':
         self.chords['V'] = Chord(self.notes['five'], abstractNote(self.notes['seven'].value + 1), self.notes['two'])
         self.chords['vii'] = Chord(abstractNote(self.notes['seven'].value + 1), self.notes['two'], self.notes['four'])
relativeRoman = {'I':0, 'ii':2, 'iii':'4', 'IV':5, 'V':7, 'vi':9, 'vii':11, 'viio':11}
def parseChord(chord, key): #takes a chord-string and a key and returns a CHORD OBJECT
   if "/" in chord:
      return parseChord(chord.split("/")[0], Key(key.key.value + relativeRoman[chord.split("/")[1]]))
   elif '64' in chord:
      return Chord(key.chords[chord.replace('64', '')].fifth, key.chords[chord.replace('64', '')].first, key.chords[chord.replace('64', '')].third)
   elif '6' in chord:
      return Chord(key.chords[chord.replace('6', '')].third, key.chords[chord.replace('6', '')].fifth, key.chords[chord.replace('6', '')].first)
   elif '7' in chord:
      return Chord(key.chords[chord.replace('7', '')].first, key.chords[chord.replace('7', '')].third, key.chords[chord.replace('7', '')].fifth, abstractNote(key.chords[chord.replace('7', '')].fifth.value + 3))
   else:
      return key.chords[chord]
def getPossibleBass(chordList, key): 
   #returns a list of possible notes for the bass
   bassRange = range(F2, B3)
   possibleBass = []
   for chord in chordList:
      abstractBass = parseChord(chord, key).first
      suitableNotes = []
      for i in bassRange:
         if i%12 is abstractBass.value:
            suitableNotes.append(i)
      possibleBass.append(suitableNotes)
   return possibleBass
def createBassLine(possibleBass, chordProgression):
   #creates the most conjunct bassline, given the possible bass notes.
   bassLine = []
   for p in range(len(possibleBass)):
      if len(possibleBass[p]) is 1:
         bassLine.append(possibleBass[p][0])
      else:
         if len(bassLine) is 0:
            bassLine.append(possibleBass[p][0])
         else:
            mostConjunct = (0, abs(bassLine[p - 1] - possibleBass[p][0]))
            for q in range(1, len(possibleBass[p])):
               if abs(bassLine[p - 1] - possibleBass[p][q]) < mostConjunct[1]:
                  mostConjunct = (q, abs(bassLine[p - 1] - possibleBass[p][q]))
            bassLine.append(possibleBass[p][mostConjunct[0]])
   return bassLine
def getPossibleNotes(chordList, key, noteRange):
   possibleNotes = []
   for chord in chordList:
      abstractSoprano = []
      parsedChord = parseChord(chord, key)
      abstractSoprano.append(parsedChord.first)
      abstractSoprano.append(parsedChord.third)
      abstractSoprano.append(parsedChord.fifth)
      if '7' in chord:
         abstractSoprano.append(parsedChord.seventh)
      suitableNotes = []
      for i in noteRange:
         for n in abstractSoprano:
            if i%12 is n.value:
               suitableNotes.append(i)
      possibleNotes.append(suitableNotes)
   return possibleNotes
def createSopranoLine(possibleSoprano, chordList, key, bassLine, conjunctivityPoints = {0:1, 1:0, 2:0, 3:1, 4:1, 5:3, 6:10, 7:3, 8:4, 9:5, 10:6, 11:7, 12:10, 13:10, 14:10, 15:10, 16:10, 17:10, 18:10, 19:10, 20:10}): #soprano only needs to check for parallel motion with the bass
   sopranoLine = []
   for p in range(len(possibleSoprano)):
      if p == 0:
         sopranoLine.append(random.choice(possibleSoprano[0][1:len(possibleSoprano[0]) - 1]))
      else:
         scores = []
         for i in possibleSoprano[p]:
            scores.append(conjunctivityPoints[abs(sopranoLine[p-1] - i)])
         bestNote = possibleSoprano[p][scores.index(min(scores))]
         while (abs(bassLine[p] - bassLine[p-1]) == 7 and abs(bestNote - sopranoLine[p-1]) == 7):
            scores[scores.index[min(scores)]] = 100
            bestNote = possibleSoprano[p][scores.index(min(scores))]
         sopranoLine.append(bestNote)
   return sopranoLine
def createAltoLine(possibleAlto, chordList, key, bassLine, sopranoLine):
   altoLine = []
   conjunctivityPoints = {0:0, 1:0, 2:0, 3:1, 4:1, 5:3, 6:10, 7:3, 8:4, 9:5, 10:6, 11:7, 12:10, 13:10, 14:10, 15:10, 16:10, 17:10, 18:10, 19:10, 20:10}
   for p in range(len(possibleAlto)):
      if p == 0:
         altoLine.append(random.choice(filter(lambda x: x < sopranoLine[0], possibleAlto[0])))
      else:
         scores = []
         for i in possibleAlto[p]:
            score = conjunctivityPoints[abs(altoLine[p-1] - i)]
            if sopranoLine[p] - i > 12:
               score += 2
            if i > sopranoLine[p]:
               score += 10
            if (abs(bassLine[p] - bassLine[p-1]) == 7 or abs(sopranoLine[p] - sopranoLine[p-1]) == 7) and abs(i - altoLine[p-1]) == 7:
               score += 7
            if i == parseChord(chordList[p], key).fifth.value and sopranoLine[p] == parseChord(chordList[p], key).fifth.value:
               score += 2
            if i == parseChord(chordList[p], key).third.value and sopranoLine[p] == parseChord(chordList[p], key).third.value:
               score += 4
            if i == parseChord(chordList[p], key).first.value and sopranoLine[p] == parseChord(chordList[p], key).first.value:
               score += 3
            scores.append(score)
         bestNote = possibleAlto[p][scores.index(min(scores))]
         altoLine.append(bestNote)
   return altoLine
def createTenorLine(possibleTenor, chordList, key, bassLine, sopranoLine, altoLine):
   tenorLine = []
   conjunctivityPoints = {0:0, 1:0, 2:0, 3:1, 4:1, 5:3, 6:10, 7:3, 8:4, 9:5, 10:6, 11:7, 12:10, 13:10, 14:10, 15:10, 16:10, 17:10, 18:10, 19:10, 20:10}
   for p in range(len(possibleTenor)):
      if p == 0:
         try:
            tenorLine.append(random.choice(filter(lambda x: x < altoLine[0], possibleTenor[0])))
         except IndexError:
            tenorLine.append(min(possibleTenor[0]))
      else:
         scores = []
         for i in possibleTenor[p]:
            score = conjunctivityPoints[abs(tenorLine[p-1] - i)]
            if i > altoLine[p]:
               score += 6
            if i == altoLine[p]:
               score += 5
            if (abs(bassLine[p] - bassLine[p-1]) == 7 or abs(sopranoLine[p] - sopranoLine[p-1]) == 7 or abs(altoLine[p] - altoLine[p-1]) == 7) and abs(i - tenorLine[p-1]) == 7:
               score += 7
            if (sopranoLine[p] == parseChord(chordList[p], key).first.value and altoLine[p] == parseChord(chordList[p], key).third.value) or (sopranoLine[p] == parseChord(chordList[p], key).third.value and altoLine[p] == parseChord(chordList[p], key).first.value):
               if i == parseChord(chordList[p], key).fifth.value:
                  score -= 5
            if (sopranoLine[p] == parseChord(chordList[p], key).first.value and altoLine[p] == parseChord(chordList[p], key).fifth.value) or (sopranoLine[p] == parseChord(chordList[p], key).fifth.value and altoLine[p] == parseChord(chordList[p], key).first.value):
               if i == parseChord(chordList[p], key).third.value:
                  score -= 5
            if (sopranoLine[p] == parseChord(chordList[p], key).fifth.value and altoLine[p] == parseChord(chordList[p], key).third.value) or (sopranoLine[p] == parseChord(chordList[p], key).third.value and altoLine[p] == parseChord(chordList[p], key).fifth.value):
               if i == parseChord(chordList[p], key).first.value:
                  score -= 10
            scores.append(score)
         bestNote = possibleTenor[p][scores.index(min(scores))]
         tenorLine.append(bestNote)
   return tenorLine
def getValue(note):
   return note.value
def elaborate(line, rhythm, key, frequency):
   for i in range(len(line) - 2):
      if line[i+1] - line[i] == 4 or line[i+1] - line[i] == 3:
         if random.random() < frequency * .85:
            line.insert(i + 1, line[i] + 2 if (line[i] + 2)%12 in map(getValue, key.notes.values()) else line[i] + 1)
            rhythm[i] = rhythm[i]/2
            rhythm.insert(i + 1, rhythm[i])
      if line[i] - line[i+1] == 4 or line[i+1] - line[i] == 3:
         if random.random() < frequency:
            line.insert(i + 1, line[i] - 2 if (line[i] - 2)%12 in map(getValue, key.notes.values()) else line[i] - 1)
            rhythm[i] = rhythm[i]/2
            rhythm.insert(i + 1, rhythm[i])
      if line[i] == line[i+1] and line[i+2] <= line[i+1]:
         if random.random() < frequency * .85:
            rhythm[i] = rhythm[i]/2
            rhythm.insert(i + 1, rhythm[i])
            line.insert(i + 1, line[i] + 2 if (line[i] + 2)%12 in map(getValue, key.notes.values()) else line[i] + 1)
      if line[i] == line[i+1] and line[i+2] > line[i+1]:
         if random.random() < frequency * .85:
            rhythm[i] = rhythm[i]/2
            rhythm.insert(i + 1, rhythm[i])
            line.insert(i + 1, line[i] - 2 if (line[i] - 2)%12 in map(getValue, key.notes.values()) else line[i] - 1)
def makeMusic(key = Key(random.choice(range(0, 11)), random.choice(['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'd', 'l', 'mi'])), cheeseLevel = .8, soprano = FLUTE, alto = TRUMPET, tenor = HORN, bass = CONTRABASS):
   TIMESIGNATURE = random.choice(['4/4'])
   THEKEY = key #'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'd', 'l', 'mi'
   sopranoRange = range(C4, G5)
   altoRange = range(G3, C5)
   tenorRange = range(C3, G4)
   if TIMESIGNATURE == '4/4':
      chords1 = rewrite(['I'], 8, rewriteRules, 'V')
      chords2 = rewrite(['I'], 7, rewriteRules, 'I')
      chords3 = rewrite(['V'], 8, rewriteRules, random.choice(['vi', 'vi', 'V', 'IV']), 'V')
      chords4 = rewrite(['I'], 7, rewriteRules, 'I')
   chordProgression = chords1 + chords2 + chords3 + chords4
   if TIMESIGNATURE == '4/4':
     bassPhraseDuration = [QN, QN, QN, QN, QN, QN, QN, QN] + [QN, QN, QN, QN, QN, QN, HN] + [QN, QN, QN, QN, QN, QN, QN, QN] + [QN, QN, QN, QN, QN, QN, HN]
     sopranoPhraseDuration = [QN, QN, QN, QN, QN, QN, QN, QN] + [QN, QN, QN, QN, QN, QN, HN] + [QN, QN, QN, QN, QN, QN, QN, QN] + [QN, QN, QN, QN, QN, QN, HN]
     altoPhraseDuration = [QN, QN, QN, QN, QN, QN, QN, QN] + [QN, QN, QN, QN, QN, QN, HN] + [QN, QN, QN, QN, QN, QN, QN, QN] + [QN, QN, QN, QN, QN, QN, HN]
     tenorPhraseDuration = [QN, QN, QN, QN, QN, QN, QN, QN] + [QN, QN, QN, QN, QN, QN, HN] + [QN, QN, QN, QN, QN, QN, QN, QN] + [QN, QN, QN, QN, QN, QN, HN]
   score = Score('Random Piece', 60)
   possibleBass = getPossibleBass(chordProgression, THEKEY)
   bassLine = createBassLine(possibleBass, chordProgression)
   possibleSoprano = getPossibleNotes(chordProgression, THEKEY, sopranoRange)
   sopranoLine = createSopranoLine(possibleSoprano, chordProgression, THEKEY, bassLine)
   possibleAlto = getPossibleNotes(chordProgression, THEKEY, altoRange)
   altoLine = createAltoLine(possibleAlto, chordProgression, THEKEY, bassLine, sopranoLine)
   possibleTenor = getPossibleNotes(chordProgression, THEKEY, tenorRange)
   tenorLine = createTenorLine(possibleAlto, chordProgression, THEKEY, bassLine, sopranoLine, altoLine)
   elaborate(sopranoLine, sopranoPhraseDuration, THEKEY, cheeseLevel)
   elaborate(altoLine, altoPhraseDuration, THEKEY, cheeseLevel)
   elaborate(tenorLine, tenorPhraseDuration, THEKEY, cheeseLevel)
   bassPhrase = Phrase()
   bassPhrase.addNoteList(bassLine, bassPhraseDuration)
   bassPart = Part(bass, 0)
   bassPart.add(bassPhrase)
   score.add(bassPart)
   sopranoPhrase = Phrase()
   sopranoPhrase.addNoteList(sopranoLine, sopranoPhraseDuration)
   for note in sopranoPhrase.getNoteList():
      note.setDynamic(F)
   sopranoPart = Part(soprano, 1)
   sopranoPart.add(sopranoPhrase)
   score.add(sopranoPart)
   altoPhrase = Phrase()
   altoPhrase.addNoteList(altoLine, altoPhraseDuration)
   for note in altoPhrase.getNoteList():
      note.setDynamic(MF)
   altoPart = Part(alto, 2)
   altoPart.add(altoPhrase)
   score.add(altoPart)
   tenorPhrase = Phrase()
   tenorPhrase.addNoteList(tenorLine, tenorPhraseDuration)
   tenorPart = Part(tenor, 3)
   tenorPart.add(tenorPhrase)
   score.add(tenorPart)
   Write.midi(score, 'Randomly Generated Chorale.mid')
   Play.midi(score)
class MusicMaker(JFrame):
    keyRoot = 0
    tonality = 'M'
    cheeseFactor = .5
    soprano = FLUTE
    alto = TRUMPET
    tenor = HORN
    bass = CONTRABASS
    def __init__(self):
        super(MusicMaker, self).__init__()
        self.initUI()
    def initUI(self):
        layout = GroupLayout(self.getContentPane())
        self.getContentPane().setLayout(layout)
        layout.setAutoCreateGaps(True)
        layout.setAutoCreateContainerGaps(True)
        self.setPreferredSize(Dimension(800, 500))
        windows = JLabel("Options")
        keyList = JList(['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B'], valueChanged=self.changeKeyRoot)
        tonalityList = JList(['Major', 'Minor', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Locrian', 'Lydian Dominant', 'Phrygian Dominant', 'Major Locrian', 'Ukrainian Dorian', 'Hungarian Minor', 'Neapolitan'], valueChanged=self.changeTonality)
        cheeseList = JList(['Homorhythmic', 'A Little Motion', 'Standard', 'Really Moving', 'Dangerously Cheesy'], valueChanged=self.changeCheese)
        sopranoList = JList(['SOPRANO'] + INSTRUMENTS.keys(), valueChanged=self.changeSoprano)
        altoList = JList(['ALTO'] + INSTRUMENTS.keys(), valueChanged=self.changeAlto)
        tenorList = JList(['TENOR'] + INSTRUMENTS.keys(), valueChanged=self.changeTenor)
        bassList = JList(['BASS'] + INSTRUMENTS.keys(), valueChanged=self.changeBass)
        area = JPanel()
        scrollList1 = JScrollPane()
        scrollList1.getViewport().add(keyList)
        scrollList2 = JScrollPane()
        scrollList2.getViewport().add(tonalityList)
        scrollList3 = JScrollPane()
        scrollList3.getViewport().add(cheeseList)
        scrollList4 = JScrollPane()
        scrollList4.getViewport().add(sopranoList)
        scrollList5 = JScrollPane()
        scrollList5.getViewport().add(altoList)
        scrollList6 = JScrollPane()
        scrollList6.getViewport().add(tenorList)
        scrollList7 = JScrollPane()
        scrollList7.getViewport().add(bassList)
        scrollList1.setVisible(True)
        area.add(scrollList1)
        area.add(scrollList2)
        area.add(scrollList3)
        area.add(scrollList4)
        area.add(scrollList5)
        area.add(scrollList6)
        area.add(scrollList7)
        def help(e):
          JOptionPane.showMessageDialog(area, "Choose the options you want, or use randomize!",
             "Help", JOptionPane.INFORMATION_MESSAGE)
        area.setBorder(BorderFactory.createLineBorder(Color.gray))
        activate = JButton("Make Music", actionPerformed= self.createSong )
        def close(e):
           sys.exit(0)
        close = JButton("Close", actionPerformed = close)
        help = JButton("Help", actionPerformed = help)
        ok = JButton("Randomize Choices", actionPerformed=self.randomSong)
        layout.setHorizontalGroup(layout.createSequentialGroup()
            .addGroup(layout.createParallelGroup()
                .addComponent(windows)
                .addComponent(area)
                .addComponent(help))
            .addGroup(layout.createParallelGroup()
                .addComponent(activate)
                .addComponent(close)
                .addComponent(ok))
        )
        layout.setVerticalGroup(layout.createSequentialGroup()
            .addComponent(windows)
            .addGroup(layout.createParallelGroup()
                .addComponent(area)
                .addGroup(layout.createSequentialGroup()
                    .addComponent(activate)
                    .addComponent(close)))
            .addGroup(layout.createParallelGroup()
                .addComponent(help)
                .addComponent(ok))
        )
        layout.linkSize(SwingConstants.HORIZONTAL, [ok, help, close, activate])
        self.pack()
        self.setTitle("Tonal Music Generator")
        self.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
        self.setLocationRelativeTo(None)
        self.setVisible(True)
    def changeKeyRoot(self, e):
           sender = e.getSource()
           if not e.getValueIsAdjusting():
              name = sender.getSelectedValue()
              catalogue = {'C':0, 'C#/Db':1, 'D':2, 'D#/Eb':3, 'E':4, 'F':5, 'F#/Gb':6, 'G':7, 'G#/Ab':8, 'A':9, 'A#/Bb':10, 'B':11}
              self.keyRoot = catalogue[name]
    def changeTonality(self, e):
           sender = e.getSource()
           if not e.getValueIsAdjusting():
              name = sender.getSelectedValue()
              catalogue = {'Major':'M', 'Minor':'m', 'Dorian':'d', 'Phrygian':'p', 'Lydian':'l', 'Mixolydian':'mi', 'Locrian':'lo', 'Lydian Dominant':'ld', 'Phrygian Dominant':'pd', 'Major Locrian':'mlo', 'Ukrainian Dorian':'ud', 'Hungarian Minor':'hm', 'Neapolitan':'n'}
              self.tonality = catalogue[name]
    def changeCheese(self, e):
           sender = e.getSource()
           if not e.getValueIsAdjusting():
              name = sender.getSelectedValue()
              catalogue = {'Homorhythmic':0, 'A Little Motion':.3, 'Standard':.6, 'Really Moving':.8, 'Dangerously Cheesy':1.5}
              self.cheeseFactor = catalogue[name]
    def changeSoprano(self, e):
           sender = e.getSource()
           if not e.getValueIsAdjusting():
              name = sender.getSelectedValue()
              self.soprano = INSTRUMENTS[name]
    def changeAlto(self, e):
           sender = e.getSource()
           if not e.getValueIsAdjusting():
              name = sender.getSelectedValue()
              self.alto = INSTRUMENTS[name]
    def changeTenor(self, e):
           sender = e.getSource()
           if not e.getValueIsAdjusting():
              name = sender.getSelectedValue()
              self.tenor = INSTRUMENTS[name]
    def changeBass(self, e):
           sender = e.getSource()
           if not e.getValueIsAdjusting():
              name = sender.getSelectedValue()
              self.bass = INSTRUMENTS[name]
    def randomSong(event, idk):
       makeMusic()
    def createSong(self, event):
       makeMusic(Key(self.keyRoot, self.tonality), self.cheeseFactor, self.soprano, self.alto, self.tenor, self.bass)
if __name__ == '__main__':
    MusicMaker()
