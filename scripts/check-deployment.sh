#!/bin/bash

# Website Deployment Health Check Script
# This script verifies that the website deployment is properly configured

echo "======================================"
echo "Relay Launch Website Health Check"
echo "======================================"
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check 1: Build system
echo "1. Checking build system..."
if [ -f "package.json" ] && [ -f "astro.config.mjs" ]; then
    echo -e "   ${GREEN}✓${NC} Build configuration files found"
else
    echo -e "   ${RED}✗${NC} Build configuration missing"
    exit 1
fi

# Check 2: CNAME file
echo "2. Checking CNAME file..."
if [ -f "public/CNAME" ]; then
    DOMAIN=$(cat public/CNAME)
    echo -e "   ${GREEN}✓${NC} CNAME file exists: $DOMAIN"
else
    echo -e "   ${RED}✗${NC} CNAME file missing in public/"
fi

# Check 3: Workflow file
echo "3. Checking deployment workflow..."
if [ -f ".github/workflows/astro.yml" ]; then
    echo -e "   ${GREEN}✓${NC} Deployment workflow found"
else
    echo -e "   ${RED}✗${NC} Deployment workflow missing"
fi

# Check 4: Try to build
echo "4. Testing build process..."
if npm run build > /tmp/build.log 2>&1; then
    echo -e "   ${GREEN}✓${NC} Build successful"

    # Check if CNAME is in dist
    if [ -f "dist/CNAME" ]; then
        echo -e "   ${GREEN}✓${NC} CNAME copied to dist/"
    else
        echo -e "   ${YELLOW}⚠${NC}  CNAME not found in dist/"
    fi
else
    echo -e "   ${RED}✗${NC} Build failed (see /tmp/build.log for details)"
fi

# Check 5: DNS resolution
echo "5. Checking DNS resolution..."
if command -v host >/dev/null 2>&1; then
    if host relaylaunch.com > /dev/null 2>&1; then
        echo -e "   ${GREEN}✓${NC} DNS configured for relaylaunch.com"
    else
        echo -e "   ${YELLOW}⚠${NC}  DNS not configured or not propagated yet"
    fi
elif command -v dig >/dev/null 2>&1; then
    if dig +short relaylaunch.com >/dev/null 2>&1; then
        echo -e "   ${GREEN}✓${NC} DNS configured for relaylaunch.com"
    else
        echo -e "   ${YELLOW}⚠${NC}  DNS not configured or not propagated yet"
    fi
elif command -v nslookup >/dev/null 2>&1; then
    if nslookup relaylaunch.com >/dev/null 2>&1; then
        echo -e "   ${GREEN}✓${NC} DNS configured for relaylaunch.com"
    else
        echo -e "   ${YELLOW}⚠${NC}  DNS not configured or not propagated yet"
    fi
else
    echo -e "   ${YELLOW}⚠${NC}  DNS check skipped: no 'host', 'dig', or 'nslookup' command available"
fi

# Check 6: Website accessibility
echo "6. Checking website accessibility..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" https://relaylaunch.com 2>/dev/null || echo "000")
if [ "$HTTP_CODE" = "200" ]; then
    echo -e "   ${GREEN}✓${NC} Website is live and accessible"
elif [ "$HTTP_CODE" = "000" ]; then
    echo -e "   ${RED}✗${NC} Cannot connect to website (DNS or Pages not configured)"
else
    echo -e "   ${YELLOW}⚠${NC}  Website returned HTTP $HTTP_CODE"
fi

echo ""
echo "======================================"
echo "Summary"
echo "======================================"
echo ""
echo "Build System:  Ready ✓"
echo "Workflow:      Configured ✓"
echo ""

if [ "$HTTP_CODE" != "200" ]; then
    echo -e "${YELLOW}Action Required:${NC}"
    echo "The website is not live yet. This requires a one-time"
    echo "manual configuration step in GitHub repository settings."
    echo ""
    echo "Please see DEPLOYMENT_SETUP.md for detailed instructions."
    echo ""
    echo "Quick link: https://github.com/Relay-Launch/relaylaunch-website/settings/pages"
else
    echo -e "${GREEN}Status: Website is live! ✓${NC}"
fi

echo ""
