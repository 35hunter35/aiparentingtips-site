# Deploying aiparentingtips.com (free)

**Status:** Nothing is deployed yet. No accounts were created and no DNS was changed. The current records listed in step 4b come from a read-only public DNS lookup on Oct 17, 2026.

**Nameservers:** GitHub Pages (the pick) works with DNS kept at Squarespace, so you **don't** need to move nameservers.

## Recommendation: GitHub Pages

GitHub Pages is the best free option here because it is the only one that does all three of these:

1. It serves the **root domain** `aiparentingtips.com` using plain `A` records at Squarespace. You don't have to move nameservers.
2. It **leaves the Google Workspace MX, SPF, DKIM, and DMARC records alone**. You only add or replace `@` A/AAAA records and the `www` CNAME.
3. It's **$0 with no hard cap**. The limits are a soft 100 GB/month of bandwidth and a 1 GB site, which is far more than a newsletter site uses.

The site is already set up for it: `CNAME` holds `aiparentingtips.com`, `.nojekyll` makes sure `tips/_template.html` (which starts with an underscore) gets published, and `404.html` is picked up automatically.

### How the alternatives compare

| Host | Root domain with DNS kept at Squarespace? | Free-tier catch |
|---|---|---|
| **GitHub Pages** (pick) | Yes: 4 A + 4 AAAA records | The repo must be **public** on a free GitHub account. GitHub's terms say Pages isn't meant to "run your online business, e-commerce site," or SaaS. A free content site with sponsor mentions and no checkout is the normal blog/publication use, but if that line worries you, use Cloudflare Pages. |
| Cloudflare Pages | **No.** A root domain only works if the domain's nameservers move to Cloudflare. With DNS at Squarespace you can use only `www` (a CNAME), and the root has to redirect to it. | Unlimited bandwidth. Moving nameservers means re-creating every Google Workspace record by hand, which is the email risk we wanted to avoid. Best choice if you later move DNS to Cloudflare. |
| Netlify | Yes (A record) | New accounts get **300 credits a month with a hard limit**. When they run out, *every* site pauses ("Site not available") until the next month, and free accounts can't buy more. |

Sources:
- Squarespace: Google Workspace MX records on Squarespace domains: https://support.squarespace.com/hc/en-us/articles/360001476528-Add-Google-Workspace-MX-records-to-your-domain
- Google Workspace DKIM (google._domainkey): https://support.google.com/a/answer/174124
- GitHub Pages custom domains and DNS values: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
- GitHub Pages limits and terms: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- GitHub Pages HTTPS: https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https
- Cloudflare Pages custom domains (root domain needs a Cloudflare zone): https://developers.cloudflare.com/pages/configuration/custom-domains/
- Netlify credit limits: https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work/
- Squarespace DNS records and "Squarespace Defaults": https://support.squarespace.com/hc/en-us/articles/31119879125645-DNS-records-for-web-hosting

---

## Step-by-step (GitHub Pages)

### 1. Create the GitHub account and repo (Adam)
1. Sign up at https://github.com/signup. Use the business email if you like, and turn on 2FA.
2. Optional: create a free **organization** called `aiparentingtips` so the repo lives under the brand. (Profile menu > Your organizations > New organization > Free.)
3. Create a **public** repository, e.g. `aiparentingtips-site`. Don't add a README.

### 2. Upload the site
Push everything in this folder **except `screens/` and `DEPLOY.md`** (pushing them does no harm either):
```bash
cd /workspace/aiparentingtips-site
git init -b main
git add .
git commit -m "Launch AI Parenting Tips site"
git remote add origin https://github.com/<OWNER>/aiparentingtips-site.git
git push -u origin main
```
(Or on github.com: **Add file > Upload files** and drag in the folder contents. Include the hidden `.nojekyll` and `CNAME` files.)

### 3. Turn on Pages
Repo > **Settings > Pages**:
- **Source:** Deploy from a branch. **Branch:** `main`, folder `/ (root)` > Save.
- **Custom domain:** `aiparentingtips.com` > Save. It will say the DNS check is failing until step 4 is done, which is normal.
- Recommended: verify the domain first so nobody else can claim it on GitHub. Profile/Org **Settings > Pages > Add a domain** gives you a `TXT` record (`_github-pages-challenge-<owner>`); add it in step 4 too.

### 4. DNS at Squarespace Domains (keep DNS at Squarespace, no nameserver move)

**GitHub Pages does NOT require moving nameservers.** The domain stays on Squarespace's nameservers (`nsb1`–`nsb4.squarespacedns.com`). You only edit records for `@` and `www`. Don't touch the **Nameservers** section, and don't switch to "custom nameservers". If you do, every record below, including email, stops working.

#### 4a. Open the DNS panel
aiparentingtips.com was bought during Google Workspace signup, so it's registered at Squarespace Domains under your Workspace account. Either path opens the same screen:
- **From Google:** https://admin.google.com > **Account > Domains > Manage domains** > next to aiparentingtips.com click **View details** > **Manage domain** (on some accounts it's labeled **Advanced DNS settings**). This signs you in to Squarespace Domains.
- **Directly:** https://account.squarespace.com/domains > **Continue with Google** using your Workspace admin account (the one you bought the domain with) > **aiparentingtips.com** > **DNS** > **DNS Settings**.

Deleting a preset makes Squarespace ask you to sign in again (password or 2FA). That's expected.

#### 4b. What's there now (public DNS lookup on Oct 17, 2026)
| Host | Type | Value | Belongs to | Action |
|---|---|---|---|---|
| `@` | MX | `1 smtp.google.com` | Google Workspace mail | **KEEP, don't touch** |
| `@` | TXT | `v=spf1 include:_spf.google.com ~all` | Google Workspace SPF | **KEEP, don't touch** |
| `google._domainkey` | TXT | `v=DKIM1; k=rsa; p=MIIBIjANBgkq…IDAQAB` | Google Workspace DKIM | **KEEP, don't touch** |
| `@` | A | `198.185.159.144` | Squarespace Defaults (parking/site) | **REMOVE** |
| `@` | A | `198.185.159.145` | Squarespace Defaults | **REMOVE** |
| `@` | A | `198.49.23.144` | Squarespace Defaults | **REMOVE** |
| `@` | A | `198.49.23.145` | Squarespace Defaults | **REMOVE** |
| `www` | CNAME | `ext-sq.squarespace.com` | Squarespace Defaults | **REMOVE** |

There's no `_dmarc` record and no `@` `google-site-verification=` TXT in public DNS. Google verifies domains bought through Workspace automatically. If the panel *does* show a `google-site-verification` TXT, or a CNAME such as `mail`/`calendar`/`drive` pointing to `ghs.googlehosted.com`, or a random-looking verification CNAME pointing to `gv-….dv.googlehosted.com`, **keep those too**.

Rule of thumb: **leave every MX record, every TXT record, and anything inside the "Google Workspace" preset.** Only remove records whose host is `@` or `www` **and** whose type is A, AAAA, or CNAME, or that sit inside the **Squarespace Defaults** preset.

#### 4c. Remove the conflicting Squarespace parking records
1. In **DNS Settings**, find the **Squarespace Defaults** block (the four `@` A records and `www` → `ext-sq.squarespace.com`).
2. Click the **red trash can** next to *Squarespace Defaults* > sign in again > **Delete**. Leave the **Google Workspace** block alone.
3. If any `@`/`www` A, AAAA, or CNAME records are still listed under **Custom records**, delete them one by one with their trash icons.
4. If **Domain forwarding** (sometimes called *Website forwarding*) is set for `aiparentingtips.com` or `www`, delete it. Don't touch **Email forwarding**, though there probably isn't any because Workspace handles mail.

Squarespace won't let you add a `www` CNAME while another `www` record exists, so this step has to come first.

#### 4d. Add the GitHub Pages records
Under **Custom records** > **Add record**, one at a time (TTL: leave the default, or 1 hr):

| Host | Type | Data |
|---|---|---|
| `@` | A | `185.199.108.153` |
| `@` | A | `185.199.109.153` |
| `@` | A | `185.199.110.153` |
| `@` | A | `185.199.111.153` |
| `@` | AAAA | `2606:50c0:8000::153` |
| `@` | AAAA | `2606:50c0:8001::153` |
| `@` | AAAA | `2606:50c0:8002::153` |
| `@` | AAAA | `2606:50c0:8003::153` |
| `www` | CNAME | `<OWNER>.github.io` (your GitHub username or org, e.g. `aiparentingtips.github.io`; no repo name) |
| `_github-pages-challenge-<OWNER>` | TXT | *optional:* value from GitHub > Settings > Pages > Add a domain (stops anyone else claiming the domain on GitHub) |

How the domains behave: `aiparentingtips.com` (the root, or "apex") serves the site. `www.aiparentingtips.com` gets an automatic 301 redirect to the root from GitHub, because the repo's `CNAME` file says `aiparentingtips.com`.

Optional, but good for email deliverability (it doesn't affect the website): add `_dmarc` TXT `v=DMARC1; p=none; rua=mailto:hello@aiparentingtips.com`. beehiiv sends from its own domain (`mail.beehiiv.com`), so this doesn't affect the newsletter.

#### 4e. Expected result
Afterwards the zone should contain exactly the Google Workspace records from 4b (MX, SPF, DKIM, plus any verification records), the 8 GitHub `@` A/AAAA records, and the `www` CNAME. Nothing else should exist for `@` or `www`.

### 5. HTTPS and checks
1. Wait for DNS. Usually that's minutes, but it can take up to 24–48 hours. Check with `dig +short aiparentingtips.com` (should return the 185.199.x.153 addresses), `dig +short MX aiparentingtips.com` (should still be `1 smtp.google.com.`) and `dig +short TXT google._domainkey.aiparentingtips.com` (DKIM key still there). Without `dig`, use https://dns.google/resolve?name=aiparentingtips.com&type=MX.
2. Settings > Pages: when the check mark shows, tick **Enforce HTTPS**. The Let's Encrypt certificate can take up to about an hour.
3. Send a test email to the Workspace inbox to confirm mail still arrives.
4. Open https://aiparentingtips.com, /about.html, /tips/, and a made-up URL (it should show the 404 page).

### 6. After launch
- **Google Search Console:** add a *Domain* property for `aiparentingtips.com` and verify with the TXT record it gives you (add it at Squarespace). Then submit `https://aiparentingtips.com/sitemap.xml`.
- **Bing Webmaster Tools:** import from Search Console, then submit the same sitemap.
- Check the social preview with X's post composer or https://www.opengraph.xyz/.

### Plan B: Cloudflare Pages
Only if you decide to move DNS to Cloudflare (registration can stay at Squarespace). Add the domain to a free Cloudflare account and **check every Google Workspace record (MX, SPF, DKIM, DMARC, verification TXT) was imported** before changing the nameservers at Squarespace. Then: Workers & Pages > Create > Pages > upload this folder (or connect the repo; no build command, output directory `/`) > Custom domains > `aiparentingtips.com`. Delete `CNAME` and `.nojekyll` (they're GitHub-only and harmless).

---

## Hooking up the beehiiv signup form
The forms on `index.html` and `about.html` currently use a **fallback**: a normal form that sends visitors to `https://aiparentingtips.beehiiv.com/subscribe` (with `?email=` added). It works with no setup, but visitors may have to type their email again on beehiiv's page.

For one-click signup on the site itself (free plan supported, per beehiiv's help article "Creating an embedded subscribe form"):
1. beehiiv dashboard > **Subscribers > Subscribe forms > Create new form**.
2. Content tab: set the button text to **Get the free tips**. Style tab > Embed: **Layout: Slim** (or Regular, which is better on mobile), **Embed type: Inline**. Colors: button `#E4572E`, text `#FFFFFF`.
3. Settings tab: show a success message, or redirect to `https://aiparentingtips.com/?subscribed=1`.
4. **Save & get embed code** and copy the single `<script>` tag.
5. In `index.html` (2 spots) and `about.html` (1 spot), paste it inside `<div class="beehiiv-embed"></div>` and delete the `<form class="fallback-form">…</form>` that follows. Search for `BEEHIIV EMBED PLACEHOLDER`.

## Publishing a new issue page
Copy `tips/_template.html` to `tips/<keyword-slug>.html` and follow the comment at the top of the file: replace the REPLACE markers, switch robots to `index,follow`, and add the page to `tips/index.html` and `sitemap.xml`.
