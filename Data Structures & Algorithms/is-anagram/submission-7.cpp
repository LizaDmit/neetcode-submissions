class Solution {
public:
    bool isAnagram(string s, string t) {

        if (s.size() != t.size()) return false;
        
        int mp[26] = {};

        for (int i = 0; i < s.size(); ++i) mp[s[i] - 'a']++;

        for (int i = 0; i < t.size(); ++i) mp[t[i] - 'a']--;

        for (int i = 0; i < 26; ++i) {
            if (mp[i]) return false;
        }

        return true;

    }

};
