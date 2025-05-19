# CYSE 411 - Security Requirements

## 🧪 Objective

This lab gives students hands-on experience eliciting **user stories**, **evil user stories**, and **security stories** from a real-world scenario involving a disaster response system ("Argus Crisis").

Students will read a provided **problem statement**, analyze the system, and write:

- User Stories (task-oriented)
- Evil User Stories (from attacker perspective)
- Security Stories (countermeasures)

All stories must follow the appropriate format and include acceptance criteria (when required).

---

## 📘 Instructions

1. Read the `Problem_Statement.pdf` provided in this repo.
2. Complete the three files below using the specified formats:
   - `user_stories.txt`
   - `evil_user_stories.txt`
   - `security_stories.txt`
3. Use the templates for each story type as shown below.

---

## ✍️ Template Formats

### 1. User Story
```
As a <type of user>,
I want <some goal>,
So that <some reason>.
```

### 2. Evil User Story (with acceptance criteria)
```
As a malicious actor,
I want to <exploit a weakness>,
So that <achieve a malicious goal>.

Acceptance Criteria:
- <criteria 1>
- <criteria 2>
```

### 3. Security Story (with acceptance criteria)
```
As a security engineer,
I want to <protect against a threat>,
So that <ensure system security>.

Acceptance Criteria:
- <criteria 1>
- <criteria 2>
```

---

## ✅ Autograding

Autograding will check:
- Each file includes correctly formatted stories.
- Specific keywords are used for each role (`As a malicious actor`, `As a security engineer`, etc.).
- Presence of “Acceptance Criteria” for Evil/Security stories.

Run the tests locally:
```bash
python3 test_user_stories.py
```

---

## 📁 Files to Submit

Please fill out:
- `user_stories.txt`
- `evil_user_stories.txt`
- `security_stories.txt`

Push your changes to GitHub to submit your assignment.
