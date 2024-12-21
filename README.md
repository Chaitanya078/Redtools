# Malware README: Ransomware, Adware, and Worm

## 1. **Ransomware**
### What It Does:
This tool encrypts all files in a specified directory and demands the victim to enter a "secret phrase" to decrypt their files.

### How It Works:
1. **Encrypts Files**: Files are encoded using Base64.
2. **Ransom Message**: Displays a message informing the victim that their files have been encrypted.
3. **Decryption**: The victim needs to provide the correct "secret phrase" to recover their files.

### How to Run:
- Run the script to encrypt files in the same folder.
- Decryption is only possible if the correct "secret phrase" is entered.

---

## 2. **Adware**
### What It Does:
This tool opens multiple advertisement windows with sarcastic messages to annoy the user. It also tracks how many times the victim clicks on "Claim Reward" and teases them further.

### Features:
1. **Ad Pop-Ups**: Displays windows with sarcastic ad slogans.
2. **Click Counter**: Tracks how many times the victim clicks the ad button.
3. **Exit Condition**: The victim must enter a "magic phrase" (e.g., `let_me_out`) to stop the ads.

### How It Works:
1. The program shows three ad windows at random positions on the screen.
2. When the victim clicks on the ad button, it logs the click and displays sarcastic messages.
3. The victim can escape by typing the correct magic phrase.

### How to Run:
- Run the script to display ads.
- Type the magic phrase when prompted to close the tool.

---

## 3. **Worm**
### What It Does:
This tool replicates itself by copying its own script into random directories within the user's home folder.

### How It Works:
1. **Locate Home Directory**: Finds the user's home folder (e.g., `/home/user/` or `C:\Users\Username\`).
2. **Random Replication**: Copies itself into random subdirectories.
3. **Spreads**: Continues this process indefinitely to simulate a spreading infection.

### How to Run:
- Run the script. It will immediately start replicating itself into random directories.

---

### Disclaimer:
These scripts are purely for educational purposes. They should **never** be used for malicious activities. Always test in a secure, isolated environment (e.g., virtual machines). Misuse of these tools is illegal and unethical.

