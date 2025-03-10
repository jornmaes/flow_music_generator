from pydub import AudioSegment
import numpy as np
import soundfile as sf
import random


#load some drum samples from the internet
kick = AudioSegment.from_file("drum_kick.wav") - 25
snare = AudioSegment.from_file("drum_snare.wav") - 25
hihat = AudioSegment.from_file("hihat.wav") - 20



#define in beats per minute
tempo = 60 #60 seems better
beat_length = 60000 / tempo # this is the length of each beat in ms

#create a basic loop pattern: kick on 0, snare on 2, hihat on 1
def create_drum_loop():
    drum_loop = AudioSegment.empty()
    for i in range(16): #16 beats in a 4/4 loop
        if i % 4 == 0: #kick on 1, 5, 9, 13
            drum_loop += kick + random.randint(-3, 3)
        elif i % 4 == 2:
            drum_loop += snare + random.randint(-3, 3)
        elif i % 4 == 1:
            drum_loop += hihat + random.randint(-3, 3)
        else:
            drum_loop += AudioSegment.silent(duration= beat_length) # remain silent on the other beats

    return drum_loop

#create and export the loop
drum_loop = create_drum_loop()
drum_loop.export("drum_loop.wav", format="wav")


#define some basic notes (A4, C5, D5, etc) -> i got this from some music teaching website
notes = {
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "B4": 493.88,
    "C5": 523.25
}

#generate a sine wave for a note
def generate_note(frequency, duration = 0.5, sample_rate = 44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint= False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t) #formula for sine wave
    return wave

#now we create a random melody by choosing random notes
def create_melody(length = 8, scale = notes):
    melody = []
    for _ in range(length):
        note = random.choice(list(scale.values())) # this will pick a random note out of our collection
        melody.append(generate_note(note))

    #now we concatenate the notes into a single melody
    melody_conc = np.concatenate(melody)
    return melody_conc


#lets test this by crzating a melody and saving it as a wav
melody = create_melody()
sf.write("melody.wav", melody, 44100)

#lets try this with chords -> also found on that teaching site
#now with jazz-inspired 7th chords
chords = {
    "Cmaj7": [261.63, 329.63, 329.00, 493.88],
    "Am7": [220.00, 261.63, 329.63, 415.30],
    "Fmaj7": [349.23, 440.00, 523.25, 698.46],
    "G7": [392.00, 493.88, 587.33, 698.46],
    "Dm7": [293.66, 349.23, 440.00, 554.37],
    "Em7": [329.63, 411.73, 523.25, 622.25],
    "Bm7b5": [246.94, 311.13, 391.99, 493.88],
    "E7": [329.63, 415.30, 523.25, 698.46],
    "Abmaj7": [415.30, 523.25, 622.25, 830.51],
    "Bb7": [466.16, 622.25, 739.99, 987.77],
    'Cm7': [261.63, 311.13, 392.00, 466.16],
    "Gm7": [196.00, 233.08, 293.66, 349.23]
}

chord_sequences = {
    1: ["Cmaj7", "Am7", "Fmaj7", "G7"], #standard
    2: ["Cmaj7", "Dm7", "Em7", "Am7"], #smooth
    3: ["Cmaj7", "Fmaj7", "G7", "Em7"], #open
    4: ["Cmaj7", "Bm7b5", "E7", "Am7"], #darker
    5: ["Am7", "Dm7", "G7", "Cmaj7"], #relaxed
    6: ["Fmaj7", "Cmaj7", "Em7", "Am7"], #open
    7: ["Cm7", "Abmaj7", "Bb7", "Gm7"], #melancholic
    8: ["Am7", "G7", "Cmaj7", "Fmaj7"], #jazz
    9: ["Cmaj7", "Em7", "Dm7", "G7"], #movement
    10: ["Cm7", "G7", "Abmaj7", "G7"] #sophisticated
}

def generate_chord_sequence():
    sequence = []

    num_sequences = 50

    sequences = [random.choice(range(1,11)) for _ in range(num_sequences)]
    print(sequences)

    for sequence_num in sequences:
        
        for chord_name in chord_sequences[sequence_num]:
            #chord_choice = random.choice(chord_sequence)
            #frequencies = chords[chord_choice]

            frequencies = chords[chord_name]

            #add a chance for a chord to be inverted to keep it more fresh
            if random.random() < 0.2: #a 20% chance to be inverted
                frequencies = frequencies[1:] + frequencies[:1]
            chord = np.sum([generate_note(frequency, duration=2.0) for frequency in frequencies], axis=0)

            sequence.append(chord)

    """
    for chord_name in chord_sequence:
        frequencies = chords[chord_name]
        chord = np.sum([generate_note(frequency, duration=2.0) for frequency in frequencies], axis=0)
        sequence.append(chord)
    """


    return np.concatenate(sequence)

chords_melody = generate_chord_sequence()
sf.write("melody_with_chords.wav", chords_melody, 44100)





#combine the melody and the drum:

#melody_audio = AudioSegment.from_file("melody.wav")
melody_audio = AudioSegment.from_file("melody_with_chords.wav")

drum_loop = AudioSegment.from_file("drum_loop.wav")

vinyl_cracking_sound = AudioSegment.from_file("vinyl_cracking.wav") - 10



#we have to make sure the tracks have the same length (so we repeat the one thats shorter)
if len(drum_loop) < len(melody_audio):
    drum_loop = drum_loop * (len(melody_audio) // len(drum_loop) + 1)
    vinyl_cracking_sound = vinyl_cracking_sound * (len(melody_audio) // len(vinyl_cracking_sound) + 1)
else:
    melody_audio = melody_audio * (len(drum_loop) // len(melody_audio) + 1)
    vinyl_cracking_sound = vinyl_cracking_sound * (len(drum_loop) // len(vinyl_cracking_sound) + 1)




#combine them using .overlay
combined_audio = drum_loop.overlay(melody_audio)
combined_audio = combined_audio.overlay(vinyl_cracking_sound)

#export the final track
combined_audio.export("final_beat.wav", format = "wav")


def add_reverb(audio, reverb_level = 25):
    return audio.low_pass_filter(reverb_level)

melody_with_reverb = add_reverb(melody_audio)


combined_with_reverb = drum_loop.overlay(melody_with_reverb)
combined_with_reverb = combined_with_reverb.overlay(vinyl_cracking_sound)

combined_with_reverb.export("final_beat_with_reverb.wav", format = "wav")





















