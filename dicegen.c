#include <stdio.h>
#include <stdlib.h>

#ifdef _WIN32
    #include <windows.h>
    #include <bcrypt.h>
    #pragma comment(lib, "bcrypt.lib")
#else
    #include <sys/random.h>
    #include <errno.h>
#endif

int secure_random_byte(unsigned char *b) {

#ifdef _WIN32

    if (BCryptGenRandom(
            NULL,
            b,
            1,
            BCRYPT_USE_SYSTEM_PREFERRED_RNG) != 0) {
        return -1;
    }

#else

    ssize_t result;

    do {
        result = getrandom(b, 1, 0);
    } while (result == -1 && errno == EINTR);

    if (result != 1) {
        return -1;
    }

#endif

    return 0;
}

int roll_die() {

    unsigned char b;

    do {
        if (secure_random_byte(&b) != 0) {
            return -1;
        }
    } while (b >= 252);

    return (b % 6) + 1;
}

int main(int argc, char *argv[]) {

    if (argc != 2) {
        fprintf(stderr, "Usage: %s <digits>\n", argv[0]);
        return 1;
    }

    int digits = atoi(argv[1]);

    if (digits <= 0) {
        fprintf(stderr, "Invalid digit count\n");
        return 1;
    }

    for (int i = 0; i < digits; i++) {

        int die = roll_die();

        if (die == -1) {
            return 1;
        }

        printf("%d", die);
    }

    printf("\n");

    return 0;
}

// gcc dicegen.c -o dicegen
// gcc dicegen.c -lbcrypt -o dicegen.exe

