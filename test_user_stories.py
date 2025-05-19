
---

### ✅ `test_user_stories.py` (Regex Auto-Grader)

```python
import re

def check_file(filename, pattern, must_include):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    matches = re.findall(pattern, content, re.IGNORECASE)
    errors = []

    if len(matches) == 0:
        errors.append(f"No valid entries found in {filename}.")
    
    for phrase in must_include:
        if phrase.lower() not in content.lower():
            errors.append(f"Missing required phrase '{phrase}' in {filename}.")

    return errors

def run_tests():
    tests = {
        'user_stories.txt': {
            'pattern': r"As a .*?,\s*I want .*?,\s*So that .*?\.",
            'phrases': ['As a', 'I want', 'So that']
        },
        'evil_user_stories.txt': {
            'pattern': r"As a malicious actor,\s*I want to .*?,\s*So that .*?\.\s*Acceptance Criteria:\s*- .*",
            'phrases': ['As a malicious actor', 'Acceptance Criteria']
        },
        'security_stories.txt': {
            'pattern': r"As a security engineer,\s*I want to .*?,\s*So that .*?\.\s*Acceptance Criteria:\s*- .*",
            'phrases': ['As a security engineer', 'Acceptance Criteria']
        }
    }

    total_errors = 0
    for filename, rules in tests.items():
        errors = check_file(filename, rules['pattern'], rules['phrases'])
        if errors:
            print(f"❌ Issues in {filename}:")
            for err in errors:
                print(f"   - {err}")
            total_errors += 1
        else:
            print(f"✅ {filename} passed.")

    if total_errors == 0:
        print("\n🎉 All tests passed! Submission ready.")
    else:
        print(f"\n🚨 {total_errors} file(s) have issues.")

if __name__ == "__main__":
    run_tests()
