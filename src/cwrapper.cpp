#include <chuck-fact.h>

/*
 * Created by Misha Tavkhelidze on 10/12/19.
 *
 * Copyright (c) 2019 Misha Tavkhelidze. All rights reserved.
 */

#include <chuck-fact.hpp>

#pragma clang diagnostic push
#pragma ide diagnostic ignored "OCDFAInspection"

chuck_fact_t* chuck_fact_init(void)
{
    auto cnf = new ChuckNorrisFact();
    return reinterpret_cast<chuck_fact_t*>(cnf);
}

const char* chuck_fact_get(chuck_fact_t* cnft)
{
    auto cnf = reinterpret_cast<ChuckNorrisFact*>(cnft);
    std::string fact = cnf->get();
    const char* r = fact.c_str();
    return strdup(r);
}

void chuck_fact_destroy(chuck_fact_t* cnft)
{
    auto cnf = reinterpret_cast<ChuckNorrisFact*>(cnft);
    delete cnf;
}

#pragma clang diagnostic pop
