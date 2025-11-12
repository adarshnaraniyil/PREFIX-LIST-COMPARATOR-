# PREFIX-LIST-COMPARATOR

Network Automation using Python

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)](https://www.python.org/)

A Python 3 utility to compare two Cisco prefix-list files and highlight differences perfect for **network engineers** auditing or syncing router configurations.

---

## 🎯 The Problem

When managing complex network routing, ensuring two routers (or a router and a staging file) have identical prefix-lists is crucial. Manual comparison is error-prone. This tool automates the auditing process by providing a **precise, actionable diff** between two configurations.

---

## 🚀 Features

* **🔍 Comprehensive Comparison:** Compares two prefix-list files line by line after intelligently parsing the relevant prefix statements.
* **📌 Detect Missing Entries:** Highlights prefixes present in one file but absent in the other.
* **⚠️ Flag Mismatches:** Detects differences in **sequence numbers**, **permit/deny actions**, or the **IP/Mask** itself, even if the surrounding text is similar.
* **📄 Readable Diff Format:** Outputs results in a structured format, separating **Missing**, **Extra**, and **Mismatched** entries.
* **✨ Pure Python:** No external dependencies required, ensuring easy setup and portability.

---

## 🐍 Requirements & Setup

* Python **3.6+**

Since this project has **no external dependencies**, setup is minimal.

### 📦 Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/adarshnaraniyil/prefix-list-comparator.git](https://github.com/adarshnaraniyil/prefix-list-comparator.git)
    cd prefix-list-comparator
    ```

---

## 🖥️ Usage

To run the comparator, ensure you've placed all three necessary files`prefix_compare.py`, `original prefix-list file`, and `new prefix-list file` in the `same directory`

Execution Steps (Command Prompt/Terminal)
Open Command Prompt: Open the Command Prompt or your preferred terminal application (type cmd into the Windows search bar and press Enter).

Navigate to the Directory: Use the cd (Change Directory) command to move to the folder where you placed the files. Example:

```bash

cd C:\Users\YourUsername\Desktop\comparator > python3 prefix_compare.py
  ```

🧾 Example Output

The output clearly categorizes all deviations found:

```bash
*** PREFIX-LIST COMPARISON REPORT ***

--- ❌ MISSING in prefix_list2.txt (Present in list1 only) ---
ip prefix-list MY_LIST seq 10 permit 192.168.1.0/24

--- ✅ EXTRA in prefix_list2.txt (Present in list2 only) ---
ip prefix-list MY_LIST seq 5 permit 172.16.0.0/16 ge 20 le 24

--- ⚠️ MISMATCHES (Different action/prefix/sequence at the same line position) ---
File 1: seq 20 deny 10.0.0.0/8
File 2: seq 20 permit 10.0.0.0/8
  ```
🧪 Sample Input Format

The script is designed to handle standard Cisco prefix-list entries, often extracted directly from a show run command.

```bash
! Contents of prefix_list.txt
ip prefix-list MY_LIST seq 10 permit 192.168.1.0/24
ip prefix-list MY_LIST seq 20 deny 10.0.0.0/8
ip prefix-list MY_LIST seq 30 permit 172.16.0.0/16 le 24
 ```

🛠 Development & Contributing 💡

Feel free to fork, improve, and contribute! All pull requests are welcome.

📧 Contact & Support

Feel free to reach out to the project owner, Adarsh Naraniyil, for questions, feedback, or collaborations.

Email: adarshnaraniyil@gmail.com

LinkedIn:https://www.linkedin.com/in/adarshnaraniyil



