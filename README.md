# Isha ❤️ Proposal Website

A single-file, fully functional, animated romantic proposal website.

## Deploy it live with GitHub Pages (recommended — this is what lets a QR code work)

1. Create a new **public** GitHub repo (e.g. `isha-proposal`).
2. Push this whole folder to it:
   ```bash
   cd isha_proposal
   git init
   git add .
   git commit -m "Isha proposal website"
   git branch -M main
   git remote add origin https://github.com/<your-username>/isha-proposal.git
   git push -u origin main
   ```
3. On GitHub: go to **Settings → Pages → Build and deployment → Source**, and select
   **"GitHub Actions"**.
4. That's it — the included workflow at `.github/workflows/deploy.yml` runs
   automatically on every push to `main` and publishes `index.html` live at:
   ```
   https://<your-username>.github.io/isha-proposal/
   ```
   Check the **Actions** tab for build status; the live URL also appears there
   once the deploy finishes (takes ~30–60 seconds).
5. Generate a QR code for that URL (see below) and share it however you like —
   text, print it, etc. Anyone who scans it opens the live site directly.

## How to run locally

1. Open the `isha_proposal` folder in **VS Code**.
2. Easiest: right-click `index.html` → **"Open with Live Server"** (install the
   *Live Server* extension if you don't have it), or just **double-click
   `index.html`** to open it in your browser.
3. That's it — no build step, no dependencies.

## Adding background music

The music button works, but no audio file is bundled (to avoid using
copyrighted music). To enable it:

1. Add your own royalty-free `.mp3` file to the `assets/` folder, e.g.
   `assets/romantic-bg.mp3`.
2. In `index.html`, find this line inside the `<audio>` tag and uncomment it:
   ```html
   <source src="assets/romantic-bg.mp3" type="audio/mpeg">
   ```

## What's inside

- **Page 1 — Proposal**: YES / NO buttons. YES triggers a heart burst and
  moves to the shayari page. NO is playful (dodges on mouse hover / first
  couple of mobile taps) but is **always keyboard-reachable** and never
  blocks the choice — clicking it goes straight to a warm, non-guilt-inducing
  response page with "Go Back" / "Close" options.
- **Page 2 — Shayari**: 4 original Hindi shayaris, revealed one at a time
  with a fade-in animation.
- **Page 3 — Celebration**: "SHE SAID YES!" with a floating-hearts background.
- **Page 4 — Mini Games**: Quiz ("How Well Do You Know Me?"), Catch the
  Hearts (30-second click game), and a Memory Match game (emoji pairs).
- **Page 5 — Final Message**: the personal Hindi + English message, signed
  by Krish.
- **Closing screens**: separate, distinct endings depending on whether Isha
  chose YES or NO, ending on a calm, pressure-free final screen either way.

## Accessibility

- All interactive elements are real `<button>`s — fully keyboard operable
  (Tab + Enter/Space).
- Visible focus outlines (`:focus-visible`).
- The NO button only dodges on **mouse hover**, never on keyboard focus, so
  keyboard users can always reach and activate it.
- Respects `prefers-reduced-motion`: disables floating particles, heart
  bursts, falling hearts, and the NO-button dodge, replacing them with plain,
  non-animated states.
- Icon-only buttons (music toggle) have `aria-label`s that update with state.
- The NO button's playful messages are announced via `aria-live="polite"`.
- Text/background color pairs were chosen for solid contrast (dark ink text
  on light pink/white glass panels).

## Customizing

- **Quiz questions**: edit the `quizQuestions` array near the bottom of the
  `<script>` block in `index.html`.
- **Shayaris**: edit the `shayaris` array.
- **Colors**: edit the CSS custom properties at the top of `<style>`
  (`--pink`, `--red`, `--purple`, etc.).
