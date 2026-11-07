---
name: dating-app-design
description: Complete design system, UX architecture, card stack mechanics, and interaction patterns for building modern, high-conversion mobile dating applications in FigCraft, React Native, or Flutter.
metadata:
  version: "1.0.0"
  category: "Mobile UX & Product Design"
---

# Mobile Dating App Design System & UX Architecture

This skill provides comprehensive product design patterns, tokens, visual hierarchy rules, and interaction architectures for modern dating applications (inspired by Hinge, Tinder, Bumble, and Raya).

---

## 1. Core Visual Design Tokens

### Color Palette & Theme: Dark Obsidian Romantic
- **Canvas / Background**: `#0D0E16` (Deep Midnight)
- **Elevated Surfaces / Cards**: `#161826` / `#1B1D2D`
- **Borders & Dividers**: Hairline `#FFFFFF15` (subtle elevation, zero harsh strokes)
- **Primary Accent (Love & Passion)**: Linear Gradient `["#FF385C", "#FF6584"]` (Warm Coral Pink)
- **Secondary Accent (VIP / Spotlight)**: Linear Gradient `["#8B5CF6", "#D946EF"]` (Electric Violet)
- **Gold / Super Boost**: Linear Gradient `["#FF8A00", "#FFC700"]` (Sunset Gold)
- **Super Like**: Linear Gradient `["#00F2FE", "#4FACFE"]` (Cyan)
- **Online Indicator**: `#10B981` (Emerald Green dot with dark stroke)

### Typography Hierarchy (iOS Human Interface Guidelines)
- **Screen Titles**: 24–28px Bold (`Inter` / `SF Pro Display`)
- **Profile Name & Age**: 22–26px Bold (`#FFFFFF`)
- **Section Headers**: 15–18px Bold (`#FFFFFF` or `#CCD2E3`)
- **Bio & Prompts**: 12–14px Medium (`#CCD2E3` on dark cards)
- **Metadata & Subtitles**: 11–12px Regular (`#8E95AB`)
- **Tags & Badges**: 10–11px SemiBold with 12–14px pill corner radius

---

## 2. Essential Screen Architectures

### A. Home (Swipe & Discovery Deck)
1. **Status Bar**: iPhone 16 standard (`9:41`, Dynamic Island pill `120x32px`, signal, Wi-Fi, battery).
2. **Top Bar**: Brand logo (`amour` / `flame`), Location chip (`📍 Brooklyn, NY`), and Filter button.
3. **Filter Pills**: `🔥 Trending`, `📍 Nearby (3mi)`, `✨ Verified`.
4. **Hero Card Stack**:
   - Depth under-card visible at bottom (2–4px offset).
   - High-contrast photographic card (`353 × 516px`, corner radius `28px`).
   - Story progress bars at top of photo (`4 segments`).
   - Badges: `Active 5m ago` and `✨ 96% Match` gradient chip.
   - Dark gradient scrim (`#00000000` to `#080911F5`) over bottom 45% for high text legibility.
   - Profile block: Name, age, verified badge, profession, distance, 3 lifestyle tag chips, and prompt quote.
5. **Ergonomic Action Controls** (Balanced 5-button floating row):
   - Rewind (Yellow 48px), Pass (Red ✕ 62px), Super Like (Cyan ★ 54px), Like (Coral Heart ♥ 70px), Boost (Purple ⚡ 48px).

### B. Dashboard (Explore & Vibes)
1. **Search & Audio Bar**: Input for activities, music, and places.
2. **Vibe Category Filters**: Horizontal chips (`🔥 All Vibes`, `☕ Coffee Date`, `🎵 Live Music`, `🍷 Wine Bar`).
3. **Daily Spotlight Hero Card**: Countdown timer (`⏱️ Resets in 04:32:10`), resonance score, and prompt.
4. **Top Picks Grid**: 2-column cards with compatibility meters.
5. **Live Radar Map Preview**: Concentric radar circles with pulsing avatar dots representing active local daters.

### C. Match (Matches & Conversations)
1. **Filter Tabs**: `All Chats`, `Unread (4)`, `Dates Planned (2)`.
2. **New Matches Story Tray**: Horizontal circular tray with gradient rings, online dots, and a blurred gold `Likes You (+14)` disc.
3. **Instant Celebration Banner**: Alert card celebrating mutual matches with quick CTA (`"Say Hi →"`).
4. **Conversation List**: Message preview, timestamp, unread counter pill, and read receipt double-checkmarks.

### D. Profile & Preferences
1. **Hero Avatar**: Circular avatar with camera edit badge and verified checkmark.
2. **VIP Status**: `👑 Flame Platinum Member` badge.
3. **Profile Completeness**: Progress bar meter (e.g. `92% Complete`).
4. **Stats Metric Row**: 3 equal tiles for `Matches`, `Profile Views`, and `Response Rate`.
5. **Prompt Cards**: Hinge-style prompt questions with highlighted answers.
6. **Passions Tag Cloud**: Micro-chips for hobbies and interests.

### E. Modals & Bottom Sheets
1. **"It's a Match!" Celebration Modal**:
   - Overlapping dual avatar discs with a bridging heart badge.
   - Match resonance percentage and suggested icebreaker prompt.
   - Quick message input box with send arrow.
   - `Send Message` primary button and `Keep Swiping` secondary button.
2. **Discovery Filters Sheet**:
   - Distance & age range sliders.
   - Verification and active status toggle switches.
   - Interest & passion multi-select chips.

---

## 3. Micro-Interactions & Prototyping Rules

- **Bottom Navigation**: All tabs must cross-navigate with `smartAnimate` transitions.
- **Swipe Card Feedback**: Like action triggers the celebration overlay.
- **Filter Action**: Filter button opens the preferences bottom sheet.
- **Dismissal**: All modals must feature both a top close button ("✕") and a secondary dismiss action.

