<div align="center" style="margin-top:2rem">
  <h1>TawanaX-Agent</h1>
  <p>Next-Gen Multi-Stage AI Coding Agents under Tawana Network</p>
</div>

- Modular, multi-agent autocoding framework
- Clean architecture for Planner → Coder → Reviewer → Indexer → Docs
- Public docs and GitHub Pages ready
- Extensible registry for TawanaX-Bot agents

```
Planner → Coder → Reviewer → Indexer → Docs
```

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:20px 0">
  <a href="./quickstart.md" style="padding:14px;border:1px solid #eee;border-radius:10px;text-decoration:none">Quickstart</a>
  <a href="./architecture.md" style="padding:14px;border:1px solid #eee;border-radius:10px;text-decoration:none">Architecture</a>
  <a href="./agents.md" style="padding:14px;border:1px solid #eee;border-radius:10px;text-decoration:none">Agents</a>
  <a href="./roadmap.md" style="padding:14px;border:1px solid #eee;border-radius:10px;text-decoration:none">Roadmap</a>
</div>

More documentation coming soon.

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

<div style="margin-top:2rem;color:#666;font-size:13px">TawanaX is a Tawana Network project by Tawana Mohammadi.</div>
