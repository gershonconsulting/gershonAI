# gershonAI hub — STATUS (updated 2026-11-16)

Static hub for gershon.ai. Cloudflare Pages project `gershon-ai` (direct zip upload, no Git link).
Deploy = zip of index.html + internal.html + mcp/ + apps/ uploaded in the Pages dashboard (see HANDOFF.txt).

## Pages
- `/` index.html — hub v1.5 (brand red #FE1B04)
- `/internal` internal.html — team platforms v1.5.1
- `/mcp` mcp/index.html — Gershon MCP connector
- `/apps` apps/index.html — v1.0, all 35 apps in 3 families: External (14), Internal (11), Independent (10); search + filter. Generator: tiles are hand-kept in the page.

## ✅ Done
- ✅ 2026-11-16 /apps page added (35 apps, 27 open, 8 coming soon). Desktop 1280 + mobile 390: no overflow, no JS errors. All 27 links checked with curl (200 or redirect to sign-in).

## ❌ Open
- ❌ New home page (AI-agency teaser, gershonconsulting.com look) — concepts shown to Olivier, awaiting his pick.
- ❌ No DNS yet: crm.gershoncrm.com, ai.gershon.ai, roi.gershoncrm.com, e2.gershoncrm.com, mcp.gershon.ai (shown as Coming soon).
- ❌ enricherpro.com / qrnetworking.com redirect to dead novita sandboxes; xpensepro.com redirects to a genspark space.
