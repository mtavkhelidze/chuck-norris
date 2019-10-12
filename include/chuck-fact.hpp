#ifndef CHUCK_NORRIS_HPP
#define CHUCK_NORRIS_HPP

#include <string>
#include <sqlite3.h>

class ChuckNorrisFact {
public:
    ChuckNorrisFact();
    ~ChuckNorrisFact();

    // no copy
    ChuckNorrisFact(ChuckNorrisFact const&) = delete;
    ChuckNorrisFact operator=(ChuckNorrisFact const&) = delete;

    // no move
    ChuckNorrisFact(ChuckNorrisFact &&) = delete;
    ChuckNorrisFact operator=(ChuckNorrisFact &&) = delete;


    std::string get();

private:
    sqlite3 *_db = nullptr;
};

#endif // CHUCK_NORRIS_HPP
