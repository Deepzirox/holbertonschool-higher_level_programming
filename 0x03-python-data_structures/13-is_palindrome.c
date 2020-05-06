#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - check if linked list is palindrome
 * @head: head of list
 * Return: 1 if palindrome, 0 not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *check = *head;
	int first = 0;
	int last = 0;

	if (check == NULL)
		return (1);

	first = check->n;
	while (check->next != NULL)
	{
		check = check->next;
	}
	last = check->n;
	if (first == last)
	{
		return (1);
	}
	return (0);
}
