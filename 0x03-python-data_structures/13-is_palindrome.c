#include "lists.h"
#include <stdio.h>


/**
 * reversed - function
 * @head: arg1
 * Return: listint_t
 */
listint_t *reversed(listint_t *head)
{
	listint_t *prev = NULL;

	while (head)
	{
		listint_t *next = head->next;

		head->next = prev;
		prev = head;
		head = next;
	}
	return (prev);
}

/**
 * is_palindrome - function
 * @head: arg1
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	slow = reversed(slow);
	fast = *head;

	while (slow != NULL)
	{
		if (slow->n != fast->n)
			return (0);
		slow = slow->next;
		fast = fast->next;
	}
	return (1);
}
