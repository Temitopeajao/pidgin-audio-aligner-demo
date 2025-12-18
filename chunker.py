 audio_chunker.py
from pydub import AudioSegment
from pydub.silence import split_on_silence

def chunk_pidgin_audio(file_path, min_silence_len=500, silence_thresh=-40):
    """
    Splits Nigerian Pidgin audio into training-ready chunks.
    Adjusted for rapid code-switching cadences (shorter pauses).
    """
    audio = AudioSegment.from_wav(file_path)
    chunks = split_on_silence(
        audio, 
        min_silence_len=min_silence_len, 
        silence_thresh=silence_thresh
    )
    
    # Export logic here...
    print(f"Split into {len(chunks)} segments suitable for ASR training.")

# NOTE: This is a demo implementation of the pipeline used for N-ATLAS.
