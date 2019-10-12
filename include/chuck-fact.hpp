#ifndef CHUCK_NORRIS_HPP
#define CHUCK_NORRIS_HPP

#include <string>
#include <sqlite3.h>

class ChuckNorris {
public:
    ChuckNorris();
    ~ChuckNorris();

    // no copy
    ChuckNorris(ChuckNorris const&) = delete;
    ChuckNorris operator=(ChuckNorris const&) = delete;

    // no move
    ChuckNorris(ChuckNorris &&) = delete;
    ChuckNorris operator=(ChuckNorris &&) = delete;


    std::string get_fact();

private:
    sqlite3 *_db = nullptr;
};

#endif // CHUCK_NORRIS_HPP
