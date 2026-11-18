"""Builds gershon.ai/articles from _build/articles_content.py.
Outputs: articles/index.html, articles/<slug>/index.html, articles/articles.json, articles/embed.js
"""
import html, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from articles_content import ARTICLES, DATE, AUTHOR

ROOT = os.path.join(os.path.dirname(__file__), "..")
OUT = os.path.join(ROOT, "articles")
BASE = "https://gershon.ai"
VERSION = "1.0"
e = html.escape

CSS = """
:root{--red:#FE1B04;--red2:#d11200;--tint:#fff5f5;--ink:#1a1a1a;--char:#2a2a2a;--muted:#6b6b6b;--line:#e5e5e5;--paper:#fafaf7;--dark:#0b0f1a}
*{box-sizing:border-box;margin:0;padding:0}html,body{overflow-x:hidden}
body{font-family:'Inter Tight','Helvetica Neue',Helvetica,Arial,sans-serif;background:var(--paper);color:var(--ink);line-height:1.5;-webkit-font-smoothing:antialiased}
a{color:inherit}
.top{position:sticky;top:0;z-index:50;background:rgba(250,250,247,.94);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.top-in{max-width:1180px;margin:0 auto;padding:14px 28px;display:flex;align-items:center;gap:24px}
.top img{height:34px;display:block}.nav{display:flex;gap:22px;margin-left:auto;font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.1em;text-transform:uppercase}
.nav a{text-decoration:none}.nav a.on,.nav a:hover{color:var(--red)}
.pill{background:var(--red);color:#fff;border-radius:999px;padding:10px 18px;font-weight:600;font-size:14px;text-decoration:none;white-space:nowrap;display:inline-block}
.pill:hover{background:var(--red2)}
.eb{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--red);display:flex;align-items:center;gap:12px;margin-bottom:18px}
.eb::before{content:'';width:28px;height:2px;background:var(--red)}
h1,h2,h3{font-family:Fraunces,Georgia,serif;font-weight:500;letter-spacing:-.02em}
.hero{max-width:1180px;margin:0 auto;padding:72px 28px 40px}
.hero h1{font-size:clamp(38px,5.4vw,68px);line-height:1.02;max-width:900px}.hero h1 em{color:var(--red)}
.hero p{font-size:18px;color:var(--char);max-width:640px;margin-top:20px;line-height:1.6}
.feat{max-width:1180px;margin:0 auto 24px;padding:0 28px}
.feat a{display:grid;grid-template-columns:1.2fr 1fr;gap:40px;background:var(--dark);color:#fff;border-radius:20px;padding:48px;text-decoration:none}
.feat h2{font-size:clamp(28px,3.4vw,42px);line-height:1.08}.feat p{color:rgba(255,255,255,.8);font-size:17px;line-height:1.6}
.feat .eb{color:#ff5a3c}.feat .eb::before{background:#ff5a3c}.feat .go{margin-top:22px;display:inline-block;color:#ff5a3c;font-weight:600}
.grid{max-width:1180px;margin:0 auto;padding:0 28px 80px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.card{display:flex;flex-direction:column;background:#fff;border:1px solid var(--line);border-radius:14px;padding:26px;text-decoration:none;transition:border-color .15s,transform .15s}
.card:hover{border-color:var(--red);transform:translateY(-2px)}
.card .tag{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--red);letter-spacing:.08em;text-transform:uppercase;margin-bottom:14px}
.card h3{font-size:22px;line-height:1.15;margin-bottom:10px}.card p{font-size:14.5px;color:#444;line-height:1.55;flex:1}
.card .meta{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--muted);margin-top:18px;padding-top:14px;border-top:1px dashed var(--line);display:flex;justify-content:space-between}
.art{max-width:760px;margin:0 auto;padding:64px 28px 24px}
.art h1{font-size:clamp(34px,4.6vw,54px);line-height:1.05}
.dek{font-size:20px;color:var(--char);line-height:1.55;margin:20px 0 26px}
.byline{font-family:'JetBrains Mono',monospace;font-size:11.5px;color:var(--muted);letter-spacing:.04em;padding:14px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);display:flex;flex-wrap:wrap;gap:8px 20px}
.body{padding-top:28px}.body h2{font-size:28px;margin:36px 0 12px}
.body p{font-size:18px;line-height:1.7;color:#222;margin-bottom:18px}
.body ul{list-style:none;margin:6px 0 22px}.body li{position:relative;padding-left:24px;font-size:17.5px;line-height:1.6;margin-bottom:10px;color:#222}
.body li::before{content:'';position:absolute;left:2px;top:11px;width:8px;height:8px;border-radius:50%;background:var(--red)}
.body blockquote{font-family:Fraunces,Georgia,serif;font-size:28px;line-height:1.25;color:var(--red);border-left:3px solid var(--red);padding:4px 0 4px 22px;margin:30px 0}
.app{max-width:760px;margin:16px auto 0;padding:0 28px}
.app>div{background:var(--tint);border:1px solid #ffd9d3;border-radius:16px;padding:26px 28px;display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap}
.app b{font-family:Fraunces,Georgia,serif;font-weight:500;font-size:22px;display:block}.app span{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--red2)}
.ghost{border:1px solid var(--ink);border-radius:999px;padding:10px 18px;font-weight:600;font-size:14px;text-decoration:none}
.more{max-width:1180px;margin:0 auto;padding:64px 28px 0}.more h2{font-size:30px;margin-bottom:20px}
.more .grid{padding:0 0 40px}
.cta{max-width:1180px;margin:0 auto;padding:0 28px 64px}
.cta>div{background:var(--dark);color:#fff;border-radius:20px;padding:48px;display:grid;grid-template-columns:1.3fr 1fr;gap:32px;align-items:center}
.cta h2{font-size:34px;line-height:1.1}.cta p{color:rgba(255,255,255,.75);font-size:14px;margin-top:10px}
footer{border-top:1px solid var(--line);text-align:center;padding:32px;color:#888;font-size:13px}footer a{color:#888}
@media(max-width:900px){.grid{grid-template-columns:1fr 1fr}.feat a,.cta div{grid-template-columns:1fr;padding:32px}}
@media(max-width:620px){.grid{grid-template-columns:1fr}.nav a.hide{display:none}.nav{gap:14px}.top img{height:28px}.top .pill{display:none}.body p{font-size:17px}}
"""

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter+Tight:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>'


def head(title, desc, url, extra=""):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{e(title)}</title><meta name="description" content="{e(desc)}"/><link rel="canonical" href="{url}"/>
<meta property="og:type" content="article"/><meta property="og:title" content="{e(title)}"/><meta property="og:description" content="{e(desc)}"/><meta property="og:url" content="{url}"/><meta property="og:site_name" content="Gershon.AI"/><meta name="twitter:card" content="summary"/>
<link rel="icon" href="/assets/gershon-ai-logo.png"/>{FONTS}<style>{CSS}</style>{extra}</head><body>
<header class="top"><div class="top-in"><a href="/"><img src="/assets/gershon-ai-logo.png" alt="Gershon.AI"/></a>
<nav class="nav"><a href="/" class="hide">Home</a><a href="/agents/" class="hide">Agents</a><a href="/apps/">Apps</a><a href="/articles/" class="on">Articles</a></nav>
<a class="pill" href="https://www.gershonconsulting.com/calendar">Book a call</a></div></header>"""


FOOT = f"""<section class="cta"><div><div><div class="eb" style="color:#ff5a3c">Your U.S. launch</div><h2>See what these apps can do for your U.S. pipeline.</h2></div>
<div><a class="pill" href="https://www.gershonconsulting.com/calendar">Book a 20-minute call</a><p>With the Gershon team in New York.</p></div></div></section>
<footer><a href="/">Gershon.AI</a> · by Gershon Consulting · Est. 2013 · New York · <a href="/articles/">Articles</a> v {VERSION}</footer></body></html>"""


def card(a):
    return f"""<a class="card" href="/articles/{a['slug']}/"><div class="tag">{e(a['app'])} · {e(a['tag'])}</div><h3>{e(a['title'])}</h3><p>{e(a['dek'])}</p><div class="meta"><span>{a['read']} min read</span><span>Read →</span></div></a>"""


def render_body(blocks):
    out = []
    for kind, val in blocks:
        if kind == "h":
            out.append(f"<h2>{e(val)}</h2>")
        elif kind == "p":
            out.append(f"<p>{e(val)}</p>")
        elif kind == "q":
            out.append(f"<blockquote>{e(val)}</blockquote>")
        elif kind == "ul":
            out.append("<ul>" + "".join(f"<li>{e(i)}</li>" for i in val) + "</ul>")
    return "\n".join(out)


def article_page(a, others):
    url = f"{BASE}/articles/{a['slug']}/"
    ld = json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["dek"],
                     "author": {"@type": "Person", "name": "Olivier Attia"},
                     "publisher": {"@type": "Organization", "name": "Gershon Consulting", "url": "https://www.gershonconsulting.com"},
                     "datePublished": "2026-11-18", "mainEntityOfPage": url})
    app_label = a["url"].replace("https://", "").rstrip("/")
    more = "".join(card(o) for o in others)
    return (head(f"{a['title']} | Gershon.AI", a["dek"], url, f'<script type="application/ld+json">{ld}</script>') +
            f"""<main><article class="art"><div class="eb">{e(a['app'])} · {e(a['tag'])}</div><h1>{e(a['title'])}</h1><p class="dek">{e(a['dek'])}</p>
<div class="byline"><span>{e(AUTHOR)}</span><span>{DATE}</span><span>{a['read']} min read</span></div>
<div class="body">{render_body(a['body'])}</div></article>
<section class="app"><div><div><b>{e(a['app'])}</b><span>{e(app_label)}</span></div><div style="display:flex;gap:10px;flex-wrap:wrap"><a class="pill" href="{a['url']}">Open {e(a['app'])} ↗</a><a class="ghost" href="https://www.gershonconsulting.com/calendar">Talk to us</a></div></div></section>
<section class="more"><h2>More from the series</h2><div class="grid">{more}</div><p style="padding-bottom:40px"><a href="/articles/" style="color:var(--red);font-weight:600;text-decoration:none">All articles →</a></p></section></main>""" + FOOT)


def index_page():
    feat = [a for a in ARTICLES if a.get("featured")][0]
    rest = [a for a in ARTICLES if not a.get("featured")]
    url = f"{BASE}/articles/"
    desc = "Why we built each Gershon.AI app, what it does and why it is powerful for companies growing in the U.S. market."
    return (head("Articles | Gershon.AI", desc, url) +
            f"""<main><section class="hero"><div class="eb">gershon.ai/articles</div><h1>Why we built <em>every app.</em></h1>
<p>Thirteen years of U.S. market entry taught us where growth leaks. Each app plugs one leak. These articles explain the reason behind each one, what it does and why it matters for your U.S. pipeline.</p></section>
<section class="feat"><a href="/articles/{feat['slug']}/"><div><div class="eb">Start here · {e(feat['tag'])}</div><h2>{e(feat['title'])}</h2></div><div><p>{e(feat['dek'])}</p><span class="go">Read the story · {feat['read']} min →</span></div></a></section>
<section class="grid">{''.join(card(a) for a in rest)}</section></main>""" + FOOT)


def main():
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, "index.html"), "w").write(index_page())
    for i, a in enumerate(ARTICLES):
        others = [ARTICLES[(i + k) % len(ARTICLES)] for k in (1, 2, 3)]
        d = os.path.join(OUT, a["slug"]); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w").write(article_page(a, others))
    feed = {"version": VERSION, "url": f"{BASE}/articles/", "updated": "2026-11-18",
            "articles": [{"slug": a["slug"], "app": a["app"], "title": a["title"], "summary": a["dek"],
                          "url": f"{BASE}/articles/{a['slug']}/", "app_url": a["url"], "read_minutes": a["read"]} for a in ARTICLES]}
    open(os.path.join(OUT, "articles.json"), "w").write(json.dumps(feed, indent=1))
    print(f"built {len(ARTICLES)} articles + index + feed")


if __name__ == "__main__":
    main()
