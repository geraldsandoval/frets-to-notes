import pytest
import sys

def EString(fret):
    EStringNotes = ["E","F","F#/Gb","G","G#/Ab","A","A#/Bb","B","C","C#/Db","D","D#/Eb",
        "E","F","F#/Gb","G","G#/Ab","A","A#/Bb","B","C","C#/Db","D","D#/Eb"]
    if fret != "-":
        fret = EStringNotes[int(fret)]
    return fret

def test_E_string_notes():
    assert EString(0) == "E"
    assert EString(13) == "F"

def AString(fret):
    AStringNotes = ["A","A#/Bb","B","C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab",
        "A","A#/Bb","B","C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab"]
    if fret != "-":
        fret = AStringNotes[int(fret)]
    return fret

def test_A_string_notes():
    assert AString(0) == "A"
    assert AString(13) == "A#/Bb"

def DString(fret):
    DStringNotes = ["D","D#/Eb","E","F","F#/Gb","G","G#/Ab","A","A#/Bb","B","C","C#/Db",
        "D","D#/Eb","E","F","F#/Gb","G","G#/Ab","A","A#/Bb","B","C","C#/Db"]
    if fret != "-":
        fret = DStringNotes[int(fret)]
    return fret

def test_D_string_notes():
    assert DString(0) == "D"
    assert DString(13) == "D#/Eb"

def GString(fret):
    GStringNotes = ["G","G#/Ab","A","A#/Bb","B","C","C#/Db","D","D#/Eb","E","F","F#/Gb",
        "G","G#/Ab","A","A#/Bb","B","C","C#/Db","D","D#/Eb","E","F","F#/Gb"]
    if fret != "-":
        fret = GStringNotes[int(fret)]
    return fret

def test_G_string_notes():
    assert GString(0) == "G"
    assert GString(13) == "G#/Ab"

def BString(fret):
    BStringNotes = ["B","C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab","A","A#/Bb",
        "B","C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab","A","A#/Bb"]
    if fret != "-":
        fret = BStringNotes[int(fret)]
    return fret

def test_B_string_notes():
    assert BString(0) == "B"
    assert BString(13) == "C"

def eString(fret):
    return EString(fret)

def test_e_string_notes():
    assert eString(0) == "E"
    assert eString(13) == "F"

def frets_to_notes():
    return (EString(sys.argv[1]) + " " + AString(sys.argv[2]) + " " + DString(sys.argv[3]) + 
        " " + GString(sys.argv[4]) + " " + BString(sys.argv[5]) + " " + eString(sys.argv[6]))
            
def test_frets_to_notes():
    sys.argv = ["","-","2","4","4","3","-"]
    assert frets_to_notes() == "- B F#/Gb B D -"

def main():
    print(frets_to_notes())

##########################

if __name__ == '__main__':
    main()

