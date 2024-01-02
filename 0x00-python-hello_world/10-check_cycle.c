#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checking for cycles
 * @list: linked list
 * Return: 1 if there a cycle and 0 if there is not
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
