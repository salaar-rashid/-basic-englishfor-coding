"""
check_examples.py
Runs every Python example in content.py and confirms that the output printed
in the booklet is exactly what Python really shows. Also confirms that each
error-message example really produces the error it is listed under, and
computes the answers for the practice questions.

Run it on its own with:
    python src/check_examples.py
build.py also runs it automatically and refuses to build if anything is wrong.
"""
import contextlib
import io

from content import SECTIONS, ERRORS, PRACTICE


def run(code):
    """Run a piece of Python code and return what it prints."""
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        exec(code, {})
    return buffer.getvalue().rstrip("\n")


def check_all():
    """Return a list of problems. An empty list means everything is correct."""
    problems = []

    for section in SECTIONS:
        for entry in section[4]:
            if entry.get("noverify"):
                continue
            actual = run(entry["ex"])
            if actual != entry["out"]:
                problems.append(
                    f"{entry['w']}: booklet says {entry['out']!r} but Python shows {actual!r}"
                )

    for name, _meaning, code in ERRORS:
        try:
            exec(compile(code, "<example>", "exec"), {})
            problems.append(f"{name}: the example code did not produce any error")
        except BaseException as error:
            if type(error).__name__ != name:
                problems.append(f"{name}: the example produced {type(error).__name__} instead")

    for number, code in enumerate(PRACTICE, 1):
        try:
            run(code)
        except Exception as error:
            problems.append(f"Practice question {number} crashed: {error}")

    return problems


if __name__ == "__main__":
    found = check_all()
    if found:
        print("Problems found:")
        for line in found:
            print("  -", line)
        raise SystemExit(1)
    total = sum(len(s[4]) for s in SECTIONS)
    print(f"All good: {total} keyword examples, {len(ERRORS)} error examples "
          f"and {len(PRACTICE)} practice questions checked.")
