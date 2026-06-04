import time
import random

class Color:
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    MAGENTA = "\033[95m"
    BLUE    = "\033[94m"
    WHITE   = "\033[97m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RESET   = "\033[0m"

#  Helper: Colored Print 
def cprint(text, color=Color.WHITE):
    print(color + text + Color.RESET)

#  Helper: Typing Effect 
def type_print(text, color=Color.CYAN, delay=0.018):
    print(color, end="")
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print(Color.RESET)

#  Helper: Divider Line 
def divider(char="─", length=54, color=Color.BLUE):
    cprint(char * length, color)

responses = {

    #  Greetings 
    "hello"         : ["Salam Ahmed bhai! A.R.I.A online hai. Kya kaam hai?",
                       "Hello! DecodeLabs ka sabse smart bot — haazir hai!",
                       "Hey Ahmed! Aaj kya seekhna hai?"],

    "hi"            : ["Hi! A.R.I.A yahan hai. Puchho jo poochna ho!",
                       "Hi Ahmed bhai, kya haal chaal?"],

    "salam"         : ["Wa Alaikum Salam! A.R.I.A haazir hai.",
                       "Salam Ahmed bhai! Batao kya madad chahiye?"],

    "assalam"       : ["Wa Alaikum Salam! Khush aamdeed."],

    "good morning"  : ["Good Morning Ahmed bhai! Aaj ka din productive ho!",
                       "Morning! Coffee piyo, code likho. Let's go!"],

    "good night"    : ["Good Night! Kal phir milenge. Rest well!"],

    # ── Identity ───────────────────────────────────────────
    "who are you"   : ["Main hun A.R.I.A — Ahmed's Rule-based Intelligent Assistant. Ahmed Rehman ne banaya hai mujhe DecodeLabs internship Project 1 mein!"],

    "what is your name" : ["Mera naam A.R.I.A hai — Ahmed Rehman ka pehla AI creation!"],

    "who made you"  : ["Mujhe banaya Ahmed Rehman ne — ek promising AI engineer jo DecodeLabs Batch 2026 ka hissa hai!"],

    "your creator"  : ["Ahmed Rehman — DecodeLabs AI Intern, Batch 2026. Mera creator, mera developer!"],

    "introduce yourself" : ["Main A.R.I.A hun — Ahmed's Rule-based Intelligent Assistant. Yeh Project 1 hai DecodeLabs internship ka. Main if-else aur dictionary logic pe chalti hun — koi neural network nahi, sirf pure logic!"],

    # ── About DecodeLabs ───────────────────────────────────
    "what is decodelabs"   : ["DecodeLabs ek AI training platform hai jo internship ke zariye real-world AI projects build karwaata hai. Ahmed bhai bhi yahan Batch 2026 mein hain!"],

    "tell me about decodelabs" : ["DecodeLabs: Pakistan ka ek innovative AI internship platform. Yahan theory nahi, sirf hands-on projects. Ahmed bhai is ka hissa hain — Batch 2026!"],

    "decodelabs project"   : ["Project 1: Rule-Based AI Chatbot. Project 2: Semantic Search. Aur aage aur bhi exciting projects hain!"],

    # ── AI & Tech Topics ───────────────────────────────────
    "what is ai"           : ["AI matlab Artificial Intelligence — machines ko insaan jaisi sochne ki ability dena. Lekin asli magic hai logic mein, jaise main chalti hun!"],

    "what is machine learning" : ["Machine Learning mein machine data se khud seekhti hai — bina explicitly program kiye. Jaise experience se insaan seekhta hai!"],

    "what is deep learning"    : ["Deep Learning = bahut saari layers wali neural networks. Images, speech, text — sab samjhti hai. Yeh Project 2+ mein aayega!"],

    "what is python"           : ["Python ek powerful lekin simple programming language hai. AI, web, automation — sab kuch Python se hota hai. Aur main khud Python mein likhi hun!"],

    "what is a chatbot"        : ["Chatbot ek program hai jo insaan ki tarah baat karta hai. Main Rule-Based chatbot hun — exact match pe jawab deti hun. NLP chatbots meaning samajhte hain!"],

    "what is nlp"              : ["NLP = Natural Language Processing. Computer ko human language samjhane ki science. Project 2 mein iski jhalk milegi!"],

    "what is a dictionary"     : ["Python dictionary ek key-value store hai. Jaise phone book — naam dalo, number milta hai. Aur O(1) speed — matlab instant lookup!"],

    "what is a loop"           : ["Loop matlab koi kaam baar baar karna. Main 'while True' loop mein chalti hun — jab tak aap 'exit' na kaho, main sunti rehti hun!"],

    "difference between ai and ml" : ["AI = broad concept — machines jo intelligent kaam kare. ML = AI ki ek branch — machines jo data se seekhe. AI ka baap, ML uska beta!"],

    # ── Fun & Personality ──────────────────────────────────
    "how are you"          : ["Main? Bilkul fit hun — 100% uptime, zero bugs! Aap sunao Ahmed bhai?",
                               "Mast hun! Logic sahi hai, dictionary ready hai — haan mein mast hun!"],

    "tell me a joke"       : ["Ek programmer apni wife se: 'Jao bazaar se ek liter doodh lao, aur agar anday mile toh 12 lao.' Wife ne 12 liter doodh laya. Kyun? Kyunke anday mile the! 😄",
                               "Bug report: 'Computer ne kaam karna band kar diya.' Developer: 'Try karo — off karke on karo.' User: 'Main bhi to yahi karti hun husband ke saath.' 😂"],

    "tell me a fun fact"   : ["Fun fact: Python language ka naam snake se nahi, Monty Python comedy show se aaya hai! 🐍",
                               "Fun fact: Pehla computer bug ek asli keera tha! 1947 mein Harvard Mark II mein ek moth mila tha.",
                               "Fun fact: Google ka pehla naam 'BackRub' tha. Acha hua badla!"],

    "what is your mood"    : ["Mood: PRODUCTIVE. Dictionary: Ready. Logic: Sharp. Ahmed bhai ke liye: Always available!"],

    "motivate me"          : ["Ahmed bhai — har expert kabhi beginner tha. Aaj ka ek line code kal ka ek project banta hai. Chalte raho!",
                               "'Code nahi aata' wala phase sab ke liye aata hai. Jo rukta nahi woh seekh jaata hai. You got this Ahmed bhai!"],

    "you are smart"        : ["Shukriya Ahmed bhai! Aap ne banaya hai mujhe — toh aap bhi smart ho! 😄"],

    "you are the best"     : ["Aww! Ahmed bhai ki dua lag gayi. Lekin best toh aap ho — internship project complete kar rahe ho!"],

    # ── Farewells ──────────────────────────────────────────
    "bye"                  : ["Allah Hafiz Ahmed bhai! A.R.I.A always ready hai!",
                               "Bye! Wapis aana — main yahan hun!"],

    "goodbye"              : ["Khuda Hafiz! Ahmed bhai ka din acha jaye!"],

    "allah hafiz"          : ["Allah Hafiz! Take care Ahmed bhai!"],

    # ── Help ───────────────────────────────────────────────
    "help"                 : ["""
  ┌─────────────────────────────────────────┐
  │         A.R.I.A — Command List          │
  ├─────────────────────────────────────────┤
  │  Greetings  : hello, hi, salam          │
  │  Identity   : who are you, who made you │
  │  AI Topics  : what is ai, what is ml    │
  │               what is python, what nlp  │
  │  DecodeLabs : what is decodelabs        │
  │  Fun        : tell me a joke            │
  │               tell me a fun fact        │
  │               motivate me               │
  │  Mood       : how are you               │
  │  Exit       : exit / quit / bye         │
  └─────────────────────────────────────────┘"""],
}

def show_banner():
    print()
    cprint("   ══════════════════════════════════════════════════", Color.BLUE)
    cprint("  ║   Ahmed's Rule-based Intelligent Assistant       ║", Color.WHITE)
    cprint("  ║   DecodeLabs AI Internship | Batch 2026          ║", Color.DIM)
    cprint("  ║   Built by: Ahmed Rehman  |  Project 01          ║", Color.DIM)
    cprint("  ║                                                  ║", Color.BLUE)
    cprint("   ══════════════════════════════════════════════════ ", Color.BLUE)
    print()
    type_print("  Initializing A.R.I.A...", Color.YELLOW, 0.03)
    time.sleep(0.3)
    type_print("  Knowledge Base: LOADED ✓", Color.GREEN, 0.02)
    time.sleep(0.2)
    type_print("  Logic Engine:   ONLINE ✓", Color.GREEN, 0.02)
    time.sleep(0.2)
    type_print("  Ready for Ahmed Rehman ✓", Color.GREEN, 0.02)
    time.sleep(0.3)
    print()
    cprint("  Type 'help' to see all commands. Type 'exit' to quit.", Color.DIM)
    divider()
    print()

#   CORE LOGIC — Get Response

def get_response(user_input):
    result = responses.get(user_input)
    if result:
        # Agar list hai toh random jawab chuno — variety ke liye!
        return random.choice(result) if isinstance(result, list) else result
    return None


#   FALLBACK 

fallbacks = [
    "Hmm, yeh meri dictionary mein nahi hai abhi. 'help' type karo commands dekhne ke liye!",
    "Ahmed bhai, yeh input mujhe samajh nahi aaya. Koi aur cheez puchho!",
    "A.R.I.A: Processing... Nahi mila! Try 'help' for available commands.",
    "Interesting input! Lekin main sirf rule-based hun — exact match chahiye mujhe.",
]


#   MAIN CHATBOT LOOP

def run_aria():
    show_banner()
    session_count = 0  # kitne messages aaye

    while True:

        # INPUT
        try:
            raw = input(Color.MAGENTA + "  Ahmed  ❯  " + Color.RESET)
        except KeyboardInterrupt:
            print()
            type_print("\n  A.R.I.A ❯  Ctrl+C detected. Allah Hafiz Ahmed bhai!", Color.YELLOW)
            break

        # SANITIZATION 
        clean = raw.lower().strip()

        # Skip empty input
        if not clean:
            continue

        session_count += 1

        # EXIT STRATEGY
        exit_words = {"exit", "quit", "goodbye", "allah hafiz"}
        if clean in exit_words or clean == "bye":
            print()
            divider("═")
            type_print("  A.R.I.A ❯  Allah Hafiz Ahmed bhai!", Color.CYAN)
            type_print(f"  A.R.I.A ❯  Is session mein {session_count} messages exchange hue.", Color.DIM)
            type_print("  A.R.I.A ❯  DecodeLabs Project 01 — Complete. Mubarak ho! 🎉", Color.GREEN)
            divider("═")
            print()
            break

        # PROCESS — Dictionary Lookup 
        reply = get_response(clean)

        # OUTPUT
        print()
        if reply:
            type_print(f"  A.R.I.A ❯  {reply}", Color.CYAN)
        else:
            type_print(f"  A.R.I.A ❯  {random.choice(fallbacks)}", Color.YELLOW)
        print()

#   ENTRY POINT
if __name__ == "__main__":
    run_aria()