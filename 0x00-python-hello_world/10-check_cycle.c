#include "lists.h"

/**
 * check_cycle - checks if a single linked list has a cycle ijt
 * @list: linked list to check
 * Return: 0 if there is no cycle and 1 if there is one
 */

int check_cycle(listint_t *list)
{
	listint_t *current;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list;
	while (current->next)
	{
		if (current->next != list)
			current = current->next;
		else if (current->next == NULL)
			return (0);
		else
			return (1);
	}
	return (0);
}
