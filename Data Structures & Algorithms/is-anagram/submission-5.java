class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap <Character, Integer> scounter = new HashMap<>();
        HashMap <Character, Integer> tcounter = new HashMap<>();
        for (int i = 0; i < s.length(); i++){
            char c1 = s.charAt(i);
            scounter.put(c1, scounter.getOrDefault(c1, 0) + 1);
        }
        for (int i = 0; i < t.length(); i++){
            char c2 = t.charAt(i);
            tcounter.put(c2, tcounter.getOrDefault(c2, 0) + 1);
        }
        if (scounter.equals(tcounter)){
            return true;
        }
        return false;
    }
}
