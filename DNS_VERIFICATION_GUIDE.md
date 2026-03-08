# DNS Configuration Verification Guide

## Correct DNS Settings for relaylaunch.com on Porkbun

Your DNS settings should look **exactly** like this in Porkbun:

### ✅ Configuration Option 1: A Records for Apex Domain (Recommended)

| Type | Host | Answer/Value | TTL | Priority |
|------|------|--------------|-----|----------|
| A | @ (or blank) | `185.199.108.153` | 600 (or auto) | - |
| A | @ (or blank) | `185.199.109.153` | 600 (or auto) | - |
| A | @ (or blank) | `185.199.110.153` | 600 (or auto) | - |
| A | @ (or blank) | `185.199.111.153` | 600 (or auto) | - |

**Optional but recommended - Add www subdomain:**

| Type | Host | Answer/Value | TTL | Priority |
|------|------|--------------|-----|----------|
| CNAME | www | `relay-launch.github.io` | 600 (or auto) | - |

### 📋 Common Porkbun Field Names

Different DNS providers use different terminology. Here's what Porkbun uses:

- **Type**: The record type (A, CNAME, etc.)
- **Host**: The subdomain or "@" for root domain
  - Use **@** or leave **blank** for the apex/root domain (relaylaunch.com)
  - Use **www** for the www subdomain (www.relaylaunch.com)
- **Answer**: The IP address or destination
  - For A records: The GitHub Pages IP addresses
  - For CNAME: `relay-launch.github.io` (without https://)
- **TTL**: Time to live (usually 600 or "auto")
- **Priority**: Only for MX records, leave blank for A and CNAME

## ✅ What Your Screenshot Should Show

Your Porkbun DNS settings should show:

**For the 4 A records:**
- **4 separate rows** (not one row with 4 IPs)
- Each row with Type = **A**
- Host = **@** (or blank, or "relaylaunch.com")
- Answer = one of these IPs:
  - `185.199.108.153`
  - `185.199.109.153`
  - `185.199.110.153`
  - `185.199.111.153`

**For the CNAME (optional but recommended):**
- Type = **CNAME**
- Host = **www**
- Answer = **relay-launch.github.io** (NO trailing dot, NO https://)

## ❌ Common Mistakes to Avoid

### Mistake 1: All 4 IPs in One Record
❌ **WRONG:**
```
Type: A
Host: @
Answer: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
```

✅ **CORRECT:**
```
Type: A, Host: @, Answer: 185.199.108.153
Type: A, Host: @, Answer: 185.199.109.153
Type: A, Host: @, Answer: 185.199.110.153
Type: A, Host: @, Answer: 185.199.111.153
```

### Mistake 2: Wrong Host Value
❌ **WRONG:**
```
Host: relaylaunch.com (full domain)
Host: * (wildcard)
Host: (empty when it should be @)
```

✅ **CORRECT:**
```
Host: @ (or blank, depending on Porkbun's interface)
```

### Mistake 3: Wrong CNAME Target
❌ **WRONG:**
```
Answer: https://relay-launch.github.io
Answer: relay-launch.github.io.
Answer: github.io
Answer: relaylaunch-website.github.io
```

✅ **CORRECT:**
```
Answer: relay-launch.github.io (no protocol, no trailing dot)
```

### Mistake 4: CNAME for Root Domain
❌ **WRONG:**
```
Type: CNAME
Host: @
Answer: relay-launch.github.io
```

✅ **CORRECT:**
```
Use A records for @ (root domain)
Use CNAME only for www subdomain
```

## 🔍 How to Verify Your Configuration

### Step 1: Visual Inspection

Look at your Porkbun screenshot and count:
- [ ] Do you have exactly **4 A records**?
- [ ] Do all 4 A records have Host = **@** (or blank)?
- [ ] Do the 4 A records have these **exact IP addresses**?
  - [ ] `185.199.108.153`
  - [ ] `185.199.109.153`
  - [ ] `185.199.110.153`
  - [ ] `185.199.111.153`
- [ ] (Optional) Do you have **1 CNAME record** for **www**?
- [ ] Does the CNAME point to **relay-launch.github.io** (no protocol, no trailing dot)?

### Step 2: Command Line Verification

After saving your DNS records, wait 5-10 minutes, then run these commands:

**Check A records:**
```bash
dig relaylaunch.com +short
```

**Expected output (all 4 IPs, order doesn't matter):**
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**Check CNAME:**
```bash
dig www.relaylaunch.com +short
```

**Expected output:**
```
relay-launch.github.io.
<one or more of the GitHub IPs>
```

### Step 3: Online DNS Checker

Use one of these online tools to verify:
- https://dnschecker.org (check from multiple locations worldwide)
- https://www.whatsmydns.net
- https://mxtoolbox.com/DNSLookup.aspx

Enter `relaylaunch.com` and check that A records show the 4 GitHub IPs.

## 📝 Specific Instructions for Porkbun

If you're setting this up in Porkbun for the first time:

1. **Log in to Porkbun** → Account → Domain Management
2. **Find relaylaunch.com** → Click "DNS"
3. **Delete any conflicting records:**
   - Delete any existing A records for "@" that point to other IPs
   - Delete any CNAME records for "@" (root domain)
   - Delete any old parking page records
4. **Add the 4 A records:**
   - Click "+ Add" or "Add Record"
   - Type: **A**
   - Host: **@** (if Porkbun asks, or leave blank)
   - Answer: **185.199.108.153**
   - Click Save
   - Repeat 3 more times for the other 3 IPs
5. **Add the CNAME record (optional):**
   - Click "+ Add" or "Add Record"
   - Type: **CNAME**
   - Host: **www**
   - Answer: **relay-launch.github.io**
   - Click Save
6. **Wait for DNS propagation** (5 minutes to 48 hours)

## 🕐 DNS Propagation Timeline

- **Porkbun to internet**: 5-10 minutes (usually fast)
- **Full global propagation**: Up to 48 hours
- **Most users will see changes**: Within 2-4 hours

## ✅ Verification Checklist

Use this checklist to verify your configuration from your screenshot:

### A Records (All 4 Required)
- [ ] Record 1: Type=A, Host=@, Answer=185.199.108.153
- [ ] Record 2: Type=A, Host=@, Answer=185.199.109.153
- [ ] Record 3: Type=A, Host=@, Answer=185.199.110.153
- [ ] Record 4: Type=A, Host=@, Answer=185.199.111.153

### CNAME Record (Optional but Recommended)
- [ ] Record 5: Type=CNAME, Host=www, Answer=relay-launch.github.io

### No Conflicting Records
- [ ] No other A records for "@" with different IPs
- [ ] No CNAME records for "@" (root domain)
- [ ] No ALIAS or ANAME records for "@"

## 🚨 If Your Screenshot Doesn't Match

If your screenshot shows something different from the configuration above:

1. **Delete the incorrect records** in Porkbun
2. **Add the correct records** as shown above
3. **Save your changes**
4. **Wait 10 minutes** for propagation
5. **Test with `dig relaylaunch.com`** or online DNS checker

## 📧 What to Send for Review

To get confirmation your DNS is correct, share:

1. **Screenshot showing:**
   - All DNS records for relaylaunch.com
   - The Type, Host, and Answer columns visible
   - All 4 A records and the CNAME visible

2. **Output of these commands:**
   ```bash
   dig relaylaunch.com +short
   dig www.relaylaunch.com +short
   ```

3. **Or use online checker:**
   - Go to https://dnschecker.org
   - Enter `relaylaunch.com`
   - Select "A" record type
   - Take screenshot showing the results

## 🎯 Quick Answer: Is Your DNS Correct?

Based on your screenshot, your DNS is correct if you see:

✅ **YES, your DNS is correct if:**
- You have 4 separate A records (not combined)
- All 4 have Host = "@" or blank
- All 4 have the exact GitHub IPs listed above
- Your CNAME (if present) points to relay-launch.github.io

❌ **NO, your DNS needs fixing if:**
- You have fewer than 4 A records
- The IPs don't match the GitHub IPs exactly
- The Host field is not "@" or blank for A records
- You have a CNAME for "@" instead of A records
- The CNAME points to the wrong domain

## Next Steps After DNS is Correct

Once your DNS is verified correct:

1. ✅ **Enable GitHub Pages** in repository settings (if not done yet)
2. ⏳ **Wait for DNS propagation** (up to 48 hours, usually faster)
3. 🔄 **Trigger the workflow** or merge a PR to deploy
4. 🌐 **Visit https://relaylaunch.com** to verify it's live

The DNS configuration is only **one part** of the puzzle. You also need:
- GitHub Pages enabled (Settings → Pages → Source: "GitHub Actions")
- Custom domain set to "relaylaunch.com" in GitHub Pages settings
- At least one successful workflow run

See **NEXT_STEPS.md** for the complete deployment checklist.

---

**Need help?** Share your screenshot with the checklist above completed, and we can confirm if your DNS is configured correctly!
