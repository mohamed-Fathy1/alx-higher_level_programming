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
	int half_list;

	while (ptr1)
	{
		ptr1 = ptr1->next;
		len++;
	}

	half_list = len / 2;

	ptr1 = *head;
	while (len != half_list)
	{
		int i = 0;
		listint_t *ptr2 = *head;

		while (i != len - 1)
		{
			ptr2 = ptr2->next;
			i++;
		}
		len--;
		if (ptr1->n != ptr2->n)
			return (0);
		ptr1 = ptr1->next;
	}
	return (1);
}
