import sys

# युजरहरूको डाटा सेभ गर्न एउटा अस्थायी डिक्सनरी (कम्प्युटर बन्द गरेपछि यो हराउँछ)
# Format -> "username": "password"
users_db = {
    "admin": "admin123",  # पहिले नै एउटा डिफल्ट युजर राख्दिएको
}

# अहिले लगिन भएको युजर को हो भनेर ट्र्याक गर्न
current_user = None


def register():
    print("\n--- 📝 नयाँ अकाउन्ट दर्ता (Register) ---")
    username = input("नयाँ युजरनेम राख्नुहोस्: ").strip().lower()

    if not username:
        print("❌ युजरनेम खाली छोड्न मिल्दैन!")
        return

    if username in users_db:
        print("❌ यो युजरनेम पहिले नै कसैले लिइसकेको छ!")
        return

    password = input("नयाँ पासवर्ड राख्नुहोस्: ")
    if len(password) < 4:
        print("❌ पासवर्ड कम्तीमा ४ अक्षरको हुनुपर्छ!")
        return

    # डेटाबेसमा सेभ गर्ने
    users_db[username] = password
    print(f"✅ अकाउन्ट सफलतापूर्वक बन्यो! अब लगिन गर्न सक्नुहुन्छ।")


def login():
    global current_user
    print("\n--- 🔑 लगिन (Login) ---")
    username = input("युजरनेम हान्नुहोस्: ").strip().lower()
    password = input("पासवर्ड हान्नुहोस्: ")

    # चेक गर्ने: युजर छ कि छैन र पासवर्ड मिल्छ कि मिल्दैन
    if username in users_db and users_db[username] == password:
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

        choice = input("\nके गर्न चाहनुहुन्छ? (१-३) हान्नुहोस्: ").strip()

        if choice == "1":
            print(
                "\n🚀 यो फिचर हामी अर्को स्टेपमा बनाउनेछौँ! (डाटाबेस सिकेपछि)"
            )
        elif choice == "2":
            print("\n📈 पोर्टफोलियो खाली छ। पहिले सेयर किन्नुहोस्!")
        elif choice == "3":
            print(f"\n👋 बाइ-बाइ {current_user}! सुरक्षित रूपमा लगआउट भयो।")
            current_user = None  # युजर खाली गर्ने
        else:
            print("❌ गलत विकल्प! १, २ वा ३ मात्र थिच्नुहोस्।")


# मुख्य प्रोग्राम लुप (Main Program Loop)
def main():
    while True:
        print("\n==============================")
        print("🇳🇵 नेप्से ट्याली एपमा स्वागत छ")
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


# प्रोग्राम सुरु गर्ने
if __name__ == "__main__":
    main()