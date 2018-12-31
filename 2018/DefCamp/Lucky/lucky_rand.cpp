#include <cstdlib>
#include <iostream>

int main(int argc, char const *argv[]) {
  srand(0x41414141);
  printf("[\n");
  for (int i = 1; i < 100; ++i) {
    printf("%d", rand());
    if (i != 0 && i % 10 == 0) {
      printf(",\n");
      continue;
    }
    if (i == 99) {
      printf("\n]\n");
      break;
    }
    printf(", ");
  }
  return 0;
}