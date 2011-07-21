/////
/// @file main.cpp
/// @author Matthew Nuckolls CS153 Section A
/// @brief Wrapper main() for unit tests
/////

#include <iostream>
#include <fstream>
#include "sudokuboard.h"
using namespace std;


void loadBoard( char* filename, sudokuBoard& b )
{
  ifstream infile( filename );
  int element;

  for( int i = 0 ; i < 9 ; ++i )
  {
    for( int j = 0 ; j < 9 ; ++j )
    {
      infile >> element;
      b.set( i, j, element );
    }
  }
  infile.close();
}

void loadBoard( ifstream& infile, sudokuBoard& b )
{
  string junk;
  char buffer;
  int num;
  
  getline( infile, junk ); // Grid XX
  for( int i = 0 ; i < 9 ; ++i )
  {
    for( int j = 0 ; j < 9 ; ++j )
    {
      buffer = infile.get();
      num = buffer - 48;
      b.set( i, j, num );
    }
    buffer = infile.get(); // catch the \n
    buffer = infile.get(); // catch the \n
  }
}


void sudokuSolve( int* kk, int k, sudokuBoard b, sudokuBoard& final, 
		  bool& done, int& iterations )
{
  iterations++;
  int x = kk[k] % 9;
  int y = kk[k] / 9;

  if( k == 81 ) // we're done, yay!
  {
    final = b;
    done = true;
  }
  else if( b.get( x, y ) != 0 ) // this is a "fixed" block
    sudokuSolve( kk, k+1, b, final, done, iterations );
  else
  {
    for( int i = 1 ; i <= 9  && !done ; ++i )
    {
      if( b.set( x, y, i ) )
	      sudokuSolve( kk, k+1, b, final, done, iterations );
    }
  }
}


void optimizeSearch( int* kk, sudokuBoard& b )
{
  for( int i = 0 ; i < 81 ; ++i )
    kk[i] = i;
}


void printBoard( sudokuBoard& b )
{
  cout << "-----+-----+-----+" << endl;
  for( int i = 0 ; i < 9 ; ++i )
  {
    for( int j = 0 ; j < 9 ; ++j )
    {
      cout << b.get(i, j);
      if((j+1) % 3 == 0)
	cout << "|";
      else
	cout << " ";
    }
    cout << endl;
    if((i+1) % 3 == 0 )
      cout << "-----+-----+-----+" << endl;
  }
}


/////
/// @brief main()
// int main()
// {
//   int k = 0;
//   int iterations = 0;
//   int kk[81];
//   sudokuBoard b, final;
//   bool done = false;
// 
//   srand( time( NULL ) );
// 
//   loadBoard( "board.txt", b );
// 
//   optimizeSearch( kk, b );
// 
//   sudokuSolve( kk, k, b, final, done, iterations );
// 
//   printBoard( final );
// 
//   cout << "iterations: " << iterations << endl;
// 
//   return 0;
// }

int main()
{
  int k = 0;
  int iterations = 0;
  int kk[81];
  sudokuBoard b, final;
  bool done;
  ifstream infile( "sudoku.txt" );
  
  int accumulator = 0;
  
  for( int i = 0 ; i < 50 ; ++i )
  {
    done = false;
    loadBoard( infile, b );
    optimizeSearch( kk, b );
    sudokuSolve( kk, k, b, final, done, iterations );
    accumulator += final.getID();
    b.clear();
    final.clear();
  }
  
  infile.close();
  
  cout << accumulator << endl;
  
  return 0;
}