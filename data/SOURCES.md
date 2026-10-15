# Verified public sources (accessed 2026-10-15; no local repo read; all no-auth public)

## Primary: Benny Lewis method (claims under test)
- https://www.fluentin3months.com/teach-yourself-language-hacking/ — speak-from-day-one, postpone grammar, learn-only-what-you-need, mini-missions (updated 2026-09-10)
- https://www.fluentin3months.com/fluently/ — mini-missions, 45-min/day framing (updated 2026-08-30)
- https://www.fluentin3months.com/engineer/ — input-vs-output engineering/feedback mental model (2010-12-07)
- https://courses.fluentin3months.com/p/bootcamp — 90-day 15-min-conversation guarantee, refund conditions, "never a promise [of fluency]" disambiguation; next cohort 2026-11-02
- https://actualfluency.com/blog/how-benny-lewis-learns-languages — 7-year-follow summary: Tarzan language, 1-h Polish demo, multiple daily 1-on-1 tutors, ~8h/day during challenges, 500 words ≈ 80% newspaper
- https://www.fluentin3months.com/not-mix-up/ — separate languages via cultural/body-language association (updated 2026-08-23)

## Counter-evidence / community audits (voting: different opinions)
- Reddit r/languagelearningjerk 2020-12-31 — 6-mission audit (Czech fail / Portuguese partial / German C2-listening fail / Chinese fail / Japanese stopped / Arabic gave up)
- Reddit r/ChineseLanguage 2012-06-04 — 6-month Mandarin assessed nowhere near claimed C2; generous A2/weak-B1 reading
- Reddit r/languagelearning 2019-10-17 — $300 challenge felt scammed; no partner provided; Slack-only
- italki discussion 2016-10-15 — "solid A2 or weak B1 fluent then 3 months possible esp. immersive; snake oil otherwise"
- LingQ forum 2011-06-19 — Moses McCormick 42-language debate; intermediate-in-3-months vs fluent distinction
- FluentU review 2024-03-06 — Premium = hacks + mindset, no grammar/vocab lessons; unorganized; advises supplement Memrise/italki

## SLA theory (for H1-H7)
- Belali & Khany 2026 meta-analysis N=404 (1973-2023): metacognitive d=0.52 (sensitivity d=1.32), cognitive ≈0.56 (ESL 0.63 vs EFL 0.48), affective d=0.18, social ≈0.40; context EFL-vs-ESL dominant moderator — via websearch 2026-10-15
- second-language.app 2026-02-05 synthesis: DeKeyser & Sokalski N=82 skill-specificity; Swain 4 functions (noticing/hypothesis-testing/reflection/fluency); Postovsky 1974 Russian 4-week silent > speaking at midterm + listening at 12w; Gary 1975 Spanish kids 14-week silent equal speaking better listening; Shintani-Li-Ellis 35-experiment meta: comprehension better ≤1w, production better 1w-75d
- Krashen comprehensible-output PDF (sdkrashen.com): CO scarce; high competence without output possible; Nobuyoshi & Ellis n=6 only 1/3 significant (E1 p=.0115, E2 ns)
- UChicago TripleHelix 2025-05-20: input+output both crucial; affective filter
- Cambridge Immersive Speaking 2025 PDF: Swain + Long interaction hypothesis; peer-peer negotiates more meaning than teacher-learner
- Kim & Webb 2022 Language Learning meta N=3411 k=98: spaced>massed immediate g=0.58 [0.16,1.00], delayed g=0.80 [0.44,1.17]; longer>shorter delayed g=0.40; equal≈expanding
- SLR 2015-2025 N=27 (proceeding.umsu.ac.id): SRS digital flashcards > massed; multimodal > monomodal; user-generated > premade; image-as-feedback not hint; limited transfer to productive speaking/writing; gamification needed
- Zhou & Zhou 2025 ReCALL Bayesian k=65 (2010-2024): mobile vocab overall d=1.28 [1.03,1.52] (≥10w); trim-fill adjusted 0.74; receptive 1.38 productive 1.25 combined 0.66; out-of-class 1.42 > classroom 0.82
- Rogers Nakata Chiu 2025 SSLA: Cepeda et al. 2009 replication online; spaced>massed d>1.5 ANCOVA; ISI/RI 10-40% rule
- Tellier & Roehr-Brackin (Essex repository): N=28 age 8-9 Esperanto vs French 1 school year; Esperanto larger aptitude/metalinguistic gains + easier proficiency
- Madella EuroCALL 2025: 30 Golden Hours 20h online Esperanto; propaedeutic Q1/Q2

## Benchmarks: hours, frequency, retention (live-data anchors)
- FSI via LingoBright 2026-07-16 report (read 2026-10-15): Cat I 552-690h / II 828h / III 1012h / IV 2200h; 40h/wk (23 class +17 self); app learners need 1.5-2× FSI (Langmitra Mar 2026); Cat IV retention +14% (Ling App Jan 2026)
- FSI calculators cross-check: fluencystreak, lowercaseonline, kilolingo, miniwebtool, iienstitu, superglobalcalculator, calculatorhub, languagetools.directory (all agree 600-2200h band)
- Duolingo scale: 2024 316M downloads → 2025 327M; MAU Q3 116.7M → 135.3M; DAU 37.2M → 50.5M (Q1 2026 56.5M); revenue $748M → $1037.6M; paid 12.2M end-2025; English #1 in 135 → 154 countries
- Frequency coverage: commonwords.app + thelernen.org: top-1000 ≈ 80-85% everyday speech; ActualFluency: 500 words ≈ 80% newspaper (keywords only)
- AnkiDroid docs (GitHub): FSRS AI-optimized scheduler; 10k+ premade decks (confirms SRS production stack)
- EuropePMC 48 hits foreign-language speaking anxiety 2026 (Yayla et al. Big-5 mediation; Barbour poetry/drama; Zhang AI-emotion review)

## Reproducibility best practice (2026)
- OpenAlex (no key) + EuropePMC (OA flag + PDF URL) + CrossRef + arXiv + Semantic Scholar used for triangulation; one-search-at-a-time to avoid 429; DuckDuckGo lite fallback pattern
- FSI CSV vendored verbatim with source column; live check script re-fetches Wikipedia FSI + OpenAlex counts with offline snapshot fallback so `docker compose up` never fails offline
- No secrets; no login walls; all datasets public or synthetic-from-public-parameters
