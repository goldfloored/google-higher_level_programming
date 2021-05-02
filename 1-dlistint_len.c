#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

size_t dlistint_len(const dlistint_t *h)
{
size_t	len = 0;

	while (h != NULL) {
		printf("%d\n", h->n);
		h = h->next;
		len= len + 1;
	}
	return(len);
}
