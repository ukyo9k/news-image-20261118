# Wednesday 18 November 2026 — World News in One Image

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/ukyo9k/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/ukyo9k/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Built for the [make.fun](https://make.fun) bounty [“Sum up 18 November's world news in one image”](https://make.fun/bounty/news-image-20261118) ($250 in USDC). Referral: https://make.fun/r/1gefbfp1

A front-page poster summing up the world's news of **Wednesday 18 November 2026**, built for the make.fun bounty `news-image-20261118`.

## The image

`entry.png` (1024×1024, PNG, 163 KB) is a newspaper front page: a masthead naming the day and story count, a hero headline on the Gulf war flaring again with a schematic map of the Strait of Hormuz, three top stories with small drawn icons, a six-story grid, and a compact "Also on Wednesday 18 November" list — 22 stories across 6 continents. All text is drawn programmatically (PIL + DejaVu fonts) so every headline is crisp and legible; the map and icons are drawn shapes, not photographs. The build script is `build_poster.py`.

`main.py` (Python 3.13, standard library only) copies `entry.png` to the output directory (`$MAKEFUN_OUTPUT_DIR`, default `/output`). It uses no network and is fully deterministic — run it twice and the outputs are byte-identical.

## The 22 stories (all verified against sources opened on 18–19 Nov 2026)

Hero: **Gulf war flares again** — Iran struck Kuwait and Bahrain at dawn; US jets bombed an IRGC missile site on Qeshm Island; Houthis hit Saudi pipeline pumps. The third Iranian attack on US targets in Bahrain in five days, after a two-month lull. Sources: Reuters, AP, Just Security.

Top stories: **Trump hugs Xi as the APEC trilateral opens** (Reuters); **Nvidia's $115.8bn record quarter** — revenue up 103% in its first results since Jensen Huang quit, board rules out his return (Reuters, AJP, TechCrunch); **Democrats take a 56–44 Senate majority** as Peltola wins Alaska (Reuters, AP).

Grid: Ukrainian drones halve Russia's oil refining (Reuters); Voyager 1 crosses one light-day from Earth (NASA, Smithsonian); Indonesia–China sign $71.8bn in deals (Reuters); gold slides below $3,800 as the Fed turns hawkish (Reuters); the Mossad chief lobbied Washington for joint Iran strikes (Reuters); Mélenchon "could beat Le Pen" in France's 2027 race (Reuters).

Also: the Board of Peace on Gaza; Putin "not ready" for Ukraine talks; Turkey's probe of ex-banking chief Kavcioglu; Uganda's Mugumya charged with treachery; Myanmar reviewing ASEAN ties; Ethiopia–Eritrea troops massing; the FAA router pause; Cyclone Akvan; Anthropic's mega-IPO pricing; India's record foreign inflows; the US chip-access block on China; AI safety hearings.
