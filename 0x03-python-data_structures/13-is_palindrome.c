#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - function
 * @head: arg1
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr1 = *head;
	int len = 0;
	int x = 0;
	int c = 0;
	int arr[1000000];

	while (ptr1)
	{
		ptr1 = ptr1->next;
		len++;
	}

	ptr1 = *head;
	while (ptr1)
	{
		arr[x] = ptr1->n;
		ptr1 = ptr1->next;
		x++;
	}
	ptr1 = *head;

	while (c != len)
	{
		if (ptr1->n != arr[--len])
			return (0);
		ptr1 = ptr1->next;
	}
	return (1);
}
