#include<stdio.h>
int main(){
	// variables
	int start,end,cnt=0;
	
	FILE *f1; // file opening
	f1 = fopen("prime.txt","a"); // using append
	
	//error handling
	if (f1 == NULL) {
    printf("Error opening file!\n");
    return 1;
	}
	
	printf("Enter starting number = "); // getting starting number
	scanf("%d",&start);
	fprintf(f1,"\n-----------------------------------------------------------------------------------------------------------------------------");
	fprintf(f1,"\nEnter starting number = %d",start); // printing startng num in file
	printf("\nEnter ending number = "); // getting ending number
	scanf("%d",&end);
	fprintf(f1,"\nEnter ending number = %d\n",end); // printing ending number in file
	
		printf("\nPrime number\t");
		fprintf(f1,"\nPrime numbers = ");
		// logic for getting prime numbers between entered numbers
		for(int i=start;i<=end;i++){
		cnt=0;
		for(int j=2;j<i;j++){
			if(i%j==0){
				cnt++;
			}
		}
		if(cnt==0){
			printf("\t%d",i);
			fprintf(f1,"\t%d",i);

		}
	}
		// logic for getting non prime numbers between entered numbers
		printf("\n\nNon prime number");
		fprintf(f1,"\nNon Prime numbers = ");
		for(int i=start;i<=end;i++){
		cnt=0;
		for(int j=2;j<i;j++){
			if(i%j==0){
				cnt++;
			}
		}
		if(cnt!=0){
			printf("\t%d",i);
			fprintf(f1,"\t%d",i);

		}
	}
	fprintf(f1,"\n-----------------------------------------------------------------------------------------------------------------------------\n");
	fclose(f1); // file closed
	
	return 0;
}
