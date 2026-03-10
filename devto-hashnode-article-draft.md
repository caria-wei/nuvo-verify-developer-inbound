# How to automate stablecoin payment reconciliation with Webhooks + deterministic IDs

If your team already has a Web2 backend and wants to avoid manual crypto reconciliation, here is a practical flow:

- Create checkout (payment link)
- Receive webhook events (`payment.created`, `payment.confirmed`, `payment.rejected`)
- Pull order proof for audit
- Write deterministic ledger keys in your internal DB

## 1) Run the API flow in 10 minutes (Postman)

Import:
- `NUVO-Verify-Developer-Inbound.postman_collection.json`
- `NUVO-Verify-Sandbox.postman_environment.json`

Then run:
1. `Merchant Login`
2. `Create Payment Link`
3. `Create Webhook`
4. `Send Test Webhook`
5. `Get Order Proof`

## 2) Webhook receiver (Node.js)

```js
import express from "express";
import crypto from "crypto";

const app = express();
app.use(express.raw({ type: "*/*" }));

const WEBHOOK_SECRET = process.env.NUVO_WEBHOOK_SECRET;

function verifySignature(rawBody, signatureHeader, secret) {
  const expected = "sha256=" + crypto.createHmac("sha256", secret).update(rawBody).digest("hex");
  const a = Buffer.from(signatureHeader || "");
  const b = Buffer.from(expected);
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}

app.post("/webhooks/nuvo", (req, res) => {
  const sig = req.header("x-nuvo-signature") || req.header("x-signature") || "";
  if (!verifySignature(req.body, sig, WEBHOOK_SECRET)) {
    return res.status(401).json({ ok: false, error: "invalid signature" });
  }

  const payload = JSON.parse(req.body.toString("utf8"));
  const ledgerKey = `${payload?.data?.orderId}:${payload?.data?.tokenSymbol}:${payload?.event}`;

  // upsert to your internal ledger table
  // upsertLedger({ ledgerKey, payload });

  return res.json({ ok: true });
});

app.listen(8787, () => console.log("listening on :8787"));
```

## 3) Event-to-ledger mapping

Recommended minimum table fields:

- `ledger_key` (unique)
- `order_id`
- `event_type`
- `token_symbol`
- `amount`
- `tx_hash`
- `traffic_light`
- `received_at`
- `raw_payload_json`

## 4) Why this reduces ops cost

- No manual transaction-by-transaction matching
- Deterministic keys avoid duplicate posting
- Proof endpoint provides auditable evidence for completed orders

## 5) Next step

- Keep your current Web2 backend
- Add webhook endpoint + idempotent writer
- Start with sandbox, then move to production environment
