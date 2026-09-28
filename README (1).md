# Basic English for Coding
# کوڈنگ کے لیے بنیادی انگریزی

A free, Urdu-medium booklet that explains the English words used in computer code, and what they really mean, for students and teachers across Pakistan.

**[Download the booklet (PDF, 20 pages)](dist/Basic_English_for_Coding_Urdu.pdf)**

## Why this booklet exists

Programming is written in English words, but in code those words often do something quite different from their everyday meaning. `print` does not print on paper; it shows something on the screen. `if` does not mean "maybe"; it is a strict test with only two answers. `while` does not mean "at the same time"; it means "keep repeating". A student who has worked hard to learn the ordinary English meaning can be confused by it the moment they start coding.

The idea came from teaching an introductory programming class at a public school in Skardu, where students think in one language, are taught in Urdu, and have to write code in English. This booklet puts the everyday meaning and the coding meaning of each word side by side, and explains the difference in simple Urdu.

It is designed to work on paper, with no computer, electricity or internet needed.

## What is inside

- 35 coding keywords in six sections: talking to the computer, storing things, making decisions, repeating, making your own commands, and fixing mistakes
- For each word: pronunciation in Urdu script, everyday English meaning, what it does in code, a short Python example with its exact output, and one point to remember
- Common error messages explained in Urdu
- Keyboard symbols with their English and Urdu names
- Practice questions to solve on paper, with answers
- A one-page quick reference

All examples are in Python and are checked automatically: the build refuses to run if any printed output in the booklet does not match what Python actually shows.

## For teachers

The booklet is free. Print it, photocopy it, share it on WhatsApp, and use it in any class. Teaching one section at a time and having students work out each example on paper before running it works well.

If a word confused your students, or a word you needed is missing, please open an issue on this page or get in touch, so the next edition can be better.

## Building the PDF yourself

All the text lives in one file, `src/content.py`. To change a word or add a new one, edit that file and rebuild.

```
pip install -r requirements.txt
python src/check_examples.py   # checks every example
python src/build.py            # creates dist/Basic_English_for_Coding_Urdu.pdf
```

WeasyPrint needs a few system libraries on Windows and macOS. See the [WeasyPrint installation guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html).

## Project structure

```
src/content.py          all booklet text, keywords and examples
src/check_examples.py   runs every example and checks the printed output
src/build.py            builds the PDF
src/style.css           page design (right-to-left Urdu layout)
fonts/                  Noto Nastaliq Urdu font and its licence
dist/                   the finished PDF
```

## Ideas for future editions

- Editions in Sindhi, Pashto, Punjabi, Balochi, Balti or Shina
- More keywords (dictionaries, classes, try and except)
- An edition for another programming language

Contributions are welcome.

## Credits and how this was made

Prepared by Muhammad Salaar Rashid. The booklet and its build script were developed with the help of an AI assistant (Claude by Anthropic). Salaar planned the project from his own teaching experience, reviewed the content, and maintains and extends it.

## Licence

- Booklet content (text and PDF): [Creative Commons Attribution 4.0](LICENSE-CONTENT). You may copy, share and adapt it freely, as long as you credit the source.
- Code: [MIT Licence](LICENSE-CODE).
- Font: Noto Nastaliq Urdu, [SIL Open Font Licence](fonts/OFL.txt).

---

## اردو میں

یہ ایک مفت کتابچہ ہے جو کوڈنگ میں استعمال ہونے والے انگریزی الفاظ کے اصل معنی آسان اردو میں سمجھاتا ہے۔ یہ پاکستان بھر کے طلبہ اور اساتذہ کے لیے ہے۔

کوڈ کے بہت سے الفاظ عام انگریزی جیسے لگتے ہیں مگر ان کا کام بالکل مختلف ہوتا ہے۔ مثال کے طور پر `print` کاغذ پر کچھ نہیں چھاپتا بلکہ سکرین پر دکھاتا ہے۔ یہ کتابچہ ہر لفظ کے دونوں مطلب ساتھ ساتھ رکھ کر اردو میں فرق سمجھاتا ہے۔

**[کتابچہ ڈاؤن لوڈ کریں](dist/Basic_English_for_Coding_Urdu.pdf)**

اساتذہ اسے مفت پرنٹ کریں، فوٹو کاپی کریں اور کلاس میں بانٹیں۔ اگر کوئی لفظ سمجھ نہ آئے یا کوئی ضروری لفظ موجود نہ ہو تو ہمیں ضرور بتائیں تاکہ اگلا ایڈیشن بہتر ہو سکے۔
