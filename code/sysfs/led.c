#include <stdio.h>
#include <stddef.h>
#include <time.h>

#define on "255"
#define off "0"

#define led1 "/sys/class/leds/ev3\:left\:green\:ev3dev\brightness"

void delay(init millseconds) {
  long pause;
  clock_t now, then;
  pause = milliseconds*(CLOCKS_PER_SEC/1000);
  now = then = clock();
  while（ （now-then) < pause)
    now = clock();
  }
}

int  main (void) {

  // define file handles for led1
  FILE *ifp_led1;

  // led1 on

  // make ifp_led1 as writable
  ifp_led1 = fopen(led1, "w");
  // fail to oepn
  if(ifp_led1 == NULL) {printf("Unable to open.\n");}
  // led1 on
  fseek(ifp_led1, on, SEEK_SET);
  // print the state
  fprintf(ifp_led1, "%s",  on);
  // flush
  fflush(ifp_led1);
  // close files
  fclose(ifp_led1);

  // waiting for 1 second
  delay(1000);

  // led1 off

  // make ifp_led1 as writable
  ifp_led1 = fopen(led1, "w");
  // fail to oepn
  if(ifp_led1 == NULL) {printf("Unable to open.\n");}
  // led1 off
  fseek(ifp_led1, off, SEEK_SET);
  // print the state
  fprintf(ifp_led1, "%s",  on);
  // flush
  fflush(ifp_led1);
  // close files
  fclose(ifp_led1);


  return 0;
}


