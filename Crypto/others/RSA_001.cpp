#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cctype>
#include <iomanip>
using namespace std;

// Generate random key
unordered_map<char, char> generate_key(vector<char>& cipher_alphabet) {
    vector<char> plain_alphabet;
    for (char c = 'A'; c <= 'Z'; ++c)
        plain_alphabet.push_back(c);

    cipher_alphabet = plain_alphabet;
    random_shuffle(cipher_alphabet.begin(), cipher_alphabet.end());

    unordered_map<char, char> key;
    for (int i = 0; i < 26; ++i) {
        key[plain_alphabet[i]] = cipher_alphabet[i];
    }
    return key;
}

// Create reverse key for decryption
unordered_map<char, char> reverse_key(const unordered_map<char, char>& key) {
    unordered_map<char, char> rev;
    for (auto& pair : key)
        rev[pair.second] = pair.first;
    return rev;
}

// Encrypt function
string encrypt(const string& text, const unordered_map<char, char>& key) {
    string result;
    for (char ch : text) {
        if (isalpha(ch)) {
            char upper = toupper(ch);
            char enc = key.at(upper);
            result += isupper(ch) ? enc : tolower(enc);
        } else {
            result += ch;
        }
    }
    return result;
}

// Decrypt function
string decrypt(const string& text, const unordered_map<char, char>& rev_key) {
    string result;
    for (char ch : text) {
        if (isalpha(ch)) {
            char upper = toupper(ch);
            char dec = rev_key.at(upper);
            result += isupper(ch) ? dec : tolower(dec);
        } else {
            result += ch;
        }
    }
    return result;
}

// Frequency analysis
void frequency_analysis(const string& text) {
    unordered_map<char, int> freq;
    int total = 0;
    for (char ch : text) {
        if (isalpha(ch)) {
            char upper = toupper(ch);
            freq[upper]++;
            total++;
        }
    }
    cout << "\nFrequency Analysis:\n";
    for (char c = 'A'; c <= 'Z'; ++c) {
        if (freq[c] > 0) {
            double percentage = (freq[c] * 100.0) / total;
            cout << c << ": " << fixed << setprecision(2) << percentage << "%\n";
        }
    }
}

int main() {
    srand(time(0)); // Seed random

    string message;
    cout << "Enter Message: ";
    getline(cin, message);

    vector<char> cipher_alphabet;
    auto key = generate_key(cipher_alphabet);
    auto rev_key = reverse_key(key);

    string encrypted = encrypt(message, key);
    string decrypted = decrypt(encrypted, rev_key);

    cout << "\nEncrypted Message: " << encrypted << endl;
    cout << "Decrypted Message: " << decrypted << endl;

    frequency_analysis(encrypted);

    return 0;
}