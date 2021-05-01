#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new;

	/* create the new node */
	new = malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;

	current = *head;
	if (current  == NULL)
	{
		return (NULL);
	}
	while (current->next != NULL)
	{
		if (current->next->n > number)
		{
			/*add the node just befor*/
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	if (current->n < number && current->next == NULL)
	{
		new = add_nodeint_end(head, number);
		return (new);
	}
	return (*head);
}
