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
	listint_t *current;
	listint_t *createnode;

	current = *head;
	createnode = malloc(sizeof(listint_t));
	if (createnode == NULL)
		return (NULL);
	createnode->n = number;
	if (*head == NULL || (*head)->n >number)
	{
		createnode->next = *head;
		*head = createnode;
		return(createnode);
	}

	while (current->next != NULL)
	{
		if ((current->next)->n >= number)
		{
			createnode->next = current->next;
			current->next = createnode;
			return (createnode);
		}
		current = current->next;

	}
	createnode->next = NULL;
	current->next = createnode;
	return (createnode);
}
