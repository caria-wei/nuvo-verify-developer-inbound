# NUVO Developer Inbound Starter Pack

This pack is for technical inbound acquisition on Postman / GitHub / Dev.to / Hashnode.

## Included

1. `NUVO-Verify-Developer-Inbound.postman_collection.json`
   - Run-ready flow: Auth -> Payment Link -> Webhook -> Order Proof -> Risk endpoints.
2. `NUVO-Verify-Sandbox.postman_environment.json`
3. `NUVO-Verify-Production.postman_environment.json`
4. `webhook-receiver-node-sample.mjs`
   - Minimal webhook endpoint with HMAC signature verification.

## 10-minute demo flow (for prospects)

1. Import collection + sandbox environment to Postman.
2. Set `merchant_email` / `merchant_password`.
3. Run `01 Auth & Context / Merchant Login`.
4. Run `02 Sandbox Payment Flow / Create Payment Link`.
5. Run `03 Webhooks / Create Webhook` (use your temporary endpoint).
6. Run `03 Webhooks / Send Test Webhook`.
7. Run `02 Sandbox Payment Flow / Get Order Proof`.

## Publish plan (highest impact first)

1. Publish Postman collection publicly.
2. Push GitHub repo with this pack + 1 quickstart README.
3. Publish one technical tutorial on Dev.to and Hashnode linking to:
   - Postman Collection
   - GitHub sample
   - API docs

## Qualification signals to track

- Imported collection count
- Successful `Merchant Login` runs
- `Create Payment Link` success count
- `Send Test Webhook` success count
- Clicks to meeting CTA from tutorial pages
