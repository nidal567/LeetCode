#include <stdbool.h>
#include <string.h>

bool isSubsequence(char* s, char* t) {
    int i = 0, j = 0;
    int len_s = strlen(s);
    int len_t = strlen(t);

    while (i < len_s && j < len_t) {
        if (s[i] == t[j]) {
            i++;
        }
        j++;
    }

    return i == len_s;
}