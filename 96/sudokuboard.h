/////
/// @file sudokuboard.h
/// @author Matthew Nuckolls CS153 Section A
/// @brief Definition of a class representing a sudoku board
/////

#ifndef SUDOKUBOARD_H
#define SUDOKUBOARD_H

/////
/// @class sudokuBoard
/// @brief A representation of a sudoku board
class sudokuBoard
{
  public:
    /////
    /// @brief default constructor
    /// @pre  none
    /// @post member variables initalized
    sudokuBoard();
    
    /////
    /// @brief getter function for specified element
    /// @pre  0 <= x,y <= 8
    /// @post none
    /// @return the value of the element at x,y
    int get( int x, int y );
    
    /////
    /// @brief Project Euler #96
    int getID();
    
    /////
    /// @clears the board
    void clear();
    
    /////
    /// @brief setter function for specified element
    ///        NOTE: will check if newly modified board is
    ///        valid partial solution. If not, board will be reset
    /// @pre  none
    /// @post board[x][y] set to value if board is valid partial solution
    ///       none otherwise
    /// @return true if the newly modified board is a partial solution
    ///         and was modified. false otherwise
    bool set( int x, int y, int value );
    
  private:
    int board[9][9]; /// two dimensional array, pretty simple
};

#endif // SUDOKUBOARD_H
