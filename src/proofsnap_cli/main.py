from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass, asdict


@dataclass
class Segment:
    start: float
    end: float
    text: str
    confidence: float


def fake_transcribe(url: str) -> list[Segment]:
    # Placeholder local pipeline output.
    return [
        Segment(0.0, 3.2, f"Transcript for {url}", 0.93),
        Segment(3.2, 7.8, "Proof mode includes confidence + hash.", 0.89),
    ]


def transcript_hash(segments: list[Segment]) -> str:
    payload = "\n".join(s.text for s in segments).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(prog="proofsnap", description="URL -> transcript pack")
    parser.add_argument("url", help="Media URL")
    parser.add_argument("--proof", action="store_true", help="Include transcript hash")
    args = parser.parse_args()

    segments = fake_transcribe(args.url)
    out = {
        "url": args.url,
        "segments": [asdict(s) for s in segments],
    }
    if args.proof:
        out["transcript_sha256"] = transcript_hash(segments)

    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
