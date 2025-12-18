import re

def normalize_pidgin(text):
    # Remove common transcription artifacts
    text = text.lower()
    text = re.sub(r'\<qn\>', '', text) # Remove noise tags
    
    # Standardize common Pidgin spelling variations (Demo logic)
    text = re.sub(r'\bde\b', 'dey', text) 
    text = re.sub(r'\bwetin\b', 'weytin', text)
    
    return text.strip()
