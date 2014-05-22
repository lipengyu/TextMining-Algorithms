package org.psychocoder.textprocessing.editdistance;

/**
 *
 * @author psychocoder
 * @version 1.0
 */
public class DamerauLavenshtein {

    private String s1;
    private String s2;
    private int len_s1;
    private int len_s2;

    public DamerauLavenshtein() {
        s1 = null;
        s2 = null;
    }

    public DamerauLavenshtein(String s1, String s2) {
        this.s1 = s1.toLowerCase();
        this.s2 = s2.toLowerCase();
    }

    private void putValue(String m, String n) {
        s1 = m.toLowerCase();
        s2 = n.toLowerCase();
    }

    private int getMinimum(int a, int b, int c) {
        return Math.min(a, Math.min(b, c));
    }

    private int getDamerauLavenshtein() {

        len_s1 = s1.length();
        len_s2 = s2.length();

        int[][] d = new int[len_s1 + 1][len_s2 + 1];
        int i, j, cost;

        if (len_s1 == 0) {
            return len_s2;
        }

        if (len_s2 == 0) {
            return len_s1;
        }

        for (i = 0; i <= len_s1; i++) {
            d[i][0] = i;
        }

        for (j = 0; j <= len_s2; j++) {
            d[0][j] = j;
        }

        for (i = 1; i <= len_s1; i++) {
            for (j = 1; j <= len_s2; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    cost = 0;
                } else {
                    cost = 1;
                }

                d[i][j] = getMinimum(
                        d[i - 1][j] + 1, /*Deletion*/
                        d[i][j - 1] + 1, /*Insertion*/
                        d[i - 1][j - 1] + cost /*Substitution*/
                );

                if (i > 1 && j > 1 && s1.charAt(i - 1) == s2.charAt(j - 1)
                        && s2.charAt(j - 1) == s1.charAt(i - 1)) {
                    d[i][j] = Math.min(d[i][j], d[i - 2][j - 2] + cost);  /*transposition*/

                }
            }
        }

        return d[len_s1][len_s2];
    }

    private int getDamerauLavenshtein(String s1, String s2) {

        s1 = s1.toLowerCase();
        s2 = s2.toLowerCase();

        len_s1 = s1.length();
        len_s2 = s2.length();

        int[][] d = new int[len_s1 + 1][len_s2 + 1];
        int i, j, cost;

        for (i = 0; i <= len_s1; i++) {
            d[i][0] = i;
        }

        for (j = 0; j <= len_s2; j++) {
            d[0][j] = j;
        }

        for (i = 1; i <= len_s1; i++) {
            for (j = 1; j <= len_s2; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    cost = 0;
                } else {
                    cost = 1;
                }

                d[i][j] = getMinimum(
                        d[i - 1][j] + 1, /*Deletion*/
                        d[i][j - 1] + 1, /*Insertion*/
                        d[i - 1][j - 1] + cost /*Substitution*/
                );

                if (i > 1 && j > 1 && s1.charAt(i - 1) == s2.charAt(j - 1)
                        && s2.charAt(j - 1) == s1.charAt(i - 1)) {
                    d[i][j] = Math.min(d[i][j], d[i - 2][j - 2] + cost);  /*transposition*/

                }
            }
        }

        return d[len_s1][len_s2];

    }

    public static void main(String... args) {
        DamerauLavenshtein ob = new DamerauLavenshtein("Ludo", "lludo");
        System.out.println(ob.getDamerauLavenshtein());
        System.out.println(ob.getDamerauLavenshtein("Hello", "olhel"));
    }

}
