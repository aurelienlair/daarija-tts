import pytest


@pytest.mark.skip(reason="requires reference audio and ~1GB model download")
def test_synthesize_writes_wav(tmp_path):
    from tts import synthesize

    output = str(tmp_path / "out.wav")
    synthesize("مرحبا بيك", "reference.wav", "مرحبا", output, speed=0.9)
    assert (tmp_path / "out.wav").stat().st_size > 0
