#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - Inserts a number into a sorted linked list
 * @head: Pointer to a pointer to the head of the linked list
 * @number: The value to insert into the linked list
 *
 * Return: Address of the new node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
