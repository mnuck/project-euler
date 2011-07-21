/////
/// @file sudokuboard.cpp
/// @author Matthew Nuckolls CS153 Section A
/// @brief Implementation of a class representing a sudoku board
/////

#include "sudokuboard.h"

sudokuBoard::sudokuBoard()
{
  clear();
}

void sudokuBoard::clear()
{
  for( int i = 0 ; i < 9 ; ++i )
    for( int j = 0 ; j < 9 ; ++j )
      board[i][j] = 0;
}

int sudokuBoard::get( int x, int y )
{
  return board[x][y];
}

int sudokuBoard::getID()
{
  return (100*board[0][0] + 10*board[0][1] + board[0][2]);
}


bool sudokuBoard::set( int x, int y, int value )
{
  int blockX = (x / 3) * 3;
  int blockY = (y / 3) * 3;
  int previousValue = board[x][y];

  board[x][y] = value;
  for( int j = 0 ; j < 9 ; ++j )
  {
    // first axis
    if( (x != j) && (board[j][y] == value) )
    {
      board[x][y] = previousValue;
      return false;
    }

    // second axis
    if( (y != j) && (board[x][j] == value) )
    {
      board[x][y] = previousValue;
      return false;
    }
  }

  // square block
  for( int i = blockX ; i < blockX+3 ; ++i )
  {
    for( int j = blockY ; j < blockY+3 ; ++j )
    {
      if( (x != i) && (y != j) && (board[i][j] == value) )
      {
	      board[x][y] = previousValue;
	      return false;
      }
    }
  }
  // if we made it through that gauntlet then we're good
  return true; // and the modification can stay
}
