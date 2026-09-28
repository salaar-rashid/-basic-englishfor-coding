# -*- coding: utf-8 -*-
"""
build.py
Builds the printable PDF of "Basic English for Coding" from content.py.

How it works:
  1. Checks every code example with check_examples.py. If any printed output
     is wrong, it stops, so a mistake can never reach students.
  2. Turns the content into an HTML page, styled by style.css.
  3. Uses WeasyPrint to turn that page into an A4 PDF in the dist folder.

Usage (from the main project folder):
    pip install -r requirements.txt
    python src/build.py
"""
import html
import re
import sys
from pathlib import Path

from content import SECTIONS, ERRORS, PRACTICE
from check_examples import check_all, run

SRC = Path(__file__).resolve().parent
ROOT = SRC.parent
FONT = ROOT / "fonts" / "NotoNastaliqUrdu.ttf"
OUTPUT = ROOT / "dist" / "Basic_English_for_Coding_Urdu.pdf"

# Part titles used after the six keyword sections
EXTRA_PARTS = [
    ("7", "غلطی کے پیغامات"),
    ("8", "کی بورڈ کے نشان"),
    ("9", "کاغذ پر مشق اور جوابات"),
    ("10", "تمام الفاظ ایک نظر میں"),
]


# ---------------------------------------------------------------- helpers

def esc(text):
    """Make text safe to place inside HTML."""
    return html.escape(text)


def urdu(text):
    """Escape Urdu text, and wrap any English words or code inside it so they
    keep their own left-to-right direction and get a little space around them."""
    parts = re.split(r"([!-~]+(?: [!-~]+)*)", text)
    out = []
    for i, part in enumerate(parts):
        if i % 2:  # odd parts are the English / code runs
            out.append(f'<span class="lat">{html.escape(part)}</span>')
        else:
            out.append(html.escape(part))
    return "".join(out)


def section_heading(number, title_ur, title_en, description, new_page=True):
    css_class = "section" if new_page else "sec2"
    return (f"<div class='{css_class}'><div class='sechead'>"
            f"<span class='enh'>{esc(title_en)}</span>"
            f"<h2><span class='num'>{number}</span>{esc(title_ur)}</h2>"
            f"<p>{urdu(description)}</p></div>")


def answer_lines(count):
    return "<div class='ln'></div>" * count


# ---------------------------------------------------------------- parts of the book

def cover():
    return f"""<div class="cover"><h1>کوڈنگ کے لیے بنیادی انگریزی</h1>
<div class="ent en">Basic English for Coding</div>
<div class="sub">کوڈنگ کے انگریزی الفاظ اور ان کے اصل معنی، آسان اردو میں</div>
<div class="note">کوڈ کے بہت سے الفاظ عام انگریزی جیسے لگتے ہیں مگر ان کا کام بالکل مختلف ہوتا ہے۔ یہ کتابچہ دونوں مطلب ساتھ ساتھ رکھ کر اردو میں فرق سمجھاتا ہے۔ اسے پڑھنے کے لیے کمپیوٹر، بجلی یا انٹرنیٹ ضروری نہیں۔ تمام مثالیں {urdu('Python')} زبان میں ہیں۔</div>
<div class="foot">تیار کردہ: محمد سالار راشد، پاکستان بھر کے طلبہ اور اساتذہ کے لیے۔ پہلا ایڈیشن، 2026۔ تدریس کے لیے مفت نقل کریں اور آگے بھیجیں۔<span class="en">Prepared by Muhammad Salaar Rashid for students and teachers across Pakistan. First edition, 2026. Free to copy and share for teaching.</span></div></div>"""


def introduction():
    rows = []
    for number, title_ur, _en, _desc, entries in SECTIONS:
        words = ", ".join(e["w"].split("  ")[0] for e in entries)
        rows.append(f"<tr><td style='width:8mm' class='en'>{number}</td><td><b>{esc(title_ur)}</b></td>"
                    f"<td class='en' style='font-size:9pt;color:#444;text-align:left'>{esc(words)}</td></tr>")
    for number, title in EXTRA_PARTS:
        rows.append(f"<tr><td class='en'>{number}</td><td colspan='2'><b>{title}</b></td></tr>")
    return f"""<h2>یہ کتابچہ کیسے استعمال کریں</h2>
<p>کمپیوٹر پروگرام انگریزی الفاظ میں لکھے جاتے ہیں، لیکن کوڈ میں ان الفاظ کا مطلب اکثر وہ نہیں ہوتا جو عام انگریزی میں ہوتا ہے۔ مثال کے طور پر {urdu('print')} کاغذ پر کچھ نہیں چھاپتا بلکہ سکرین پر دکھاتا ہے، اور {urdu('if')} کا مطلب شاید نہیں بلکہ یہ ایک سخت جانچ ہے جس کے صرف دو جواب ہوتے ہیں۔ جو طالب علم عام انگریزی کا مطلب جانتا ہے، اسے کوڈ میں وہی لفظ الجھا سکتا ہے۔</p>
<p>اس کتابچے میں ہر لفظ کے لیے یہ حصے دیے گئے ہیں:</p>
<div class="box"><b>عام انگریزی میں:</b> لفظ کا روزمرہ مطلب<br><b>کوڈ میں:</b> پروگرام میں یہ لفظ اصل میں کیا کام کرتا ہے<br><b>مثال:</b> {urdu('Python')} کوڈ کی چند لائنیں<br><b>سکرین پر:</b> کوڈ چلنے پر کمپیوٹر کیا دکھاتا ہے<br><b>یاد رکھیں:</b> سب سے ضروری بات</div>
<p>اس کتابچے کو استعمال کرنے کے لیے کمپیوٹر ضروری نہیں۔ ہر مثال کاغذ پر لکھیں، جواب کو چھپا دیں اور سوچیں کہ کمپیوٹر کیا دکھائے گا۔ جب کمپیوٹر دستیاب ہو تو مثال خود لکھ کر چلائیں، اپنا جواب چیک کریں، اور پھر کوڈ میں تبدیلی کر کے دیکھیں کہ کیا ہوتا ہے۔</p>
<p><b>اساتذہ کے لیے:</b> یہ کتابچہ مفت ہے۔ اسے فوٹو کاپی کریں، کلاس میں بانٹیں یا فون پر شیئر کریں۔ ایک وقت میں ایک حصہ پڑھانا بہتر ہے، اور ہر مثال پہلے کاغذ پر حل کروائیں۔</p>
<h2 style="font-size:15pt; margin-top:2mm">فہرست</h2><table class="grid">{''.join(rows)}</table>"""


def keyword_card(entry):
    wrong = entry.get("wrong")
    example_label = "غلط کوڈ" if wrong else "مثال"
    output_label = "نتیجہ" if wrong else "سکرین پر"
    return f"""<div class="card"><div class="head"><span class="say">تلفظ: {esc(entry['say'])}</span><span class="mono word">{esc(entry['w'])}</span></div>
<table class="mean"><tr><td class="lbl">عام انگریزی میں</td><td class="t">{urdu(entry['every'])}</td></tr>
<tr class="code"><td class="lbl">کوڈ میں</td><td class="t">{urdu(entry['ur'])}</td></tr></table>
<table class="ex"><tr><td class="c"><div class="cap">{example_label}</div><pre>{esc(entry['ex'])}</pre></td>
<td><div class="cap">{output_label}</div><pre>{esc(entry['out'])}</pre></td></tr></table>
<p class="rem"><b>یاد رکھیں:</b> {urdu(entry['rem'])}</p></div>"""


def keyword_sections():
    parts = []
    for number, title_ur, title_en, description, entries in SECTIONS:
        # Only the first section starts a new page; the rest flow on to save paper.
        parts.append(section_heading(number, title_ur, title_en, description, new_page=(number == "1")))
        parts.extend(keyword_card(e) for e in entries)
        parts.append("</div>")
    return "".join(parts)


def error_messages():
    rows = "".join(
        f"<tr><td class='mono' style='font-size:9pt'>{name}</td><td>{urdu(meaning)}</td>"
        f"<td><pre style='font-size:9pt'>{esc(code)}</pre></td></tr>"
        for name, meaning, code in ERRORS)
    return (section_heading("7", "غلطی کے پیغامات", "Error messages",
                            "جب Python آپ کا کوڈ نہیں چلا سکتا تو وہ رک کر غلطی کا پیغام دکھاتا ہے۔ یہ ڈانٹ نہیں بلکہ اشارہ ہے کہ کہاں دیکھنا ہے۔")
            + "<div class='box'><b>پہلے آخری لائن پڑھیں۔</b> اس میں غلطی کا نام ہوتا ہے۔ اس کے اوپر لکھا لائن نمبر بتاتا ہے کہ کون سی لائن چیک کرنی ہے۔</div>"
            + "<table class='grid'><tr><th style='width:40mm'>غلطی کا نام</th><th>مطلب</th><th style='width:40mm'>یہ کوڈ غلطی دیتا ہے</th></tr>"
            + rows + "</table></div>")


def keyboard_symbols():
    from content import SYMBOLS
    rows = "".join(
        f"<tr><td class='mono' style='font-size:11.5pt'>{esc(sym)}</td><td class='en' style='font-size:9.5pt'>{esc(en)}</td>"
        f"<td>{esc(ur)}</td><td>{urdu(use)}</td></tr>"
        for sym, en, ur, use in SYMBOLS)
    return (section_heading("8", "کی بورڈ کے نشان", "Keyboard symbols",
                            "کوڈ میں بہت سے ایسے نشان استعمال ہوتے ہیں جن کے نام ہم کلاس میں کم ہی لیتے ہیں۔ ان کے نام جاننے سے مدد مانگنا آسان ہو جاتا ہے۔")
            + "<table class='grid'><tr><th style='width:16mm'>نشان</th><th style='width:44mm'>انگریزی نام</th><th style='width:34mm'>اردو نام</th><th>استعمال</th></tr>"
            + rows + "</table></div>")


def practice_and_answers():
    parts = [section_heading("9", "کاغذ پر مشق", "Try it on paper",
                             "ہر پروگرام کمپیوٹر پر کیا دکھائے گا؟ اپنا جواب خالی جگہ میں لکھیں، پھر جوابات والے صفحے پر چیک کریں۔")]
    for number, code in enumerate(PRACTICE, 1):
        parts.append(f"<div class='q'><div class='qh'>سوال {number}</div><table><tr><td class='c'><pre>{esc(code)}</pre></td>"
                     f"<td><div class='cap'>آپ کا جواب</div>{answer_lines(3)}</td></tr></table></div>")
    parts.append(f"<div class='q'><div class='qh'>اب آپ کی باری</div><table><tr><td>ایک پروگرام لکھیں جو {urdu('for')} لوپ اور {urdu('range')} کی مدد سے آپ کا نام تین بار دکھائے۔ پھر ایک پروگرام لکھیں جو {urdu('input')} سے ایک عدد لے اور بتائے کہ وہ 10 سے بڑا ہے یا نہیں۔ یاد رکھیں کہ {urdu('input')} متن دیتا ہے، اس لیے {urdu('int()')} استعمال کرنا ہوگا۔{answer_lines(6)}</td></tr></table></div></div>")

    # The answers are worked out by actually running the code, so they are always right.
    rows = "".join(f"<tr><td class='en'>{n}</td><td><pre>{esc(run(code))}</pre></td></tr>"
                   for n, code in enumerate(PRACTICE, 1))
    sample = ('for i in range(3):\n    print("Amina")\n\nnumber = int(input("Number? "))\n'
              'if number > 10:\n    print("Bigger than 10")\nelse:\n    print("Not bigger than 10")')
    parts.append("<div class='section'><div class='sechead'><span class='enh'>Answers</span><h2>جوابات</h2>"
                 "<p>اگر آپ کا جواب مختلف تھا تو اس لفظ کو دوبارہ دیکھیں جس پر غلطی ہوئی۔ پروگرامر اسی طرح سیکھتے ہیں۔</p></div>"
                 f"<table class='grid'><tr><th style='width:22mm'>سوال</th><th>کمپیوٹر یہ دکھائے گا</th></tr>{rows}</table>"
                 f"<div class='box' style='margin-top:5mm'><b>اب آپ کی باری، ایک ممکنہ جواب:</b><pre style='margin-top:1mm'>{esc(sample)}</pre></div></div>")
    return "".join(parts)


def at_a_glance():
    lines = "".join(f"<p><span class='mono'>{esc(e['w'])}</span> &nbsp;{urdu(e['gl'])}</p>"
                    for section in SECTIONS for e in section[4])
    return (section_heading("10", "تمام الفاظ ایک نظر میں", "All the words at a glance",
                            "کمپیوٹر کے پاس رکھنے کے لیے مختصر فہرست۔")
            + f"<div class='gl'>{lines}</div>"
            + "<div class='box' style='margin-top:6mm'>یہ کتابچہ مفت ہے۔ اسے نقل کریں، دوسروں کو دیں اور کسی بھی کلاس میں استعمال کریں۔ اگر کوئی لفظ سمجھ نہ آئے یا کوئی ضروری لفظ اس میں موجود نہ ہو تو اپنے استاد کو بتائیں تاکہ اگلا ایڈیشن بہتر ہو سکے۔</div></div>")


# ---------------------------------------------------------------- main

def build_html():
    body = (cover() + introduction() + keyword_sections() + error_messages()
            + keyboard_symbols() + practice_and_answers() + at_a_glance())
    return ("<html lang='ur' dir='rtl'><head><meta charset='utf-8'><title>Basic English for Coding</title>"
            "<link rel='stylesheet' href='style.css'></head><body>" + body + "</body></html>")


def main():
    problems = check_all()
    if problems:
        print("Build stopped. These examples need fixing in content.py:")
        for line in problems:
            print("  -", line)
        sys.exit(1)

    if not FONT.exists():
        print(f"Urdu font not found at {FONT}. See fonts/README.md.")
        sys.exit(1)

    try:
        import weasyprint
    except ImportError:
        print("WeasyPrint is not installed. Run: pip install -r requirements.txt")
        sys.exit(1)

    OUTPUT.parent.mkdir(exist_ok=True)
    weasyprint.HTML(string=build_html(), base_url=str(SRC) + "/").write_pdf(str(OUTPUT))
    print(f"Done. PDF saved to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
