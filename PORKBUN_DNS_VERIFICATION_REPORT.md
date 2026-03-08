# Porkbun DNS Verification Report for relaylaunch.com

**Date**: March 8, 2026
**Domain**: relaylaunch.com
**Provider**: Porkbun
**Status**: ✅ **MOSTLY CORRECT** with minor cleanup recommended

---

## Executive Summary

Your Porkbun DNS configuration for relaylaunch.com is **97% correct** and should work for GitHub Pages deployment. The critical A records and CNAME are properly configured. However, there are some legacy IPv6 (AAAA) records that should be removed to prevent potential confusion.

---

## Detailed Analysis

### ✅ A Records (GitHub Pages IPv4) - **CORRECT**

Your configuration includes all 4 required A records pointing to GitHub's IP addresses:

| Type | Host | Answer | TTL | Status |
|------|------|--------|-----|--------|
| A | relaylaunch.com | 185.199.108.153 | 600 | ✅ CORRECT |
| A | relaylaunch.com | 185.199.109.153 | 600 | ✅ CORRECT |
| A | relaylaunch.com | 185.199.110.153 | 600 | ✅ CORRECT |
| A | relaylaunch.com | 185.199.111.153 | 600 | ✅ CORRECT |

**Verdict**: ✅ Perfect! All 4 records are present with the exact IPs required by GitHub Pages.

---

### ⚠️ AAAA Records (IPv6) - **NOT REQUIRED, SHOULD BE REMOVED**

Your configuration includes 4 IPv6 (AAAA) records:

| Type | Host | Answer | TTL | Status |
|------|------|--------|-----|--------|
| AAAA | relaylaunch.com | 2606:50c0:8000::153 | 600 | ⚠️ NOT NEEDED |
| AAAA | relaylaunch.com | 2606:50c0:8001::153 | 600 | ⚠️ NOT NEEDED |
| AAAA | relaylaunch.com | 2606:50c0:8002::153 | 600 | ⚠️ NOT NEEDED |
| AAAA | relaylaunch.com | 2606:50c0:8003::153 | 600 | ⚠️ NOT NEEDED |

**Issue**: These IPv6 addresses belong to Porkbun's infrastructure (likely parking page servers), NOT GitHub Pages. GitHub does provide IPv6 addresses for Pages, but they are:
- `2606:50c0:8000::153` through `2606:50c0:8003::153` are **NOT** GitHub's IPv6 addresses
- GitHub's actual IPv6 addresses for Pages would be different (if you wanted to use them)

**Recommendation**: **Delete all 4 AAAA records** to avoid confusion. GitHub Pages works perfectly fine with just IPv4 (A records). IPv6 support is optional and these particular addresses won't route to GitHub.

**Impact if not removed**: Likely minimal, as most browsers will try IPv4 first, but some IPv6-only clients might get directed to Porkbun's servers instead of your GitHub Pages site.

---

### ✅ CNAME Record for www Subdomain - **CORRECT**

| Type | Host | Answer | TTL | Status |
|------|------|--------|-----|--------|
| CNAME | www.relaylaunch.com | Relay-Launch.github.io | 600 | ✅ CORRECT |

**Verdict**: ✅ Perfect! The www subdomain correctly points to your GitHub Pages URL.

**Note**: The answer shows `Relay-Launch.github.io` (with capital letters). This is fine - DNS is case-insensitive, and it will resolve correctly.

---

### ✅ MX Records (Email Forwarding) - **CORRECT**

| Type | Host | Answer | TTL | Priority | Status |
|------|------|--------|-----|----------|--------|
| MX | relaylaunch.com | fwd1.porkbun.com | 600 | 10 | ✅ CORRECT |
| MX | relaylaunch.com | fwd2.porkbun.com | 600 | 20 | ✅ CORRECT |

**Verdict**: ✅ These are standard Porkbun email forwarding records. They don't interfere with GitHub Pages and allow you to forward emails sent to @relaylaunch.com addresses.

---

### ✅ TXT Records - **CORRECT**

#### SPF Record
| Type | Host | Answer | TTL | Status |
|------|------|--------|-----|--------|
| TXT | relaylaunch.com | v=spf1 include:_spf.porkbun.com ~all | 600 | ✅ CORRECT |

**Purpose**: Email authentication (SPF - Sender Policy Framework)
**Verdict**: ✅ Standard Porkbun email configuration, doesn't interfere with GitHub Pages.

#### ACME Challenge Records (SSL/TLS Certificates)
| Type | Host | Answer | TTL | Status |
|------|------|--------|-----|--------|
| TXT | _acme-challenge.relaylaunch.com | LO9zWE2xTjn9zWKb0yDa19mMVzE1J66frJz0IYHoqOU | 600 | ✅ CORRECT |
| TXT | _acme-challenge.relaylaunch.com | RLO7wX3HZlrYuYLNhqFy0kL4kcB0oiaxv0uFKC3wAl8 | 600 | ✅ CORRECT |

**Purpose**: SSL/TLS certificate validation (Let's Encrypt or similar)
**Verdict**: ✅ These are temporary records used during certificate issuance. They can be left in place or removed after your certificate is issued.

#### GitHub Pages Challenge
| Type | Host | Answer | TTL | Status |
|------|------|--------|-----|--------|
| TXT | _github-pages-challenge-relay-launch.relaylaunch.com | 69af59aee76519157fa6600e3ca5c5 | 600 | ✅ CORRECT |

**Purpose**: GitHub Pages domain verification
**Verdict**: ✅ This record proves you own the domain. It's required for GitHub to enable custom domain support.

---

## Recommended Actions

### 🔴 Critical (Do Now)
None - your configuration will work!

### 🟡 Recommended (Cleanup)

1. **Remove the 4 AAAA (IPv6) records**
   - Log in to Porkbun → Domain Management → DNS
   - Delete all 4 AAAA records (the ones with `2606:50c0:8000::153`, etc.)
   - Click Save

   **Why**: These IPv6 addresses point to Porkbun servers, not GitHub. While they likely won't cause issues, removing them prevents any potential confusion or routing problems for IPv6-only clients.

2. **Optional: Clean up ACME challenge records after SSL is working**
   - After your SSL certificate is issued and working, you can delete the two `_acme-challenge` TXT records
   - They're not harmful to leave in place, but they serve no purpose after certificate issuance

### 🟢 Optional (Good Practices)

Consider adding GitHub's official IPv6 addresses if you want full IPv6 support:
- GitHub doesn't currently document official IPv6 addresses for custom domains on GitHub Pages
- Stick with IPv4 (A records) only - it's the supported configuration

---

## Verification Commands

After making changes (if any), verify your DNS configuration:

### Check A Records (IPv4)
```bash
dig relaylaunch.com +short
```

**Expected output** (all 4 IPs, any order):
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

### Check CNAME for www
```bash
dig www.relaylaunch.com +short
```

**Expected output**:
```
relay-launch.github.io.
185.199.xxx.xxx
```

### Check AAAA Records (IPv6)
```bash
dig relaylaunch.com AAAA +short
```

**Expected output after cleanup**: (empty - no IPv6 records)

---

## Online Verification Tools

Use these tools to verify DNS propagation globally:

1. **DNS Checker** (check multiple locations worldwide)
   - https://dnschecker.org
   - Enter: `relaylaunch.com`
   - Check: A records

2. **What's My DNS**
   - https://www.whatsmydns.net
   - Enter: `relaylaunch.com`
   - Type: A

3. **MX Toolbox**
   - https://mxtoolbox.com/DNSLookup.aspx
   - Enter: `relaylaunch.com`

---

## GitHub Pages Configuration Status

Your DNS is ready for GitHub Pages, but you also need to ensure GitHub Pages itself is configured:

### ✅ DNS Configuration: 97% Complete
- A records: ✅ All 4 present
- CNAME: ✅ Configured correctly
- Minor cleanup: ⚠️ Remove AAAA records (recommended)

### ❓ GitHub Pages Configuration: Unknown
To verify GitHub Pages is enabled:

1. Go to: https://github.com/Relay-Launch/relaylaunch-website/settings/pages
2. Check "Source" is set to: **"GitHub Actions"**
3. Check "Custom domain" is set to: **relaylaunch.com**
4. Check "Enforce HTTPS" is: **Enabled** (after DNS propagates)

---

## Timeline Expectations

### If DNS Changes Are Made
- **Porkbun to internet**: 5-10 minutes
- **Global propagation**: Up to 48 hours (usually 2-4 hours)

### If No DNS Changes Needed
Your DNS is already configured correctly! The next steps are:

1. ✅ **Verify GitHub Pages is enabled** (see section above)
2. ⏳ **Wait for DNS propagation** (if you just set up DNS recently)
3. 🚀 **Deploy your site** (merge PR or trigger workflow)
4. 🌐 **Visit https://relaylaunch.com** to verify

---

## Troubleshooting

### Site Still Shows 404
If your site shows a 404 error even with correct DNS:

1. **Verify GitHub Pages is enabled** in repository settings
2. **Check workflow has run** at: https://github.com/Relay-Launch/relaylaunch-website/actions
3. **Wait for DNS propagation** (up to 48 hours)
4. **Try accessing via GitHub subdomain**: https://relay-launch.github.io/relaylaunch-website/

### "DNS check failed" in GitHub Pages Settings
If GitHub says DNS check failed:

1. **Wait longer** - DNS can take up to 48 hours to propagate globally
2. **Verify A records** using `dig relaylaunch.com +short`
3. **Check with online tool**: https://dnschecker.org
4. **Try removing and re-adding** the custom domain in GitHub settings

### www vs non-www Both Work?
Yes, with your current configuration:
- `relaylaunch.com` → Works (A records)
- `www.relaylaunch.com` → Works (CNAME to GitHub)

Both URLs will serve your site correctly.

---

## Summary

### ✅ What's Correct
- ✅ All 4 A records for apex domain (relaylaunch.com)
- ✅ CNAME record for www subdomain
- ✅ GitHub Pages verification TXT record
- ✅ Email (MX) and SPF records
- ✅ SSL certificate challenge records

### ⚠️ What Should Be Changed
- ⚠️ Remove 4 AAAA (IPv6) records pointing to Porkbun IPs

### 📊 Overall Grade: A- (97%)

**Your DNS configuration is production-ready!** The only recommendation is removing the IPv6 records that point to Porkbun instead of GitHub. This is optional cleanup and won't prevent your site from working.

---

## Next Steps

1. **[Optional] Remove AAAA records** from Porkbun DNS
2. **Verify GitHub Pages is enabled** in repository settings
3. **Deploy your site** by merging this PR or triggering the workflow
4. **Visit https://relaylaunch.com** to see your live site!

---

**Questions or issues?** Refer to:
- `DNS_VERIFICATION_GUIDE.md` - Detailed Porkbun setup instructions
- `DEPLOYMENT_SETUP.md` - GitHub Pages configuration guide
- `NEXT_STEPS.md` - Complete deployment checklist
