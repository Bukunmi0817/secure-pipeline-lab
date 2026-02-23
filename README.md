# Secure CI/CD Pipeline Lab 🛡️

A hands-on demonstration of **DevSecOps** principles, featuring automated security guardrails within a GitHub Actions pipeline.

## 🚀 Features
* **Secret Scanning:** Integrated `Gitleaks` to detect and prevent credential leaks in commit history.
* **SAST (Static Application Security Testing):** Utilized `Bandit` to identify high-severity Python vulnerabilities like Command Injection.
* **Automated Remediation:** Demonstrated the transition from insecure `os.system` calls to secure `subprocess` implementations.

## 🛠️ Tech Stack
* **Language:** Python 3.10
* **CI/CD:** GitHub Actions
* **Security Tools:** Gitleaks, Bandit

## 📈 Security Pipeline Status
![Security Scan](https://github.com/Bukunmi0817/secure-pipeline-lab/actions/workflows/security-scan.yml/badge.svg)

## 💡 Key Learnings
This project highlights the importance of the **Secure Development Lifecycle (SDLC)**. By shifting security "left" (testing during the build phase), we can identify and mitigate risks before they ever reach a production environment.
