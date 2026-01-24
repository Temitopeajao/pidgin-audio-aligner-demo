import json
from datetime import datetime, timedelta

# PROJECT: Audio-Text Alignment & Segmentation Tool
# AUTHOR: Temitope Ajao
# PURPOSE: To process raw ASR timestamps, validate segment duration, 
# and generate a clean 'manifest.jsonl' file for training Audio LLMs.

class PidginAligner:
    def __init__(self, min_duration=1.0, max_duration=30.0):
        """
        Configuration for the training pipeline.
        - Segments < 1s are usually noise/clicks.
        - Segments > 30s can cause OOM (Out of Memory) errors during training.
        """
        self.min_duration = min_duration
        self.max_duration = max_duration
        self.discarded_count = 0

    def time_to_seconds(self, timestamp_str):
        """
        Converts SRT-style timestamps (e.g., "00:00:01.500") to float seconds.
        """
        try:
            # Normalize comma/dot separators
            timestamp_str = timestamp_str.replace(',', '.')
            t = datetime.strptime(timestamp_str, "%H:%M:%S.%f")
            delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second, microseconds=t.microsecond)
            return delta.total_seconds()
        except ValueError:
            return 0.0

    def validate_segment(self, start, end, text):
        """
        Quality Control Gate:
        1. Checks if duration is within training bounds.
        2. Filters out empty text or explicit noise tags.
        """
        duration = end - start
        
        if duration < self.min_duration:
            return False, "Too Short (<1s)"
        if duration > self.max_duration:
            return False, "Too Long (>30s)"
        
        # Filter out common noise tokens found in raw ASR data
        noise_tokens = ["[silence]", "[noise]", "[music]", "[laughter]"]
        if not text.strip() or text.lower() in noise_tokens:
            return False, "Empty/Noise Artifact"
            
        return True, "Valid"

    def process_manifest(self, raw_data):
        """
        The Core Pipeline.
        Input: List of raw segments (mock ASR output).
        Output: Clean JSONL manifest for training.
        """
        training_manifest = []
        
        print(f"--- PROCESSING {len(raw_data)} RAW SEGMENTS ---")

        for segment in raw_data:
            start_sec = self.time_to_seconds(segment['start_time'])
            end_sec = self.time_to_seconds(segment['end_time'])
            text = segment['transcript']
            
            is_valid, reason = self.validate_segment(start_sec, end_sec, text)
            
            if is_valid:
                # Standard format for NeMo / HuggingFace datasets
                entry = {
                    "audio_filepath": segment['file_name'],
                    "duration": round(end_sec - start_sec, 2),
                    "offset": start_sec,
                    "text": text,
                    "lang": "pcm"  # ISO code for Nigerian Pidgin
                }
                training_manifest.append(entry)
            else:
                self.discarded_count += 1
                # Log edge cases for review
                print(f"⚠️ Discarding ID {segment['id']}: {reason} | Text: '{text}'")

        return training_manifest

# --- MOCK DATA & EXECUTION ---
if __name__ == "__main__":
    # Simulated Raw Output from a base model (e.g., OpenAI Whisper)
    # Contains messy data: silence, noise, and valid Pidgin.
    mock_asr_output = [
        {"id": 1, "file_name": "lagos_traffic.wav", "start_time": "00:00:00.500", "end_time": "00:00:04.200", "transcript": "Abeg, no vex, road block yakata today."},
        {"id": 2, "file_name": "lagos_traffic.wav", "start_time": "00:00:04.200", "end_time": "00:00:04.800", "transcript": "[silence]"},
        {"id": 3, "file_name": "lagos_traffic.wav", "start_time": "00:00:05.000", "end_time": "00:00:15.500", "transcript": "You see say fuel price don go up again? Na wa o."},
        {"id": 4, "file_name": "lagos_traffic.wav", "start_time": "00:00:16.000", "end_time": "00:00:16.400", "transcript": "Hmm."} 
    ]

    pipeline = PidginAligner()
    clean_manifest = pipeline.process_manifest(mock_asr_output)

    # Save to JSONL (The industry standard format for AI training)
    output_file = "train_manifest.jsonl"
    with open(output_file, "w") as f:
        for entry in clean_manifest:
            json.dump(entry, f)
            f.write('\n')

    print(f"\n--- PIPELINE SUMMARY ---")
    print(f"Total Processed: {len(mock_asr_output)}")
    print(f"Discarded:       {pipeline.discarded_count}")
    print(f"Valid Samples:   {len(clean_manifest)}")
    print(f"✅ Manifest saved to '{output_file}'")
