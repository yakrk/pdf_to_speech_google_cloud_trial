# import packages
import fitz
from google.cloud import texttospeech

def main():
    # get pdf path
    pdf_path = "sample.pdf"
    all_texts = ""

    # get text from pdf
    with fitz.open (pdf_path) as pdf:
        for i in range(len(pdf)):
            pdf_text = pdf.get_page_text(i)
            all_texts = all_texts + pdf_text


    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    # synthesis_input = texttospeech.SynthesisInput(text=all_texts)
    synthesis_input = texttospeech.SynthesisInput(ssml=all_texts)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    lang_code = "ja-JP"
    name = "ja-JP-Wavenet-B"
    voice = texttospeech.VoiceSelectionParams(
        language_code=lang_code, ssml_gender=texttospeech.SsmlVoiceGender.FEMALE, name=name
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    
    filename = "output.mp3"
    # The response's audio_content is binary.
    with open(filename, "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "{filename}"')



if __name__ == "__main__":
    main()