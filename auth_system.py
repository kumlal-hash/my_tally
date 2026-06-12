import sqlite3
import sys

DB_NAME = "nepse_tally.db"


def init_db():
    """डेटाबेस र युजर्स टेबल बनाउने फङ्सन"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # यदि टेबल छैन भने बनाउने
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


# एप चल्ने बित्तिकै डेटाबेस रेडी गर्ने
init_db()

# अहिले लगिन भएको युजर को हो ट्र्याक गर्न
current_user = None


def register():
    print("\n--- 📝 नयाँ अकाउन्ट दर्ता (Register) ---")
    username = input("नयाँ युजरनेम राख्नुहोस्: ").strip().lower()

    if not username:
        print("❌ युजरनेम खाली छोड्न मिल्दैन!")
        return

    password = input("नयाँ पासवर्ड राख्नुहोस्: ")
    if len(password) < 4:
        print("❌ पासवर्ड कम्तीमा ४ अक्षरको हुनुपर्छ!")
        return

    # डेटाबेसमा डाटा हाल्ने (INSERT)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password),
        )
        conn.commit()
        print(
            f"✅ अकाउन्ट सफलतापूर्वक बन्यो! अब सुरक्षित रूपमा लगिन गर्न सक्नुहुन्छ।"
        )
    except sqlite3.IntegrityError:
        print("❌ यो युजरनेम पहिले नै कसैले लिइसकेको छ!")
    finally:
        conn.close()


def login():
    global current_user
    print("\n--- 🔑 लगिन (Login) ---")
    username = input("युजरनेम हान्नुहोस्: ").strip().lower()
    password = input("पासवर्ड हान्नुहोस्: ")

    # डेटाबेसबाट युजर चेक गर्ने (SELECT)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password),
    )
    user = cursor.fetchone()
    conn.close()

    if user:
        current_user = username
        print(f"🎉 स्वागत छ {username}! तपाईं सफलतापूर्वक लगिन हुनुभयो।")
        show_dashboard()
    else:
        print("❌ गलत युजरनेम वा पासवर्ड! फेरि प्रयास गर्नुहोस्।")


def show_dashboard():
    global current_user
    while current_user:
        print(f"\n=============================")
        print(f"📊 NEPSE TALLY DASHBOARD ({current_user.upper()})")
        print(f"=============================")
        print("1. सेयर कारोबार रेकर्ड गर्ने (Buy/Sell) - [Coming Soon]")
        print("2. पोर्टफोलियो हेर्ने (View Portfolio) - [Coming Soon]")
        print("3. लगआउट गर्ने (Logout)")

        choice = input("\nके करना चाहनुहुन्छ? (१-३) हान्नुहोस्: ").strip()

        if choice == "1" or choice == "2":
            print(
                "\n🚀 अर्को सेसनमा हामी सेयर किनेको रेकर्ड पनि यही डेटाबेसमा सेभ गर्ने बनाउनेछौँ!"
            )
        elif choice == "3":
            print(f"\n👋 बाइ-बाइ {current_user}! सुरक्षित रूपमा लगआउट भयो।")
            current_user = None
        else:
            print("❌ गलत विकल्प! १, २ वा ३ मात्र थिच्नुहोस्।")


def main():
    while True:
        print("\n==============================")
        print("🇳🇵 नेप्से ट्याली एप (डेटाबेस संस्करण)")
        print("==============================")
        print("1. लगिन (Login)")
        print("2. नयाँ अकाउन्ट बनाउने (Register)")
        print("3. एप बन्द गर्ने (Exit)")

        choice = input("\nविकल्प छान्नुहोस् (१-३): ").strip()

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            print("\n🙏 एप प्रयोग गर्नुभएकोमा धन्यवाद। दिन शुभ रहोस्!")
            sys.exit()
        else:
            print("❌ अमान्य नम्बर! कृपया १, २ वा ३ मात्र छान्नुहोस्।")


if __name__ == "__main__":
    main()