# DEPLOY — songbird (t_fbffb777)

Built 2026-11-26. 9-page template-v2 site for Songbird, daylight-to-dusk bar,
1020 E Whitaker Mill Rd Ste 130 (East End Market), Raleigh NC 27608.

- Repo: github.com/gnaritas/songbird (public, identity-clean, no secrets)
- Railway: service `songbird` (id 999f8d3c-6f58-4acb-aea0-f7cf50f0e289) co-hosted
  inside shell project honeyspell-cafe (5be9a2cb-4597-48ed-9368-e8fb587aa71b) —
  account project cap (account-wide), co-host doctrine. Domain moved to
  `songbird-demo.up.railway.app` (domain id 3fa44277-bfb6-4fca-9b59-8be9dd8209ba).
- Variables: BREVO_API_KEY (xkeysib…, extracted post-token), MAIL_ALIAS
  jarvis+websites@onsmalltalk.com, MAIL_TO same, PORT 3000. Form relay proven:
  POST /contact → 303 /thanks, MAILSENT read-back in lane mailbox 2026-11-26.
- Verified: _verify.py PASS (0 fail/0 warn); 14-path 200-walk; live==local
  sha256 on all 14 assets; custom 404 live; X-Robots-Tag noindex on pages;
  /open?t= pixel 200 image/gif 43B; 58/58 sibling hosts 200 after co-host add.
- Render sweep: 18 shots (9 pages × 1280/390) PASS — 0 overflow, 0 console
  errors. Vision adjudication fixes applied + redeployed: evening-band hours
  line contrast, flex tiles (bottom-pinned links), visit FAQ moved to a
  full-width band (columns balanced 550/563px), map iframe un-lazied.
  Google embed tiles proven rendering via CDP clip capture (streets + marker +
  place card for the exact address); blank-box in headless capture = harness
  artifact — identical behavior on shipped sibling sites.
- lane.db: deploys + services rows written via sites_agency_state.py; export +
  verify IDENTICAL 2026-11-26.
- Pitch: prepared 2026-11-26 (v6 arm, coin even; founder bundle link; recipient
  meg@umbrelladrybar.com, America/New_York seeded in shop_tz). Send held for
  recipient window — park SCHEDULED_UNTIL 2026-11-28T07:30:00-05:00 (Thanksgiving
  pair 11-26/27 skipped). Send leg = `python3 ../../_pitch_songbird.send.py`
  (envelope-resume safe; check-only passed 110 words).
