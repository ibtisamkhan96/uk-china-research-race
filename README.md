# The Research Race: UK vs China Universities in Deep Tech

A 10-slide **LinkedIn carousel** comparing how UK and Chinese universities contribute to the technologies shaping the next decade: artificial intelligence, EVs and batteries, autonomous vehicles, nanotechnology and materials, energy materials and solar, and supply chain and logistics.

Built as a portrait (1080x1350) carousel - individual PNG slides plus a combined PDF ready for a LinkedIn document post.

## The slides

![Cover](slides/slide_01.png)
![EVs and batteries](slides/slide_04.png)

(All ten slides are in `slides/`; the assembled deck is `carousel/uk_china_research_race.pdf`.)

## The story, domain by domain

| Domain | UK strength | China strength |
|---|---|---|
| **AI** | AlphaFold and DeepMind (London/UCL roots); 2024 Nobel Chemistry | Top universities by AI publication volume; CV, LLMs, patents |
| **EVs & batteries** | The Li-ion cathode was born at Oxford (Goodenough, 1980) | CATL and BYD supply ~half the world's EV batteries |
| **Autonomous vehicles** | Wayve and Oxa - novel learning-based driving | Tsinghua + Baidu Apollo; largest robotaxi fleets and mileage |
| **Nanotech & materials** | Graphene isolated at Manchester (Nobel 2010) | World's largest nanotech output; dominates graphene patents |
| **Energy materials** | Perovskite solar pioneered at Oxford (Oxford PV) | Over 80% of global solar PV manufacturing |
| **Supply chain** | Cambridge IfM and Cranfield - the science of supply chains | Smart logistics at national scale (Cainiao, JD) |

**The throughline:** the UK invents disproportionately - graphene, Li-ion cathodes, perovskites, AlphaFold were all seeded in British labs - while China increasingly owns the path from research paper to global product, backed by unmatched publication and patent volume.

## Honest caveat

This is a qualitative comparison of research strengths, not a precise league table. Claims and figures are compiled from public reporting: the **ASPI Critical Technology Tracker**, the **Nature Index**, Nobel Prize records, and university public information. Research leadership is contested and measured many different ways.

## What's in it

- `build_carousel.py` - generates all 10 slides and the PDF with matplotlib (no design tools)
- `slides/` - individual slides as PNG (1080x1350)
- `carousel/uk_china_research_race.pdf` - the assembled deck for LinkedIn
- `linkedin-post.txt` - ready-to-publish caption

Run: `pip install matplotlib`, then `python build_carousel.py`.

*Author: Ibtisam Ahmed Khan - [linkedin.com/in/ibtisam-ahmed-khan](https://linkedin.com/in/ibtisam-ahmed-khan)*
