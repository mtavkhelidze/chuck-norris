#include <stdio.h>
#include <chuck-fact.h>

/*
 * Created by Misha Tavkhelidze on 10/12/19.
 *
 * Copyright (c) 2019 Misha Tavkhelidze. All rights reserved.
 */

int main()
{
    chuck_fact_t* cft = chuck_fact_init();
    printf("%s\n", chuck_fact_get(cft));
    chuck_fact_destroy(cft);
    return 0;
}
