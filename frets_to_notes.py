import pytest
import sys


def process_fret(string, fret):
    try:
        note = string[int(fret) % 12]
    except ValueError: 
        note = "-"
    finally:
        return note


def return_chromatic_scale(root_note):
    a_chromatic = ["A","A#/Bb","B","C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab"]
    return a_chromatic[root_note:] + a_chromatic[0:root_note - 1]


def get_e_string_note(fret):
    return process_fret(return_chromatic_scale(7), fret)
        

def test_e_string_notes():
    assert get_e_string_note(0) == "E"
    assert get_e_string_note(13) == "F"


def get_a_string_note(fret):
    return process_fret(return_chromatic_scale(0), fret)


def test_a_string_notes():
    assert get_a_string_note(0) == "A"
    assert get_a_string_note(13) == "A#/Bb"


def get_d_string_note(fret):
    return process_fret(return_chromatic_scale(5), fret)


def test_d_string_notes():
    assert get_d_string_note(0) == "D"
    assert get_d_string_note(13) == "D#/Eb"


def get_g_string_note(fret):
    return process_fret(return_chromatic_scale(10), fret)


def test_g_string_notes():
    assert get_g_string_note(0) == "G"
    assert get_g_string_note(13) == "G#/Ab"


def get_b_string_note(fret):
    return process_fret(return_chromatic_scale(2), fret)


def test_b_string_notes():
    assert get_b_string_note(0) == "B"
    assert get_b_string_note(13) == "C"


def frets_to_notes():
    try:
        return (get_e_string_note(sys.argv[1]) + " " + get_a_string_note(sys.argv[2]) + " " + get_d_string_note(sys.argv[3]) + 
              " " + get_g_string_note(sys.argv[4]) + " " + get_b_string_note(sys.argv[5]) + " " + get_e_string_note(sys.argv[6]))
    except IndexError:
        print("Must provide a fret value for each string.")
            

def test_frets_to_notes():
    sys.argv = ["","-","2","4","4","3","-"]
    assert frets_to_notes() == "- B F#/Gb B D -"


def main():
    frets_to_notes()


##########################

if __name__ == '__main__':
    main()

