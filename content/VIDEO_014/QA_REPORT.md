# VIDEO_014 completed — 2026-10-09

- Produced locally with Python/Pillow, Kokoro ONNX af_heart and FFmpeg. No Higgsfield. New spend: EUR 0.
- Model: kokoro-v1.0.int8.onnx, official thewh1teagle/kokoro-onnx model-files-v1.0 release. Original scratch fp32 copy was incomplete; restored official int8 weights.
- Vertical 1080x1920 H.264/AAC, 32.904667 s. Complete decode passed.
- Five midpoint frames reviewed; all key text and captions legible and within bounds.
- All narration words included in captions, conservatively distributed per scene using actual WAV duration; word timestamps are estimated, not Whisper alignment.
- Captured fixture run: unsafe final v1-old; serialized final v2-new; fixture PASS. Video includes genuine captured excerpt labelled local fixture, not GitLab output.
- YAML is a template; deployment shell script must be supplied by operator. No GitLab server/runner executed.
- Reviewed current official resource-group and deployment-safety docs. Serialization, process mode and outdated-job protection remain distinct; manual jobs and rollback retries caveats included.
- Publication explicitly requested by Fabio 9 October; no further editorial approval requested for this asset.

MP4 SHA256: 0095b9e3a1630683c7a95910243b5673ecc11e6ae873aa5410a63b32e59dd8b5
