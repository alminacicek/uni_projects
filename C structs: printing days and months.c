/******************************************************************************
week 2 assignment:using structs
alminacck
*******************************************************************************/
#include <stdio.h>
#include<ctype.h>

typedef enum month{ jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec} month;

typedef struct date
{ 
    month m; 
    int d
}date;

void nextday(date *dt) //we use a pointer because we want to edit the struct
{ 
    switch(dt->m){
    case feb:
    {
        if((dt->d)<28)
            dt->d++;
            
        else if((dt->d)==28)
        {
            dt-> d=1;
            dt->m++;
            
        }
        else if((dt->d)>28)
        printf("error\n");
    };break;
    case apr:
    case jun:
    case sep:
    case nov:
    {
        if((dt->d)<30)
        {
            dt->d++;
        }
        else if((dt->d)==30)
        {
            dt-> d=1;
            dt-> m++;
            
        }
        else if((dt->d)>30)
        printf("error\n");
        
    };break;
    case dec:
    {
        if((dt->d)<31)
        {
            dt->d++;
        }
        else if((dt->d)==31)
        {
            dt-> d=1;
            dt-> m=0;
            
        }
        else if((dt->d)>31)
        printf("error\n");
        
    };break;
    case jan:
    case mar:
    case may:
    case jul:
    case aug:
    case oct:
    
    {
        if((dt->d)<31)
        {
            dt->d++;
        }
        else if((dt->d)==31)
        {
            dt-> d=1;
            dt-> m++;
            
        }
        else if((dt->d)>31)
        printf("error\n");
        
    };break;
}
}

void printdate(date *dt)
{
    printf("the date is: ");
    switch(dt->m){
        case jan: printf("January ");break;
        case feb: printf("February ");break;
        case mar: printf("March ");break;
        case apr: printf("April ");break;
        case may: printf("May ");break;
        case jun: printf("June ");break;
        case jul: printf("July ");break;
        case aug: printf("August ");break;
        case sep: printf("September ");break;
        case oct: printf("October ");break;
        case nov: printf("November ");break;
        case dec: printf("December ");break;
    }
    printf("%d\n",dt->d);
}

int main()
{
    struct date today;
    
    today.m = feb;
    today.d= 28;
    
    printdate(&today);
    
    nextday(&today);
    
    printf("next day ");
    printdate(&today);
    
    return 0;
}




