#include <stdio.h>

int main()
{
	int A, B, V, cur;
	scanf("%d %d %d", &A, &B, &V);
	cur = (V - B - 1) / (A - B) + 1;
	printf("%d", cur);

	return 0;
}
