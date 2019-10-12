#include <sqlite3.h>
#include <iostream>
#include "chuck-fact.hpp"
#include "facts.hpp"


ChuckNorris::ChuckNorris()
{
    sqlite3_open(":memory:", &_db);
    sqlite3_exec(_db, sql_init, nullptr, nullptr, nullptr);
}

ChuckNorris::~ChuckNorris()
{
    sqlite3_close_v2(_db);
    _db = nullptr;
}

std::string ChuckNorris::get_fact()
{
    sqlite3_stmt* stm;

    auto rc = sqlite3_prepare_v3(_db, sql_select, -1, 0, &stm, nullptr);
    if(rc != SQLITE_OK) {
       return error_db;
    }

    rc = sqlite3_step(stm);
    if(rc != SQLITE_ROW) {
        return error_stm;
    }

    auto col_raw = sqlite3_column_text(stm, 0);
    auto col = reinterpret_cast<const char*>(col_raw);
    auto res = std::string(col);
    sqlite3_finalize(stm);
    return res;
}
