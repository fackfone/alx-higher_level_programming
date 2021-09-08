#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a node in a sorted linked list
 * @head: pointer to a pointer of first node of listint_t
 * @number: integer to be included in the new node
 * Return: address of the new element or it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *nextnode;
	listint_t *createnode;
	int num1, num2;

	current = *head;
	nextnode = current->next;
	createnode = malloc(sizeof(listint_t));
	if (createnode == NULL)
		return (NULL);
	createnode->n = number;

	while (current->next != NULL)
	{
		current = current->next;
		num1 = current->n;
		num2 = (current->next)->n;
		if (num1 < number && num2 > number)
		{
			nextnode = current->next;
			current->next = createnode;
			createnode->next = nextnode;
			return (createnode);
		}

	}
	return (NULL);
}
