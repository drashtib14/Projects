#include<stdio.h>
int main(){
	int choice,quantity,quantity_sum=0;
	int pizza_price=180,burger_price=100,fries_price=120,ice_price=50;
	int pizza_cnt=0,burger_cnt=0,fries_cnt=0,ice_cnt=0;
	char order;
	menu:
	printf("\n---------------Menu---------------");
	choice:
	printf("\n1.Pizza \t\t price = 180rs/pcs\n");
	printf("2.Burger \t\t price = 100rs/pcs\n");
	printf("3.French fries \t\t price = 120rs/pcs\n");
	printf("4.Ice cream \t\t price = 50rs/pcs\n");
	
	scanf("%d",&choice);

	switch(choice){
		case 1:
			printf("\nYou have selected Pizza\n");
			printf("Enter the quantity: ");
			scanf("%d",&quantity);
			if(quantity>0){
				pizza_cnt=0;
				for(int i=1;i<=quantity;i++){
					quantity_sum += pizza_price;
					pizza_cnt += pizza_price;
				}
				printf("Amount : %d",pizza_cnt);
				printf("\nTotal Amount is : %d",quantity_sum);
				printf("\nDo you want to place more orders? y & n : ");
				order:
				scanf(" %c",&order);
				if(order=='y'|| order=='Y'){
					goto menu;
				}
				else if(order=='n'|| order=='N'){
					printf("\nThank You");
					return 0;
				}
				else{
					printf("\nPlease enter y or n : ");goto order;
				}
			}
			else{
				printf("Please enter correct quantity");
			}
			break;
		case 2:
			printf("\nYou have selected Burger\n");
			printf("Enter the quantity: ");
			scanf("%d",&quantity);
			if(quantity>0){
				burger_cnt=0;
				for(int i=1;i<=quantity;i++){
					quantity_sum += burger_price;
					burger_cnt += burger_price;
				}
				printf("Amount : %d",burger_cnt);
				printf("\nTotal Amount is : %d",quantity_sum);
				printf("\nDo you want to place more orders? y & n : ");
				scanf(" %c",&order);
				if(order=='y'|| order=='Y'){
					goto menu;
				}
				else if(order=='n'|| order=='N'){
					printf("\nThank You");
					return 0;
				}
				else{
					printf("\nPlease enter y or n : ");goto order;
				}
			}
			else{
				printf("Please enter correct quantity");
			}
			break;
		case 3:
			printf("\nYou have selected French fries\n");
			printf("Enter the quantity: ");
			scanf("%d",&quantity);
			if(quantity>0){
				fries_cnt=0;
				for(int i=1;i<=quantity;i++){
					quantity_sum += fries_price;
					fries_cnt += fries_price;
				}
				printf("Amount : %d",fries_cnt);
				printf("\nTotal Amount is : %d",quantity_sum);
				printf("\nDo you want to place more orders? y & n : ");
				scanf(" %c",&order);
				if(order=='y'|| order=='Y'){
					goto menu;
				}
				else if(order=='n'|| order=='N'){
					printf("\nThank You");
					return 0;
				}
				else{
					printf("\nPlease enter y or n : ");goto order;
				}
			}
			else{
				printf("Please enter correct quantity");
			}
			break;
		case 4:
			printf("\nYou have selected Ice Cream\n");
			printf("Enter the quantity: ");
			scanf("%d",&quantity);
			if(quantity>0){
				ice_cnt=0;
				for(int i=1;i<=quantity;i++){
					quantity_sum += ice_price;
					ice_cnt += ice_price;
				}
				printf("Amount : %d",ice_cnt);
				printf("\nTotal Amount is : %d",quantity_sum);
				printf("\nDo you want to place more orders? y & n : ");
				scanf(" %c",&order);
				if(order=='y'|| order=='Y'){
					goto menu;
				}
				else if(order=='n'|| order=='N'){
					printf("\nThank You");
					return 0;
				}
				else{
					printf("\nPlease enter y or n : ");goto order;
				}
			}
			else{
				printf("Please enter correct quantity");
			}
			break;
		default:
			printf("\nPlease enter correct choice\n");
			goto choice;
	}
	
	return 0;
	}
