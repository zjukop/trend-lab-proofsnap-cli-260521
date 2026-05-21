from proofsnap_cli.main import fake_transcribe, transcript_hash


def test_smoke_pipeline():
    segs = fake_transcribe("https://example.com/media")
    assert segs
    h = transcript_hash(segs)
    assert len(h) == 64
