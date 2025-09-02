
# 1. Ajouter le path + nom du fichier aux alias (recommandé)
# 2. allez dans le dir ou sont placés votre srcs/ et include/
# 3. executez le programme avec python3 (soit par l'alias soit directement)
# 4. le programme vous demande le nom de la classe que vous voulez créer
# 5. tape le nom de la classe !

base_hpp = """

#pragma once

INCLUDES

class CLASSNAME {
	public :
	// CONSTRUCTORS
		CLASSNAME();
		CLASSNAME(CLASSNAME &other);
		CLASSNAME &operator=(CLASSNAME &other);
	//DESTUCTORS
		~CLASSNAME();
	//GETTERS
	//SETTERS
	//MEMBER FUNCTIONS
	private :
};"""

base_include = """#include <cstdio>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>"""

classname = input("enter class name :")

base_hpp = base_hpp.replace("CLASSNAME", classname).replace("INCLUDES", base_include)

with open("include/" + classname + ".hpp", 'w') as hpp:
    hpp.write(base_hpp)

base_cpp = """

#include "CLASSNAME.hpp"

CLASSNAME::CLASSNAME() {}

CLASSNAME::CLASSNAME(CLASSNAME &other)
{
}

CLASSNAME &CLASSNAME::operator=(CLASSNAME &other)
{
}

CLASSNAME::~CLASSNAME() {}

"""

base_cpp = base_cpp.replace("CLASSNAME", classname)

with open("srcs/" + classname + ".cpp", 'w') as cpp:
    cpp.write(base_cpp)