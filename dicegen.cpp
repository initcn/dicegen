#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <sstream>
#include <cstdlib>
#include <random> // Modern C++ secure random

// Extract the directory path of the executable
std::string get_base_dir(const std::string& exec_path) {
    size_t pos = exec_path.find_last_of("/\\");
    if (pos == std::string::npos) return ".";
    return exec_path.substr(0, pos);
}

// Roll a standard 6-sided die securely using modern C++
int roll_die() {
    // std::random_device natively hooks into /dev/urandom on Linux or CryptGenRandom on Windows.
    // 'static' ensures we only initialize the entropy pool hook once per run.
    static std::random_device rd; 
    
    // std::uniform_int_distribution automatically handles modulo bias.
    static std::uniform_int_distribution<int> dist(1, 6);
    
    return dist(rd);
}

// Generate a Diceware code of a specific width (e.g., 5 dice = "43146")
std::string get_code(int width) {
    std::string code = "";
    for (int i = 0; i < width; i++) {
        code += std::to_string(roll_die());
    }
    return code;
}

// Load the Diceware wordlist into an unordered_map
std::unordered_map<std::string, std::string> load_wordlist(const std::string& path) {
    std::unordered_map<std::string, std::string> words;
    std::ifstream file(path);

    if (!file.is_open()) {
        std::cerr << "[ERROR] Wordlist not found: " << path << std::endl;
        exit(1);
    }

    std::string line;
    while (std::getline(file, line)) {
        std::istringstream iss(line);
        std::string code, word;
        // The wordlists are formatted as "<code_digits> <word>"
        if (iss >> code >> word) {
            words[code] = word;
        }
    }
    return words;
}

void print_usage(const char* prog_name) {
    std::cout << "Usage: " << prog_name << " [-w 4|5] [-n words]\n"
              << "Secure Diceware passphrase generator\n\n"
              << "Options:\n"
              << "  -w    Wordlist width: 4 = short list, 5 = large list (default: 5)\n"
              << "  -n    Number of words to generate (default: 6)\n"
              << "  -h    Show this help message\n";
}

int main(int argc, char *argv[]) {
    int width = 5;
    int num_words = 6;

    // Simple argument parsing
    for (int i = 1; i < argc; i++) {
        std::string arg = argv[i];
        if (arg == "-h" || arg == "--help") {
            print_usage(argv[0]);
            return 0;
        } else if (arg == "-w" && i + 1 < argc) {
            width = std::stoi(argv[++i]);
        } else if (arg == "-n" && i + 1 < argc) {
            num_words = std::stoi(argv[++i]);
        } else {
            std::cerr << "[ERROR] Unknown or incomplete argument: " << arg << std::endl;
            print_usage(argv[0]);
            return 1;
        }
    }

    // Input validation
    if (width != 4 && width != 5) {
        std::cerr << "[ERROR] Width must be 4 or 5." << std::endl;
        return 1;
    }
    if (num_words <= 0) {
        std::cerr << "[ERROR] Number of words must be greater than 0." << std::endl;
        return 1;
    }

    // Determine wordlist path based on the executable's location
    std::string base_dir = get_base_dir(argv[0]);
    std::string wordlist_filename = (width == 4) ? "eff_short_wordlist_2_0.txt" : "eff_large_wordlist.txt";
    
    // Cross-platform path joining
    std::string wordlist_path = base_dir + "/" + wordlist_filename;

    // Load the dictionary mapping
    auto wordlist = load_wordlist(wordlist_path);

    std::vector<std::string> words;
    std::cout << "\nGenerated values:\n\n";

    // Generate the rolls and lookup words
    for (int i = 0; i < num_words; i++) {
        std::string code = get_code(width);
        std::string word = "missing";

        auto it = wordlist.find(code);
        if (it != wordlist.end()) {
            word = it->second;
        }

        std::cout << code << " -> " << word << "\n";
        words.push_back(word);
    }

    // Print the final joined passphrase
    std::cout << "\nPassphrase:\n\n";
    for (size_t i = 0; i < words.size(); i++) {
        std::cout << words[i];
        if (i < words.size() - 1) {
            std::cout << "-";
        }
    }
    std::cout << "\n" << std::endl;

    return 0;
}