class Solution {
public:
    bool isAnagram(std::string s, std::string t) {

    if (s.size() != t.size()) return false;

    int alph[26] = {0};
    for (int i = 0; i < s.size(); ++i) {
        alph[s[i] - 'a']++;
        alph[t[i] - 'a']--;
    }

    for (int count : alph) {
        if (count != 0) return false;
    }
    return true;}
};
