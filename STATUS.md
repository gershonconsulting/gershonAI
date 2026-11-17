# gershonAI hub — STATUS (updated 2026-11-16)

Static hub for gershon.ai. Cloudflare Pages project `gershon-ai` (direct zip upload, no Git link).
Deploy = zip of index.html + internal.html + platforms/ + mcp/ + apps/ uploaded in the Pages dashboard (see HANDOFF.txt).

## Pages
- `/` index.html — NEW home 2026-11-16: AI marketing agency teaser (gershonconsulting.com layout, Gershon.AI logo, 6 agents, early-access call)
- `/platforms/` platforms/index.html — the former hub v1.5 (moved from /)
- `/internal` internal.html — team platforms v1.5.1
- `/mcp` mcp/index.html — Gershon MCP connector
- `/apps` apps/index.html — v1.0, all 32 apps in 3 families: External (12), Internal (11), Independent (9); search + filter. Generator: tiles are hand-kept in the page.

## ✅ Done
- ✅ 2026-11-16 /apps page added (regrouped per Olivier 2026-11-16: 32 apps, 27 open, 5 coming soon; published to production). Desktop 1280 + mobile 390: no overflow, no JS errors. All 27 links checked with curl (200 or redirect to sign-in).

## ❌ Open
- ✅ 2026-11-16 New home page published on Olivier's "publish the sample". /internal and /apps take the logo from /platforms/.
- ❌ Home hero uses a drawn skyline, not the gershonconsulting.com photos; the agents box is descriptive, not live data yet.
- ❌ No DNS yet: crm.gershoncrm.com, ai.gershon.ai, roi.gershoncrm.com, e2.gershoncrm.com, mcp.gershon.ai (shown as Coming soon).
- ❌ enricherpro.com / qrnetworking.com redirect to dead novita sandboxes; xpensepro.com redirects to a genspark space.
