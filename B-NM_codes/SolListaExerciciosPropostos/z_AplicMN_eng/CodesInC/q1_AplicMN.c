#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 10

// =====================================
// ALTERE APENAS AQUI
// =====================================
typedef double REAL;   // alta precisão
typedef float  REAL32; // baixa precisão
// =====================================

int main() {

    int i;

    REAL x[N];
    REAL32 x32[N];

    srand(42);

    // ---------------------------------------------
    // Geração dos dados
    // ---------------------------------------------
    for(i = 0; i < N; i++) {
        x[i] = ((REAL) rand() / RAND_MAX) * 10.0;
        x32[i] = (REAL32) x[i];  // conversão
    }

    // ---------------------------------------------
    // Cálculo dos erros
    // ---------------------------------------------
    REAL erro_abs[N];
    REAL erro_rel[N];

    REAL soma_erro_abs = 0.0;
    REAL soma_erro_rel = 0.0;

    for(i = 0; i < N; i++) {

        erro_abs[i] = fabs(x[i] - (REAL)x32[i]);

        if(x[i] != 0.0)
            erro_rel[i] = fabs((x[i] - (REAL)x32[i]) / x[i]);
        else
            erro_rel[i] = 0.0;

        soma_erro_abs += erro_abs[i];
        soma_erro_rel += erro_rel[i];
    }

    REAL erro_abs_medio = soma_erro_abs / N;
    REAL erro_rel_medio = soma_erro_rel / N;

    printf("Erro absoluto medio: %e\n", erro_abs_medio);
    printf("Erro relativo medio: %e\n", erro_rel_medio);

    // ---------------------------------------------
    // Impacto no somatório
    // ---------------------------------------------
    REAL soma64 = 0.0;
    REAL soma32 = 0.0;

    for(i = 0; i < N; i++) {
        soma64 += x[i];
        soma32 += (REAL)x32[i];
    }

    REAL erro_soma_abs = fabs(soma64 - soma32);
    REAL erro_soma_rel = erro_soma_abs / soma64;

    printf("\nSoma (alta precisao): %f\n", soma64);
    printf("Soma (baixa precisao): %f\n", soma32);

    printf("\nErro absoluto na soma: %e\n", erro_soma_abs);
    printf("Erro relativo na soma: %e\n", erro_soma_rel);

    // ---------------------------------------------
    // Diagnóstico ponto a ponto (FINAL)
    // ---------------------------------------------
    printf("\n====================================================\n");
    printf("Diagnostico ponto a ponto (primeiros 10 valores):\n");
    printf("====================================================\n");

    for(i = 0; i < 10; i++) {
        printf("i=%02d | x=%.10f | x32=%.10f | erro_abs=%.10e | erro_rel=%.10e\n",
               i,
               x[i],
               (REAL)x32[i],
               erro_abs[i],
               erro_rel[i]);
    }

    printf("====================================================\n");

    return 0;
}