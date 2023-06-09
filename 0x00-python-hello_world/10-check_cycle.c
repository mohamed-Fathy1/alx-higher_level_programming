#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - function
 * @list: input
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *ptr = list;

	while (ptr && head && head->next)
	{
		ptr = ptr->next;
		head = head->next->next;
		if (ptr == head)
			return (1);
	}
	return (0);
}
