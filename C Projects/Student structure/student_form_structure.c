#include<stdio.h>
#include<string.h>
struct Student{
	int std_id,maths,eng,sci;
	char std_name[50];
}s[50];
int main(){
		printf("\n\t\t\t\t\t\tDream International School\n");
		printf("------------------------------------------------------------------------------------------------------------------------");
		
		int size;
		
		printf("Enter the size: ");
		scanf("%d",&size);
		
		//getting values
		for(int i=0;i<size;i++){
			printf("Enter student Id = ");
			scanf("%d",&s[i].std_id);
			printf("Enter student Name = ");
			getchar();
			gets(s[i].std_name);
			//fgets(s[i].std_name, sizeof s[i].std_name, stdin);
			//scanf("%s",s[i].std_name); //doesnt get char after space
			printf("Enter Maths marks = ");
			scanf("%d",&s[i].maths);
			printf("Enter English marks = ");
			scanf("%d",&s[i].eng);
			printf("Enter Science marks = ");
			scanf("%d",&s[i].sci);
			printf("\n");
		}
		
		int total[100];
		float percentage[100];
		
		for(int i=0;i<size;i++){
			total[i] = s[i].maths + s[i].eng + s[i].sci;
			percentage[i] = (total[i]/300.0)*100;
		}
		
		//printing manually
//		for(int i=0;i<size;i++){
//			printf("\n%d",s[i].std_id);
//			printf("\n%s",s[i].std_name);
//			printf("\n%d",s[i].maths);
//			printf("\n%d",s[i].eng);
//			printf("\n%d",s[i].sci);
//			printf("\n%d/300",total[i]);
//			printf("\n%.2f%%",percentage[i]);
//		}

	//printing header
 	printf("------------------------------------------------------------------------------------------------------------------------\n");
 	printf("%-8s %-10s %-6s %-7s %-7s %-12s %-10s\n", "Std_id", "std_name", "Maths", "English", "Science", "Total", "Percentage");
    printf("------------------------------------------------------------------------------------------------------------------------\n");

    for (int i = 0; i < size; i++) {
    	printf("%-8d %-10s %-6d %-7d %-7d %-5d/300    %-10.2f%%\n", s[i].std_id, s[i].std_name, s[i].maths, s[i].eng, s[i].sci, total[i], percentage[i]);
    }
	
	return 0;
}
