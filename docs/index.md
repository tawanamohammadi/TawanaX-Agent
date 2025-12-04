<style>
:root {
  --bg: #ffffff;
  --fg: #0f172a;
  --muted: #64748b;
  --card: #f8fafc;
  --border: #e2e8f0;
  --primary: linear-gradient(135deg,#6d28d9,#2563eb);
}
[data-theme="dark"] {
  --bg: #0b0f18;
  --fg: #e2e8f0;
  --muted: #94a3b8;
  --card: #0f172a;
  --border: #1f2937;
}
body { background: var(--bg); color: var(--fg); font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue"; }
.container { max-width: 1080px; margin: 0 auto; padding: 24px; }
.hero { border-radius: 18px; padding: 48px 28px; color: #fff; background-image: var(--primary); box-shadow: 0 10px 30px rgba(0,0,0,.12); }
.hero h1 { font-size: 42px; margin: 0 0 8px 0; }
.hero p { font-size: 18px; opacity: .95; }
.actions { display:flex; gap:12px; margin-top: 18px; flex-wrap:wrap }
.btn { display:inline-block; padding: 10px 16px; border-radius: 10px; text-decoration:none; font-weight:600; }
.btn.white { background: #fff; color:#0f172a; }
.btn.ghost { border: 1px solid rgba(255,255,255,.5); color:#fff; }
.grid { display:grid; grid-template-columns: repeat(auto-fit,minmax(240px,1fr)); gap:16px; margin: 22px 0; }
.card { background: var(--card); border: 1px solid var(--border); border-radius: 14px; padding: 16px; box-shadow: 0 2px 12px rgba(0,0,0,.06); }
.card h3 { margin: 0 0 6px 0; font-size: 18px }
.card p { margin: 0; color: var(--muted); font-size: 14px; line-height: 1.6 }
.links a { display:block; padding:14px; border:1px solid var(--border); border-radius:12px; text-decoration:none; color: var(--fg); background: var(--card); box-shadow:0 2px 8px rgba(0,0,0,.04) }
.links { display:grid; grid-template-columns: repeat(auto-fit,minmax(220px,1fr)); gap:14px; margin: 20px 0 }
.wip { color: var(--muted); margin-top: 8px }
.toggle { position: relative; display:inline-flex; align-items:center; gap:8px; font-size:14px; margin-top: 10px }
.toggle input { width: 40px; height: 20px }
</style>

<div class="container">
  <div class="hero">
    <h1>TawanaX-Agent</h1>
    <p>Next-Gen Multi-Stage AI Coding Agents under Tawana Network</p>
    <div class="actions">
      <a class="btn white" href="./quickstart.md">Get Started</a>
      <a class="btn ghost" href="./architecture.md">Architecture</a>
    </div>
    <label class="toggle">
      <input type="checkbox" id="darkToggle" />
      <span>Dark mode</span>
    </label>
  </div>

  <div class="grid">
    <div class="card"><h3>Multi-Agent</h3><p>Planner, Coder, Reviewer, Indexer, Docs. Orchestrated for real workflows.</p></div>
    <div class="card"><h3>Developer-Ready</h3><p>Minimal Python skeleton, examples, and GitHub Pages out of the box.</p></div>
    <div class="card"><h3>SEO & Docs</h3><p>Clean structure, public documentation, and knowledge sync agents.</p></div>
    <div class="card"><h3>Extensible</h3><p>Registry for specialized agents under TawanaX-Bot.</p></div>
  </div>

  <pre style="background:var(--card);border:1px solid var(--border);padding:12px;border-radius:12px">Planner → Coder → Reviewer → Indexer → Docs</pre>

  <div class="links">
    <a href="./quickstart.md">Quickstart</a>
    <a href="./architecture.md">Architecture</a>
    <a href="./agents.md">Agents</a>
    <a href="./roadmap.md">Roadmap</a>
  </div>

  <div class="wip">More documentation coming soon.</div>
</div>

<section id="recent-activity" style="margin-top:2rem">
  <h2>Recent TawanaX-Agent Activity</h2>
  <p>Auto-updated from GitHub public events. (More details coming soon.)</p>
  <div id="activity-list" style="display:grid;gap:12px"></div>
</section>

<script>
const USER = "tawanamohammadi";
const MAX_ITEMS = 12;

function cardHTML(e){
  const repo = e.repo?.name || "unknown-repo";
  const when = new Date(e.created_at).toLocaleString();
  let title = e.type.replace("Event","");

  let details = "";
  if(e.type === "PushEvent"){
    const commits = (e.payload.commits || []).slice(0,3);
    details = commits.map(c => `• ${c.message}`).join("<br>");
  }

  return `
    <div style="padding:14px;border:1px solid #eee;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,0.04)">
      <div style="font-weight:700">${title} — ${repo}</div>
      <div style="font-size:13px;color:#666;margin:6px 0">${when}</div>
      <div style="font-size:14px;line-height:1.6">${details || "Activity recorded by TawanaX agents."}</div>
      <a href=" `https://github.com/${repo}` " target="_blank" style="font-size:13px">View repo</a>
    </div>`;
}

async function loadActivity(){
  const list = document.getElementById("activity-list");
  list.innerHTML = "Loading…";
  try{
    const res = await fetch(` `https://api.github.com/users/${USER}/events/public` `);
    const events = await res.json();
    list.innerHTML = "";

    events.slice(0, MAX_ITEMS).forEach(e=>{
      list.insertAdjacentHTML("beforeend", cardHTML(e));
    });
  }catch(err){
    list.innerHTML = "Could not load activity right now.";
  }
}
loadActivity();
</script>

<script>
const tgl = document.getElementById('darkToggle');
if (tgl) {
  const apply = (v) => {
    document.documentElement.setAttribute('data-theme', v ? 'dark' : 'light');
    localStorage.setItem('tx-theme', v ? 'dark' : 'light');
  };
  const saved = localStorage.getItem('tx-theme');
  if (saved) { const v = saved === 'dark'; tgl.checked = v; apply(v); }
  tgl.addEventListener('change', e => apply(e.target.checked));
}
</script>

<div style="margin-top:2rem;color:#666;font-size:13px">TawanaX is a Tawana Network project by Tawana Mohammadi.</div>
