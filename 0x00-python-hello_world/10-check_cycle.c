#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: pointer to check the linked list
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;/*set to head */
	listint_t *fast = list;

	if (list == NULL)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;/*jump by 2 nodes */
		if (slow == fast) /*if there is a cycle */
			return (1);
	}

	return (0);
}
