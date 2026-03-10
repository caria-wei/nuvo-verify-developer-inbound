"""
Minimal NUVO Verify webhook receiver (Python / Flask)
- Verifies HMAC SHA256 signature from x-nuvo-signature / x-signature
- Builds deterministic ledger key: orderId:tokenSymbol:event
"""

import hmac
import hashlib
import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)
WEBHOOK_SECRET = os.getenv("NUVO_WEBHOOK_SECRET", "")


def verify_signature(raw_body: bytes, signature_header: str, secret: str) -> bool:
    expected = "sha256=" + hmac.new(secret.encode("utf-8"), raw_body, hashlib.sha256).hexdigest()
    return hmac.compare_digest((signature_header or "").encode("utf-8"), expected.encode("utf-8"))


@app.post("/webhooks/nuvo")
def nuvo_webhook():
    raw = request.get_data(cache=False)
    sig = request.headers.get("x-nuvo-signature") or request.headers.get("x-signature") or ""

    if not WEBHOOK_SECRET or not verify_signature(raw, sig, WEBHOOK_SECRET):
        return jsonify({"ok": False, "error": "invalid signature"}), 401

    payload = json.loads(raw.decode("utf-8"))
    data = payload.get("data", {}) if isinstance(payload, dict) else {}
    ledger_key = f"{data.get('orderId')}:{data.get('tokenSymbol')}:{payload.get('event')}"

    # TODO: upsert into your internal ledger table (idempotent on ledger_key)
    # upsert_ledger(ledger_key=ledger_key, payload=payload)

    return jsonify({"ok": True, "ledger_key": ledger_key})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8787, debug=True)
