all: $(patsubst %.cpp, %.out, $(wildcard test*.cpp))

%.out: %.cpp
	g++ -Wall -pedantic $< -std=c++11 -o $@

clean: 
	rm *.out

