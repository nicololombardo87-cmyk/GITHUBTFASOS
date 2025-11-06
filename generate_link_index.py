import os, urllib.parse, datetime

OWNER = "nicololombardo87-cmyk"
REPO  = "GITHUBTFASOS"
BRANCH = "main"
EXTS = (".pdf", ".pptx", ".docx", ".md")

rows = []
for base, _, files in os.walk("."):
    if "/.git" in base or base.startswith("./.git"):
        continue
    for f in files:
        if f.startswith("."):
            continue
        if f.lower().endswith(EXTS):
            path = os.path.join(base, f).replace("\\", "/")
            if path.startswith("./"):
                path = path[2:]
            url_path = urllib.parse.quote(path)
            blob = f"https://github.com/{OWNER}/{REPO}/blob/{BRANCH}/{url_path}"
            mod = os.path.dirname(path) or "/"
            rows.append((mod, f, blob))

rows.sort()
out = []
out.append("# 📎 Index Link Files — Archivio TFA\n")
out.append(f"_Aggiornato: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}_\n\n")
out.append("| Cartella | File | Link |\n|---|---|---|\n")
for mod, fname, link in rows:
    out.append(f"| `{mod}` | `{fname}` | [Apri]({link}) |\n")

with open("LINK_INDEX.md", "w", encoding="utf-8") as fh:
    fh.writelines(out)

print(f"Generato LINK_INDEX.md con {len(rows)} file.")
