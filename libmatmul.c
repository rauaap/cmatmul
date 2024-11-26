#include <stdio.h>
#include <time.h>
#include <stdlib.h>

typedef struct {
    size_t rows;
    size_t cols;
    int** arr;
} matrix;

matrix make_matrix(size_t rows, size_t cols) {
    matrix ret;
    ret.rows = rows;
    ret.cols = cols;

    ret.arr = (int**)malloc(rows* sizeof(int*));

    for (size_t i = 0; i < rows; i++) {
        ret.arr[i] = malloc(cols* sizeof(int));
    }

    return ret;
}

void destroy_matrix(matrix* m) {
    for (size_t i = 0; i < m->rows; i++) {
        free(m->arr[i]);
    }

    free(m->arr);
}

void print_matrix(matrix* m, char name) {
    printf("%c = [\n", name);

    for (size_t y = 0; y < m->rows; y++) {
        printf("\t[ ");

        for (size_t x = 0; x < m->cols; x++) {
            printf("%d, ", m->arr[y][x]);
        }

        printf("],\n");
    }

    printf("]\n\n");
}

matrix matmul(matrix* a, matrix* b) {
    size_t a_rows = a->rows;
    matrix ret = make_matrix(a_rows, a_rows);

    for (size_t y = 0; y < a_rows; y++) {
        for (size_t x = 0; x < a_rows; x++) {
            int sum = 0;

            for (size_t i = 0; i < b->rows; i++) {
                sum += a->arr[y][i] * b->arr[i][x];
            }

            ret.arr[y][x] = sum;
        }
    }

    return ret;
}

int main(void) {
    srand(time(NULL));

    size_t alen = rand() % 10;
    size_t blen = rand() % 10;

    matrix a = make_matrix(alen, blen);
    matrix b = make_matrix(blen, alen);

    for (size_t y = 0; y < alen; y++) {
        for (size_t x = 0; x < blen; x++) {
            a.arr[y][x] = rand() % 50;
            b.arr[x][y] = rand() % 50;
        }
    }

    matrix c = matmul(&a, &b);

    print_matrix(&a, 'a');
    print_matrix(&b, 'b');
    print_matrix(&c, 'c');

    destroy_matrix(&a);
    destroy_matrix(&b);
    destroy_matrix(&c);
}
