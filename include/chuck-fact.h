/*
 * Created by Misha Tavkhelidze on 10/12/19.
 *
 * Copyright (c) 2019 Misha Tavkhelidze. All rights reserved.
 */

#ifndef CHUCK_FACT_H
#define CHUCK_FACT_H

#ifdef __cplusplus
extern "C" {
#endif

typedef struct chuck_fact chuck_fact_t;
chuck_fact_t* chuck_fact_init(void);
const char* chuck_fact_get(chuck_fact_t*);
void chuck_fact_destroy(chuck_fact_t*);

#ifdef __cplusplus
};
#endif

#endif /* CHUCK_FACT_H */
