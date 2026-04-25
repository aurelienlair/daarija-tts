import asyncio
from pathlib import Path

import pytest

from tts import VOICES, synthesize


@pytest.mark.parametrize("voice", VOICES)
def test_synthesize_writes_mp3(tmp_path: Path, voice: str) -> None:
    output = str(tmp_path / "out.mp3")
    asyncio.run(synthesize("مرحبا بيك", voice, output))
    assert Path(output).exists()
    assert Path(output).stat().st_size > 0
