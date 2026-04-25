import argparse
import subprocess
import sys

from f5_tts.api import F5TTS

from normalize import normalize


def synthesize(text: str, ref_audio: str, ref_text: str, output: str, speed: float) -> None:
    F5TTS().infer(
        ref_audio_path=ref_audio,
        ref_text=ref_text,
        gen_text=text,
        file_wave=output,
        speed=speed,
        remove_silence=True,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Text-to-speech for Moroccan Darija via voice cloning"
    )
    parser.add_argument("text", nargs="?", help="Text to synthesize")
    parser.add_argument("-f", "--file", help="Input text file")
    parser.add_argument("-o", "--output", default="output.wav", help="Output wav path")
    parser.add_argument("--ref-audio", required=True, help="Reference WAV (5-15s of a Moroccan speaker)")
    parser.add_argument("--ref-text", required=True, help="Transcript of the reference audio")
    parser.add_argument("-s", "--speed", type=float, default=0.9, help="Speed factor (default 0.9)")
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
    synthesize(text, args.ref_audio, args.ref_text, args.output, args.speed)
    print(f"Saved to {args.output}")
    if args.play:
        subprocess.run(["afplay", args.output], check=True)


if __name__ == "__main__":
    main()
