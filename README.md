# TipRun Rubbish Removal — Static Site

56 files: homepage, 50 suburb pages, locations index, 404, sitemap.xml, robots.txt.

## Before you publish (important)
1. Open `generate.py` and edit the CONFIG block at the top:
   - PHONE / PHONE_A  -> your real number
   - BASE_URL         -> your real GitHub Pages URL (or custom domain)
   - FORM_URL         -> your Formspree endpoint (see below)
   - BIZ              -> your business name
2. Run `python3 generate.py` — this rebuilds every page with your details.
3. Replace the placeholder ABN in the footer (search "00 000 000 000").

## Enquiry form setup (Formspree — free)
GitHub Pages can't process forms itself, so the form posts to Formspree:
1. Sign up free at https://formspree.io (50 submissions/month on the free plan).
2. Create a new form -> copy the endpoint (looks like https://formspree.io/f/abcdwxyz).
3. Paste it into FORM_URL in generate.py and re-run the script.
4. Enquiries arrive in your email with name, phone, suburb and job details.
Tip: in Formspree settings, set a redirect "thank you" URL back to your site.

## Deploy on GitHub Pages
1. Create a repo, push this whole folder.
2. Repo Settings -> Pages -> Source: "Deploy from a branch" -> branch `main`, folder `/docs`.
3. Wait ~2 min, your site is live at https://USERNAME.github.io/REPONAME/
4. Submit sitemap.xml in Google Search Console (verify your site there first).

## SEO checklist after launch
- Google Search Console: verify + submit sitemap
- Buy a custom domain (e.g. tiprunrubbish.com.au) — ranks far better than github.io
- Add real photos of jobs/trucks per suburb over time (biggest ranking lever)
- Get listed in local directories (TrueLocal, Yellow Pages, StartLocal)

## Adding suburbs
Add a dict to SUBURBS in generate.py (write a genuinely unique `note` for each — 
this is what keeps pages from looking like doorway spam) and re-run the script.
