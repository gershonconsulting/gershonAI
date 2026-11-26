# gershonAI hub — STATUS (updated 2026-11-26)

Static hub for gershon.ai. Cloudflare Pages project `gershon-ai` (direct zip upload, no Git link).
Deploy = zip of index.html + internal.html + agents/ + platforms/ + mcp/ + apps/ + articles/ + assets/ uploaded in the Pages dashboard (see HANDOFF.txt).

## Pages
- `/` index.html — NEW home 2026-11-16: AI marketing agency teaser (gershonconsulting.com layout, Gershon.AI logo, 6 agents, early-access call)
- `/agents/` agents/index.html — 2026-11-17 dedicated page for the 6 agents (what each does, deliverable, cadence, platform behind it, how they chain, what stays human, FAQ). Home #agents cards + nav link here.
- `/platforms/` platforms/index.html — the former hub v1.5 (moved from /)
- `/internal` internal.html — team platforms v1.5.5
- `/mcp` mcp/index.html — Gershon MCP connector
- `/articles/` articles/ — v1.0 2026-11-18: 16 articles (why we built each app), index, articles.json feed. Source + generator in _build/ (edit _build/articles_content.py, run python3 _build/build_articles.py). Logo file /assets/gershon-ai-logo.png. _build/ is NOT part of the deploy zip.
- `/apps` apps/index.html — v1.0, all 32 apps in 3 families: External (12), Internal (11), Independent (9); search + filter. Generator: tiles are hand-kept in the page.

## ✅ Done
- ✅ 2026-11-26 Articles v1.1: LinkedIn article "If you pay peanuts, you get monkeys!" at /articles/if-you-pay-peanuts-you-get-monkeys/ with podcast MP3 (Kokoro TTS, 2 hosts, 4:28). PR #20. DEPLOYED to production (Pages zip upload from branch deploy-zip via dashboard). This upload also put v1.5.3–1.5.5 and /articles live.
- ✅ 2026-11-18 /articles/ section + Articles link on home, agents, apps, mcp, platforms, internal. Desktop 1280 / mobile 390: no overflow, no JS errors.
- ✅ 2026-11-17 /agents/ page + home links to it. Desktop 1280 / mobile 390: no overflow, no JS errors.
- ✅ 2026-11-16 /apps page added (regrouped per Olivier 2026-11-16: 32 apps, 27 open, 5 coming soon; published to production). Desktop 1280 + mobile 390: no overflow, no JS errors. All 27 links checked with curl (200 or redirect to sign-in).

## ❌ Open
- ❌ Link gershon.ai/articles (and each app's own article) from every app's menu/footer.
- ✅ 2026-11-16 New home page published on Olivier's "publish the sample". /internal and /apps (and /platforms) now load /assets/gershon-ai-logo.png (v1.5.4).
- ❌ Home hero uses a drawn skyline, not the gershonconsulting.com photos; the agents box is descriptive, not live data yet.
- ❌ No DNS yet: crm.gershoncrm.com, ai.gershon.ai, roi.gershoncrm.com, e2.gershoncrm.com, mcp.gershon.ai (shown as Coming soon).
- ❌ enricherpro.com / qrnetworking.com redirect to dead novita sandboxes; xpensepro.com redirects to a genspark space.

## Deploy route (works, no human)
zip index.html internal.html agents platforms mcp apps articles assets → push as gershon-ai-site.zip to branch deploy-zip → in dash.cloudflare.com Pages gershon-ai > Create deployment, fetch raw.githubusercontent.com/.../deploy-zip/gershon-ai-site.zip in page JS, inject into the .zip file input via DataTransfer → Save and deploy.
