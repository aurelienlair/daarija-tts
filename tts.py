import argparse
import asyncio
import subprocess
import sys

import edge_tts

from normalize import normalize

DEFAULT_VOICE = "ar-MA-JamalNeural"


async def synthesize(text: str, voice: str, output: str, speed: float) -> None:
    rate = f"{int((speed - 1) * 100):+d}%"
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(output)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Text-to-speech for Moroccan Darija")
    parser.add_argument("text", nargs="?", help="Text to synthesize")
    parser.add_argument("-f", "--file", help="Input text file")
    parser.add_argument("-o", "--output", default="output.mp3", help="Output path")
    parser.add_argument("--voice", default=DEFAULT_VOICE, help="Edge TTS voice (default: ar-MA-JamalNeural)")
    parser.add_argument("-s", "--speed", type=float, default=0.75, help="Speed factor (default 0.75)")
    parser.add_argument("--play", action="store_true", help="Play audio after generating")
    return parser.parse_args()


def read_text(args: argparse.Namespace) -> str:
    if args.file:
        with open(args.file, encoding="utf-8") as f:
            return f.read()
    if args.text:
        return args.text
    if not sys.stdin.isatty():
        return sys.stdin.read()
    print("Error: provide text as argument, --file, or via stdin.", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    args = parse_args()
    text = normalize(read_text(args))
    asyncio.run(synthesize(text, args.voice, args.output, args.speed))
    print(f"Saved to {args.output}")
    if args.play:
        subprocess.run(["afplay", args.output], check=True)


if __name__ == "__main__":
    main()
