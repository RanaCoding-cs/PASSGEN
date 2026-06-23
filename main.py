import random
import string
import os

# পাসওয়ার্ড সেভ করার ফাইলের নাম
PASSWORD_FILE = "passwords.txt"

# টার্মিনাল স্ক্রিন ক্লিয়ার করার ফাংশন
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# কালার কোড (টার্মিনাল ইন্টারফেস সুন্দর করার জন্য)
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RED = '\033[91m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
BOLD = '\033[1m'

# মেইন এস্কি ব্লক ব্যানার (ডেভেলপার এবং গিটহাব ইনফো সহ)
def display_banner():
    banner = f"""
{CYAN}{BOLD}
 ██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗███╗   ██╗
 ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║
 ██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║
 ██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║
 ██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║ ╚████║
 ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
              [ v2.0 • ULTIMATE MANAGER ]
{RESET}
{GREEN}{BOLD}  ► Developer : MD Imran Hossen (RANA VHAI)
  ► GitHub    : https://github.com/RanaCoding-cs{RESET}"""
    print(banner)
    print(f"{YELLOW}======================================================={RESET}")

# ফাইল থেকে পাসওয়ার্ড লোড করার ফাংশন
def load_passwords():
    if not os.path.exists(PASSWORD_FILE):
        return []
    with open(PASSWORD_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

# ফাইলে পাসওয়ার্ড রাইট করার ফাংশন
def save_all_passwords(passwords):
    with open(PASSWORD_FILE, "w", encoding="utf-8") as f:
        for pwd in passwords:
            f.write(pwd + "\n")

# পাসওয়ার্ড জেনারেশন লজিক
def generate_password(length, use_upper, use_lower, use_digits, use_special):
    char_pool = ""
    if use_upper: char_pool += string.ascii_uppercase
    if use_lower: char_pool += string.ascii_lowercase
    if use_digits: char_pool += string.digits
    if use_special: char_pool += string.punctuation

    if not char_pool: return None

    password = []
    if use_upper: password.append(random.choice(string.ascii_uppercase))
    if use_lower: password.append(random.choice(string.ascii_lowercase))
    if use_digits: password.append(random.choice(string.digits))
    if use_special: password.append(random.choice(string.punctuation))

    remaining_length = length - len(password)
    password += [random.choice(char_pool) for _ in range(remaining_length)]
    random.shuffle(password)
    return "".join(password)

# ১. পাসওয়ার্ড জেনারেট এবং সেভ অপশন
def menu_generate_password():
    clear_screen()
    display_banner()
    print(f"{MAGENTA}{BOLD}[ Feature: Password Generation ]{RESET}\n")
    
    try:
        length = int(input(f"{GREEN}[+] Enter password length (Min 8): {RESET}"))
        if length < 4:
            print(f"{RED}[!] Length too short! Automatically set to 8.{RESET}")
            length = 8

        use_upper = input(" - Include uppercase letters (A-Z)? (y/n): ").strip().lower() == 'y'
        use_lower = input(" - Include lowercase letters (a-z)? (y/n): ").strip().lower() == 'y'
        use_digits = input(" - Include numbers (0-9)? (y/n): ").strip().lower() == 'y'
        use_special = input(" - Include special characters (@,#)? (y/n): ").strip().lower() == 'y'

        if not (use_upper or use_lower or use_digits or use_special):
            use_upper = use_lower = use_digits = use_special = True

        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        
        print(f"\n{GREEN}{BOLD}[✔] Generated Password:{RESET} {BOLD}{password}{RESET}")
        print(f"{YELLOW}-------------------------------------------------------{RESET}")
        
        # সেভ করার পপআপ/প্রম্পট
        save_choice = input(f"{CYAN}[?] Do you want to save this password? (y/n): {RESET}").strip().lower()
        if save_choice == 'y':
            passwords = load_passwords()
            passwords.append(password)
            save_all_passwords(passwords)
            print(f"{GREEN}[✔] Successfully saved to '{PASSWORD_FILE}'!{RESET}")
        else:
            print(f"{RED}[X] Password not saved.{RESET}")

    except ValueError:
        print(f"\n{RED}[!] Invalid input! Please enter a valid number.{RESET}")
    
    input(f"\n{YELLOW}Press Enter to return to menu...{RESET}")

# ২. সংরক্ষিত সব পাসওয়ার্ড ভিউ করা
def menu_show_passwords():
    clear_screen()
    display_banner()
    print(f"{MAGENTA}{BOLD}[ Feature: Saved Password List ]{RESET}\n")
    
    passwords = load_passwords()
    if not passwords:
        print(f"{RED}[!] No passwords saved yet!{RESET}")
    else:
        print(f"{GREEN}[+] Total Saved Passwords:{RESET}")
        for index, pwd in enumerate(passwords, 1):
            print(f"  {YELLOW}{index}.{RESET} {pwd}")
            
    input(f"\n{YELLOW}Press Enter to return to menu...{RESET}")

# ৩. শুধু মোট পাসওয়ার্ড সংখ্যা দেখা (নিরাপত্তার জন্য পাসওয়ার্ড হাইড থাকবে)
def menu_show_total_count():
    clear_screen()
    display_banner()
    print(f"{MAGENTA}{BOLD}[ Feature: Total Password Counter ]{RESET}\n")
    
    passwords = load_passwords()
    total = len(passwords)
    print(f"{GREEN}[✔] Total passwords in database:{RESET} {BOLD}{total}{RESET}")
    print(f"{CYAN}[*] For security reasons, passwords are hidden in this view.{RESET}")
    
    input(f"\n{YELLOW}Press Enter to return to menu...{RESET}")

# ৪. সিরিয়াল নাম্বার ইনপুট দিয়ে নির্দিষ্ট পাসওয়ার্ড ডিলিট করা
def menu_remove_password():
    clear_screen()
    display_banner()
    print(f"{MAGENTA}{BOLD}[ Feature: Remove Password ]{RESET}\n")
    
    passwords = load_passwords()
    if not passwords:
        print(f"{RED}[!] No passwords available to remove.{RESET}")
    else:
        print(f"{CYAN}[*] Current Password List:{RESET}")
        for index, pwd in enumerate(passwords, 1):
            print(f"  {YELLOW}{index}.{RESET} {pwd}")
        print(f"{YELLOW}-------------------------------------------------------{RESET}")
        
        try:
            remove_index = int(input(f"{RED}[+] Enter the number of the password to delete: {RESET}"))
            if 1 <= remove_index <= len(passwords):
                removed_pwd = passwords.pop(remove_index - 1)
                save_all_passwords(passwords)
                print(f"\n{GREEN}[✔] Password #{remove_index} ({removed_pwd}) removed successfully!{RESET}")
            else:
                print(f"{RED}[!] Invalid number! No password found at this index.{RESET}")
        except ValueError:
            print(f"{RED}[!] Invalid input! Please enter a valid serial number.{RESET}")

    input(f"\n{YELLOW}Press Enter to return to menu...{RESET}")

# ৫.ツールス পরিচিতি (About)
def menu_about():
    clear_screen()
    display_banner()
    print(f"{MAGENTA}{BOLD}[ Feature: About Tool ]{RESET}\n")
    print(f"{GREEN}Tool Name:{RESET} Advanced Password Generator & Manager")
    print(f"{GREEN}Version:{RESET} v2.0 (Ultimate Edition)")
    print(f"{GREEN}Language:{RESET} Python 3")
    print(f"{GREEN}Description:{RESET} A smart terminal-based security tool")
    print("             that generates cryptographically strong passwords")
    print("             and safely manages them in a local file.")
    
    input(f"\n{YELLOW}Press Enter to return to menu...{RESET}")

# মেইন কন্ট্রোল প্যানেল লুপ
def main():
    while True:
        clear_screen()
        display_banner()
        print(f"{GREEN}[1]{RESET} Generate Password")
        print(f"{GREEN}[2]{RESET} Show Saved Passwords")
        print(f"{GREEN}[3]{RESET} Show Total Password Count")
        print(f"{GREEN}[4]{RESET} Remove a Password")
        print(f"{GREEN}[5]{RESET} About Tool")
        print(f"{RED}[6]{RESET} Exit")
        print(f"{YELLOW}======================================================={RESET}")
        
        choice = input(f"{BOLD}Select an option (1-6): {RESET}").strip()
        
        if choice == '1':
            menu_generate_password()
        elif choice == '2':
            menu_show_passwords()
        elif choice == '3':
            menu_show_total_count()
        elif choice == '4':
            menu_remove_password()
        elif choice == '5':
            menu_about()
        elif choice == '6':
            print(f"\n{CYAN}[*] Thank you for using the tool! Goodbye.{RESET}\n")
            break
        else:
            print(f"{RED}[!] Invalid option! Please select between 1 and 6.{RESET}")
            import time
            time.sleep(1.5)

if __name__ == "__main__":
    main()
