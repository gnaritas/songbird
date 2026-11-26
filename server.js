/* Songbird — static server + contact-form relay (template v2, 2026-11-26, t_fbffb777) */
const http = require("http"), fs = require("fs"), path = require("path");

const SITE = "Songbird";
const PORT = process.env.PORT || 3000;
const root = path.join(__dirname, "public");
const BREVO_API = "https://api.brevo.com/v3/smtp/email";
const MAIL = {
  key: process.env.BREVO_API_KEY || "",
  alias: process.env.MAIL_ALIAS || "jarvis+websites@onsmalltalk.com",
  to: process.env.MAIL_TO || "jarvis+websites@onsmalltalk.com",
};
const MAIL_READY = !!MAIL.key;
const NOINDEX = { "x-robots-tag": "noindex, nofollow" };

const MIME = {
  ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript",
  ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
  ".svg": "image/svg+xml", ".ico": "image/x-icon", ".gif": "image/gif", ".xml": "application/xml", ".txt": "text/plain",
};

function readBody(req, cb) {
  let data = "", len = 0;
  req.on("data", (c) => { len += c.length; if (len > 20000) { req.destroy(); return; } data += c; });
  req.on("end", () => cb(data));
}

function out(file, body, res) {
  const ext = path.extname(file).toLowerCase();
  const cache = ext === ".png" || ext === ".jpg" || ext === ".jpeg" ? "public, max-age=86400"
    : ext === ".css" || ext === ".svg" ? "public, max-age=300" : "public, max-age=60";
  res.writeHead(200, Object.assign({ "content-type": MIME[ext] || "application/octet-stream", "cache-control": cache }, NOINDEX));
  res.end(body);
}

function serve404(res) {
  fs.readFile(path.join(root, "404.html"), (e, d) => {
    res.writeHead(404, Object.assign({ "content-type": "text/html; charset=utf-8" }, NOINDEX));
    res.end(e ? "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"utf-8\"><title>Not found</title><meta name=\"robots\" content=\"noindex\"></head><body><h1>404 — not found</h1></body></html>" : d.toString());
  });
}

function serveStatic(p, res) {
  if (p === "/") p = "/index.html";
  const f = path.normalize(path.join(root, p));
  if (!f.startsWith(root)) { res.writeHead(403); return res.end("no"); }
  fs.readFile(f, (e, d) => {
    if (e && !path.extname(f)) {
      const alt = f + ".html";
      return fs.readFile(alt, (e2, d2) => e2 ? serve404(res) : out(alt, d2, res));
    }
    if (e) return serve404(res);
    out(f, d, res);
  });
}

const PIXEL = fs.readFileSync(path.join(root, "pixel.gif"));

http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split("?")[0]).replace(/\/$/, "");
  if (p === "") p = "/";
  if (p === "/open" && (req.method === "GET" || req.method === "HEAD")) {
    const q = new URLSearchParams(req.url.split("?")[1] || "");
    console.log("OPEN " + SITE + " " + JSON.stringify({ t: (q.get("t") || "").slice(0, 120), ua: (req.headers["user-agent"] || "").slice(0, 60), ts: new Date().toISOString() }));
    res.writeHead(200, Object.assign({ "content-type": "image/gif", "cache-control": "no-store, no-cache, must-revalidate" }, NOINDEX));
    return res.end(PIXEL);
  }
  if (req.url.indexOf("utm_") !== -1) {
    const q = new URLSearchParams(req.url.split("?")[1] || "");
    console.log("CLICK " + SITE + " " + JSON.stringify({ c: (q.get("utm_content") || "").slice(0, 120), path: p.slice(0, 100), ua: (req.headers["user-agent"] || "").slice(0, 60), ts: new Date().toISOString() }));
  }
  if (p === "/healthz") { res.writeHead(200, Object.assign({ "content-type": "text/plain" }, NOINDEX)); return res.end("ok"); }
  if (req.method === "POST" && p === "/contact") {
    if ((req.headers["content-type"] || "").split(";")[0] !== "application/x-www-form-urlencoded") {
      res.writeHead(415, Object.assign({ "content-type": "text/plain" }, NOINDEX)); return res.end("expected a plain form post");
    }
    return readBody(req, (raw) => {
      const F = Object.fromEntries(new URLSearchParams(raw));
      const name = (F.name || "").slice(0, 120), phone = (F.phone || "").slice(0, 60),
            email = (F.email || "").slice(0, 120), message = (F.message || "").slice(0, 4000);
      if (!name.trim() || !message.trim()) {
        res.writeHead(400, Object.assign({ "content-type": "text/plain" }, NOINDEX)); return res.end("name and message are required");
      }
      console.log("CONTACT " + SITE + " " + JSON.stringify({ name, phone, email, message, t: new Date().toISOString() }));
      if (!MAIL_READY) { res.writeHead(503, Object.assign({ "content-type": "text/plain" }, NOINDEX)); return res.end("form mailbox not configured yet"); }
      const payload = {
        sender: { name: SITE, email: MAIL.alias },
        to: [{ email: MAIL.to }],
        subject: `[${SITE}] website contact from ${name}`,
        textContent: `Name: ${name}\nPhone: ${phone || "-"}\nEmail: ${email || "-"}\n\n${message}\n\n— sent via the Songbird site, ${new Date().toISOString()}`,
      };
      if (/^[^@\s]+@[^@\s]+$/.test(email)) payload.replyTo = { email };
      fetch(BREVO_API, {
        method: "POST",
        headers: { "api-key": MAIL.key, "content-type": "application/json" },
        body: JSON.stringify(payload),
      }).then((r) => {
        if (!r.ok) return r.text().then((t) => { throw new Error(`relay HTTP ${r.status}: ${t.slice(0, 200)}`); });
        return r.json();
      }).then((j) => {
        console.log("MAILSENT " + SITE + " " + (j && j.messageId ? j.messageId : "accepted"));
        res.writeHead(303, Object.assign({ location: "/thanks" }, NOINDEX)); res.end();
      }).catch((err) => {
        console.log("MAILERR " + SITE + " " + err.message);
        res.writeHead(502, Object.assign({ "content-type": "text/html; charset=utf-8" }, NOINDEX));
        res.end("<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"utf-8\"><title>Couldn't send just now</title><meta name=\"robots\" content=\"noindex\"></head><body><h1>Couldn't send just now</h1><p>Your note is logged — please try again in a moment, or book an evening table on Resy.</p></body></html>");
      });
    });
  }
  if (req.method === "GET" || req.method === "HEAD") return serveStatic(p, res);
  res.writeHead(405, Object.assign({ "content-type": "text/plain" }, NOINDEX));
  res.end("method not allowed");
}).listen(PORT, () => console.log(SITE + " site on :" + PORT));
