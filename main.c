#include<stdio.h>
#include<stdlib.h>
#include "video.h"

int V = -1;
int R = -1;
int X = -1;
int E = -1;
int C = -1;

int parse_first_line(char *str) {
  int i = 0;

  V = atoi(&str[i]);
  while (str[i] != ' ' &&  str[i] != '\n'  && str[i] != '\0')
    i++;
  i++;

  E = atoi(&str[i]);
  while (str[i] != ' ' &&  str[i] != '\n'  && str[i] != '\0')
    i++;
    i++;

  R = atoi(&str[i]);
  while (str[i] != ' ' &&  str[i] != '\n'  && str[i] != '\0')
  i++;
  i++;

  C = atoi(&str[i]);
  while (str[i] != ' ' &&  str[i] != '\n'  && str[i] != '\0')
  i++;
  i++;

  X = atoi(&str[i]);
  return (0);
}

int   main(int argc, char **argv)
{
  FILE *stream;
  char *line = NULL;
  size_t len = 0;
  ssize_t read;
  char data;

  stream = fopen(argv[1], "r");
  if (stream == NULL)
      exit(EXIT_FAILURE);
  read = getline(&line, &len, stream);
  get_nb(line);
  printf("V: %d\nE: %d\nR: %d\nC: %d\nX: %d\n", V, E, R, C, X);
  // while ((read = getline(&line, &len, stream)) != -1) {
  // }

  free(line);
  fclose(stream);
  return (EXIT_SUCCESS);
}
