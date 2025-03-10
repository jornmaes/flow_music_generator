# Flow Music Generator

## Challenge Explanation

For my **Daily Coding Challenge**, the goal was to create a small project each day to improve my coding skills, learn new concepts, and explore various technologies. For one of these challenges, I decided to create a program that automatically generates **lofi beats**—chilled-out instrumental tracks perfect for studying, relaxation, and focus. The idea was to combine random **melodies**, **chord progressions**, and **drum loops** to create a unique lofi experience every time the program is run.

This project is intended to not only showcase my ability to code but also create a useful tool that could be used for personal relaxation, background music, or even as a starting point for a YouTube channel focused on relaxing music.

## Project Description

### Flow Music Generator

The **Flow Music Generator** is a Python-based program that generates a relaxing **lofi music track** by randomly combining various elements:

- **Randomly generated chord progressions**: Using a combination of major, minor, and seventh chords in jazz-inspired progressions.
- **Generated melodies**: Chord notes are used to create simple, smooth melodies that complement the generated chord progression.
- **Drum loops**: A basic drum kit is used to add rhythm and variation, with randomized kick, snare, and hi-hat patterns.
- **Effects**: Basic reverb is added to the melody and drums to achieve a more **warm, atmospheric** sound.

This project automatically generates an entire lofi beat, which is then exported as a `.wav` file that can be played or uploaded to platforms like YouTube.

## Software Used

### Programming Languages and Libraries

- **Python** (main language)
- **Libraries**:
  - **`numpy`**: For numerical operations and creating sound waves.
  - **`pydub`**: To process and manipulate audio, including adding reverb and exporting the final track as a `.wav` file.
  - **`soundfile`**: For exporting audio in various formats.
  - **`random`**: To generate random chord progressions, melodies, and rhythm patterns, making the output unique each time.

### External Tools

- **FFmpeg**: Required for `pydub` to export audio files as `.wav` format.
- **Drum Samples**: Various **kick**, **snare**, and **hi-hat** sounds (which can be replaced or expanded as needed).

## Implementation

### Project Breakdown

1. **Chord Progressions and Melody Generation**:
   - I created a library of common **chords** (e.g., Cmaj7, Am7, Dm7, G7) using predefined **frequencies**.
   - The program randomly selects a chord progression from this library and uses the **notes of each chord** to build a **melody** by generating simple **arpeggios** or **randomized note sequences** within the chords.
   
2. **Drum Loop Generation**:
   - Drum loops are created using **sample sounds** (kick, snare, hi-hat) with slight variations in timing to simulate a more natural, human-like performance.
   - Randomness is added to the loops so they don’t sound repetitive, but they maintain a consistent, laid-back rhythm typical of lofi music.

3. **Effects and Mixing**:
   - I added **reverb** effects to both the **melody** and **drum loops** to create a more **smooth** and **atmospheric** sound.
   - The melody and drum loops are then combined and mixed together.

4. **Exporting the Track**:
   - Once the audio is generated and mixed, it is exported as a `.wav` file, which can then be played or shared.

### Key Features

- **Randomized melody and chord progression** to ensure every track is unique.
- **Simple drum loop generation** with some variation in the rhythm to simulate a live, human feel.
- **Reverb and sound manipulation** to create a warm, atmospheric lofi vibe.
- **Exportable audio file** for easy listening and sharing.


## License

This project is open-source and licensed under the **MIT License**. Feel free to contribute, improve, and modify the project as needed.
