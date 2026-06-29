class Solution {
public:
    bool isAnagram(string s, string t) {

        if (s.size() != t.size()) {return false;}
        unordered_map<char,int> map1, map2;

        for (int i = 0; i < s.size(); ++i) {
            map1[s[i]]++; map2[t[i]]++;}

        for (int i = 0; i < s.size(); ++i) {
            if (map2.find(s[i]) == map2.end() ||
            map1[s[i]] != map2[s[i]]) {return false;}}

        return true;}
};
