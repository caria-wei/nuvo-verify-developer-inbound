import express from "express";
import crypto from "crypto";

const app = express();
app.use(express.raw({ type: "*/*" }));

const WEBHOOK_SECRET = process.env.NUVO_WEBHOOK_SECRET || "replace_me";

function verifySignature(rawBody, signatureHeader, secret) {
  const expected = "sha256=" + crypto.createHmac("sha256", secret).update(rawBody).digest("hex");
  const a = Buffer.from(signatureHeader || "");
  const b = Buffer.from(expected);
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}

app.post("/webhooks/nuvo", (req, res) => {
  const sig = req.header("x-nuvo-signature") || req.header("x-signature") || "";
  const ok = verifySignature(req.body, sig, WEBHOOK_SECRET);
  if (!ok) return res.status(401).json({ ok: false, error: "invalid signature" });

  const payload = JSON.parse(req.body.toString("utf8"));

  // Example: deterministic ledger mapping key
  const key = `${payload?.data?.orderId || "unknown"}:${payload?.data?.tokenSymbol || ""}:${payload?.event || ""}`;

  console.log("NUVO webhook accepted", { event: payload.event, key });
  return res.json({ ok: true });
});

app.listen(8787, () => {
  console.log("NUVO webhook receiver listening on :8787");
});
