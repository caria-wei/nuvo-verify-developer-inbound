# NUVO Developer Inbound Starter Pack

This pack is for technical inbound acquisition on Postman / GitHub / Dev.to / Hashnode.

## Included

1. `NUVO-Verify-Developer-Inbound.postman_collection.json`
   - Run-ready flow: Auth -> Payment Link -> Webhook -> Order Proof -> Risk endpoints.
2. `NUVO-Verify-Sandbox.postman_environment.json`
3. `NUVO-Verify-Production.postman_environment.json`
4. `webhook-receiver-node-sample.mjs`
   - Minimal webhook endpoint with HMAC signature verification.
5. `webhook-receiver-python-sample.py`
   - Flask-based webhook endpoint with the same signature verification + deterministic ledger key pattern.
6. `openapi.yaml`
   - OpenAPI 3.0.3 spec for inbound-discovery endpoints (for API directories like APIs.guru).

## 10-minute demo flow (for prospects)

1. Import collection + sandbox environment to Postman.
2. Set `merchant_email` / `merchant_password`.
3. Run `01 Auth & Context / Merchant Login`.
4. Run `02 Sandbox Payment Flow / Create Payment Link`.
5. Run `03 Webhooks / Create Webhook` (use your temporary endpoint).
6. Run `03 Webhooks / Send Test Webhook`.
7. Run `02 Sandbox Payment Flow / Get Order Proof`.

## CTA links (UTM-tracked)

- GitHub starter pack: https://github.com/caria-wei/nuvo-verify-developer-inbound?utm_source=github&utm_medium=readme&utm_campaign=nuvo_verify_dev_inbound
- Postman docs: https://caria-w-6623992.postman.co/documentation/53056051-99c386d3-9da5-4763-abfa-533043c33d40?utm_source=github&utm_medium=readme&utm_campaign=nuvo_verify_dev_inbound
- Book technical session: https://calendar.app.google/ehTTN1rYiKAoiE9h8?utm_source=github&utm_medium=readme&utm_campaign=nuvo_verify_dev_inbound

## Current workaround

Postman public sharing is currently blocked by Team plan requirement. Until upgraded, use:

1. GitHub repo (this page)
2. Postman docs link above
3. Dev.to / Hashnode technical walkthroughs

## Qualification signals to track

- Imported collection count
- Successful `Merchant Login` runs
- `Create Payment Link` success count
- `Send Test Webhook` success count
- Clicks to meeting CTA from each channel (UTM split)
