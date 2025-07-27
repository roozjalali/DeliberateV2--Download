#!/usr/bin/env python3
"""
Download Deliberate v2.0 from CivitAI
"""

import os
import requests
from pathlib import Path

def download_deliberate_v2():
    """Download Deliberate v2.0 model from CivitAI"""
    
    # CivitAI model URL for Deliberate v2.0 (corrected)
    model_url = "https://civitai.com/api/download/models/128713"
    
    # Create models directory if it doesn't exist
    models_dir = Path(__file__).parent.parent / "models"
    models_dir.mkdir(exist_ok=True)
    
    # Create deliberate directory
    deliberate_dir = models_dir / "deliberate-v2"
    deliberate_dir.mkdir(exist_ok=True)
    
    # Download the model file
    model_file = deliberate_dir / "deliberate_v2.safetensors"
    
    print(f"📥 Downloading Deliberate v2.0 from CivitAI...")
    print(f"📁 Saving to: {model_file}")
    print(f"🔗 URL: {model_url}")
    
    try:
        # Download with progress
        response = requests.get(model_url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open(model_file, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    
                    # Show progress
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        print(f"\r📊 Progress: {percent:.1f}% ({downloaded}/{total_size} bytes)", end='', flush=True)
        
        print(f"\n✅ Download complete! Model saved to: {model_file}")
        print(f"📏 File size: {downloaded / (1024*1024):.1f} MB")
        
    except Exception as e:
        print(f"\n❌ Error downloading model: {e}")
        print(f"💡 Try visiting: https://civitai.com/models/128713/deliberate-v2")
        return False
    
    return True

if __name__ == "__main__":
    download_deliberate_v2() 
