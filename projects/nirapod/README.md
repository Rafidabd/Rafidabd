# NIRAPOD

*A Bangla-first digital trust prototype, with an English interface too.*

NIRAPOD is something I'm building to help people look more carefully at suspicious messages, social posts and online claims. I don't want it to label a person or a news story as trustworthy just because a few keywords matched. The idea is to show what raised a concern, what evidence is actually available, and what someone could check next.

## What I've been working on

- **ScamShield:** rule-based warnings for things like OTP requests, urgent payment demands and suspicious links.
- **FactLens:** an optional lookup for published fact-check reviews. It only makes a request when the user opts in and a provider has been configured. A related review isn't automatically a verdict.
- **SocialLens:** guidance for examining claims alongside public post or comment context that a user chooses to paste in. It doesn't scrape social-media accounts.
- **MediaLens Lite:** basic image metadata hints checked in the browser. It cannot reliably determine whether an image was generated or altered by AI.
- **Investigation dashboard:** a summary of warning signs, evidence status, suggested sources and practical next steps, with Bangla and English interface options.

The current version is a **v0.4 prototype** for local use and small, supervised demonstrations. It's not a production security tool or a fact-checking authority. The rules can produce false positives and miss real scams; a lack of warnings doesn't prove something is safe.

The code is in a **private repository for now**, and there isn't a public demo linked here. This page is a short overview, not a source-code release. I want to keep the distinction between a suggested source, a search result and a review that's actually been retrieved and read very clear.

[Back to my GitHub profile](../../README.md)
