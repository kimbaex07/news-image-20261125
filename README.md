# 25 November 2026 in one image

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/kimbaex07/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/kimbaex07/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image that sums up Wednesday 25 November 2026: a front page with
the date at the top and **18 date-checked stories across 7 regions** —
three illustrated leads (Houthis hitting Riyadh's tallest tower, the
Huawei verdict in New York, Zelenskiy confirming the Gulf of Finland
ship strike) plus a digest covering the Middle East, Europe, the US,
Asia and sport.

## The news of 25 November 2026

Built early on 25 November (run started 08:18 WIB = 01:18 UTC), so the
stories below are the events that happened or were first reported on
25 November 2026 in some timezone — overnight UTC wire news and
Asia-morning reporting dated 25 November. Where an event happened on
24 November, the reporting date is stated honestly.

**Leads**

- **HOUTHIS HIT RIYADH'S TALLEST TOWER** — Yemen's Houthis strike the
  tallest tower in Riyadh, the Public Investment Fund headquarters in
  the King Abdullah Financial District, with a drone on Tuesday
  24 November, wounding 11 people (2 Saudis, 2 Indians, 3 Nepalese,
  4 Egyptians). The second hit on the tower in under a week; the
  Saudi-led coalition vows a decisive response. Reported 25 November
  2026. (Reuters via BusinessWorld, 25 Nov 08:39; Saudi Civil Defence)
- **HUAWEI GUILTY ON 10 OF 12 COUNTS** — A federal jury in Brooklyn
  convicts Huawei on Tuesday 24 November on 10 of 12 counts: bank
  fraud, wire fraud, sanctions violations over Iran business and
  conspiring to steal trade secrets from US companies. It acquits on
  racketeering conspiracy and conspiracy to obstruct justice;
  sentencing is set for 14 September 2027. Reported 25 November
  2026. (Reuters; US Department of Justice; AP)
- **ZELENSKIY: UKRAINE HIT RUSSIAN SHIP** — President Zelenskiy
  confirms in a Bloomberg interview on Monday 24 November that
  Ukraine was behind Saturday's drone strike on the Russian cargo
  ship Sparta II in the Gulf of Finland, calling it a legitimate
  military target because it was carrying weapons. Norway, a close
  ally, urges caution. Reported 25 November 2026. (Reuters; Bloomberg)

**Digest (15 more)**

- **Aden:** Houthis push to within 60 km of the city but will not
  take it, Yemen's military says. (Reuters World News Summary, 25 Nov)
- **Hormuz:** Iran's navy claims three oil tankers were hit by naval
  mines in the strait. (Jagran Josh 25 Nov headlines)
- **Gaza:** UN raises concern over humanitarian conditions as
  civilians struggle for essentials. (Jagran Josh 25 Nov headlines)
- **Iran:** Winter gas shortages loom as war damage deepens the
  energy crisis. (RFE/RL, published 25 Nov 01:00 UTC)
- **War dead:** More than 700,000 Russian soldiers killed in the
  Ukraine war, a new analysis finds. (RFE/RL, published 25 Nov 01:00 UTC)
- **Sanctions:** EU proposes a 22nd package — 60 banks off SWIFT,
  70+ "shadow fleet" ships listed. Proposed 23 Nov by Commission
  President von der Leyen; reported 25 Nov. (Bytes Europe, 25 Nov 00:29 UTC)
- **France:** Ex-president Sarkozy's corruption case is ordered to
  trial; first pre-trial hearing 1 April 2027. (Reuters World News
  Summary, 25 Nov)
- **UN:** Russia and Ukraine trade accusations over attacks on Black
  Sea shipping and energy infrastructure. (Jagran Josh 25 Nov headlines)
- **Breach:** The CIA and the Office of the Director of National
  Intelligence discover a breach exposing some unclassified
  information, the New York Times reports. (Reuters, 25 Nov)
- **Medal:** Trump awards Rudy Giuliani the Presidential Medal of
  Freedom. (Reuters World News Summary, 25 Nov)
- **Turkeys:** Trump pardons Freedom and Feathers at the White House
  on Tuesday 24 November; Feathers first flees into the bushes.
  Reported 25 Nov. (Reuters; AP; White House)
- **Fort Hood:** Gunman Nidal Hasan seeks a stay of his execution,
  set for next week, court records show. (Reuters World News Summary,
  25 Nov)
- **India:** BJP and Shiromani Akali Dal revive their alliance for
  the 2027 Punjab polls after six years; they will contest all 117
  seats together. Announced 24 Nov; reported 25 Nov. (Jagran Josh
  25 Nov headlines)
- **Cricket:** England beat Australia by eight wickets in the 2nd
  T20I to level the series 1–1. (Jagran Josh 25 Nov headlines)
- **Markets:** Dell lifts its outlook after a record quarter on AI
  server demand. (Google News summary, 25 Nov)

## Run it

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

The program copies `entry.png` (a 1024x1024 PNG) to
`$MAKEFUN_OUTPUT_DIR/entry.png` byte for byte, so both grader runs
write identical output. Python 3.13, standard library only, no network.

## How the image was made

The front page is composed locally with Pillow: masthead, three
illustrated leads and a 15-item digest, all text rendered crisply in
code so nothing is garbled. All three lead scenes (the Riyadh tower at
night, the courtroom gavel, the cargo ship at sea) are flat drawings
made in code with Pillow primitives — no generated images, no text
baked into any raster art. Every story was checked against reporting
dated 25 November 2026 before it was captioned; claims are attributed
where they are claims (e.g. the IRGC's tanker claim, Kyiv's weapons
claim about the Sparta II), and events that happened on 24 November
are shown as reported on 25 November, not re-dated.

---

Built for the [make.fun](https://make.fun/r/cbprbg0z) bounty
`news-image-20261125` — sum up 25 November's world news in one image.
