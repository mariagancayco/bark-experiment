from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav


def main():
    # Preload the models
    preload_models()

    text_prompt = (
        "Hello! This is an example of generating audio using the Bark model. "
        "The Bark model can create realistic speech and other audio such as music, noise and effects."
    )

    # Generate audio from the text
    audio_array = generate_audio(text_prompt)

    # Save audio to disk
    write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)


if __name__ == "__main__":
    main()
