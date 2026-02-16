#include<stdio.h>
int main(){
    int x=10;
    printf("%p", &x);

    x=20;
    printf("\n\n%p", &x);
}