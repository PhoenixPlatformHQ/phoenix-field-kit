# Local Phoenix renderer

Requires Python 3.12, FFmpeg and packages in requirements-render.txt.
Model used: https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.int8.onnx
Voices: https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin

Set model/voice paths in build_video.py for your environment, then run it.
The supplied per-scene WAV files reproduce the rendered voice without another synthesis.
No Higgsfield, credentials or paid APIs.
Fixture output is real local Python output, never GitLab Runner output.
Subtitle chunks use estimated scene-relative timing, not forced word alignment.
