#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - function.
 * @head: input
 * @number: input
 * Return: listint_t.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head;
	listint_t *new_node = NULL;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	if (!ptr || ptr->n >= number)
	{
		new_node->n = number;
		new_node->next = ptr;
		*head = new_node;
		return (new_node);
	}

	while (ptr && ptr->next && ptr->next->n < number)
		ptr = ptr->next;

	new_node->n = number;
	new_node->next = ptr->next;
	ptr->next = new_node;
	return (new_node);
}
