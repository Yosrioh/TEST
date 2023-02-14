import itertools
import bip39
import bip32
import eth_utils
from eth_account import Account
from mnemonic import Mnemonic
# Define the known words, derivation path, and wallet address
known_words = ["love", "wedding", "husband", "wife", "marriage", "problem", "best", "friend", "affair", "baby", "reveal", "divorce", "body"]
derivation_path = "m/44'/60'/0'/0/0"
wallet_address = "0x50F2cf9Ba2B1fB8F41c425e609864d477A3263AC"



WORDS = [
   "love","romance", "passion", "devotion", "affection", "tenderness",
    "wedding","marriage", "ceremony", "nuptials", "celebration", "vow",
    "husband","spouse", "partner", "man", "mate", "groom",
    "wife","spouse", "partner", "woman", "bride", "mate",
    "marriage","union", "partnership", "commitment", "bond", "relationship",
    "problem","challenge", "difficulty", "obstacle", "issue", "dilemma",
    "best","top", "highest", "greatest", "excellent", "superb",
    "friend","companion", "ally", "confidant", "mate", "buddy",
    "affair","relationship", "liaison", "fling", "tryst", "entanglement",
    "baby","infant", "newborn", "child", "toddler", "offspring",
    "reveal","show", "display", "demonstrate", "unveil", "expose",
    "divorce","separation", "split", "breakup", "dissolution", "disunion",
    "body","physical", "anatomy", "form", "figure", "shape"
]
# Generate all possible combinations of the remaining 15 words
remaining_words = WORDS.copy()
for word in known_words:
    remaining_words.remove(word)

combinations = list(itertools.combinations(remaining_words, 11))

# Test each combination against the derivation path and wallet address
for i, combo in enumerate(combinations):
    phrase = " ".join(known_words + list(combo))
    seed = bip39.mnemonic_to_seed(phrase)
    master_key = bip32.BIP32.from_seed(seed)
    priv_key = master_key.derive_path(derivation_path).private_key.hex()

    # Derive public address from private key
    acct = Account.privateKeyToAccount(priv_key)
    pub_address = acct.address

    print(f"Testing combination {i+1}/{len(combinations)}: {phrase}")
    if pub_address.lower() == wallet_address.lower():
        print("SUCCESS: Found the correct mnemonic phrase!")
        print(f"Mnemonic phrase: {phrase}")
        print(f"Private key: {priv_key}")
        print(f"Public address: {pub_address}")
        break
