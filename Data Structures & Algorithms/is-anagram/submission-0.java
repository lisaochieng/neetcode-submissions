class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap <Character, Integer> s_letters = new HashMap <>();
        HashMap <Character, Integer> t_letters = new HashMap <>();

        for (char c:s.toCharArray()){
            s_letters.put(c,s_letters.getOrDefault(c,0)+1);
        }
        for (char c:t.toCharArray()){
            t_letters.put(c,t_letters.getOrDefault(c,0)+1);
        }

        if (s_letters.equals(t_letters)){
            return true;
        }
        return false;

    }
}
